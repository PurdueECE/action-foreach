import datetime
import os
import shutil

from git import Repo
from actions_toolkit import core
from github import Github, Repository, UnknownObjectException


def run_foreach(args):
    # env init
    monorepo_name = 'action_foreach_run'
    workdir = os.environ.get('GITHUB_WORKSPACE', '/usr/src/app') + f'/{monorepo_name}'
    # GitHub init
    github = Github(args['token'])
    org = github.get_organization(os.environ["GITHUB_REPOSITORY_OWNER"])
    try:
        remote = org.get_repo(monorepo_name)
    except UnknownObjectException as e:
        if e.status == 404:
            remote: Repository.Repository = org.create_repo(monorepo_name)
    # Clone monorepo
    if os.path.exists(workdir):
        shutil.rmtree(workdir)
    monorepo = Repo.clone_from(remote.clone_url, workdir)
    workflow_path = f'{workdir}/.github/workflows'
    os.makedirs(workflow_path, exist_ok = True)
    with open(f'{workflow_path}/workflow.yml', "w") as f:
        f.write(f"name: Foreach Actions\n")
        f.write(f"on: [push]\n")
        f.write(f"jobs:\n")
    # Fill in monorepo
    for repo_name in args['repos'].split(','):
        # Clone each repo
        gh_repo = github.get_repo(repo_name)
        repo_dir = f"{workdir}/{repo_name}"
        if os.path.exists(repo_dir):
            shutil.rmtree(repo_dir)
        Repo.clone_from(gh_repo.clone_url, repo_dir)
        shutil.rmtree(f'{repo_dir}/.git')
        # Copy action job
        with open(f'{workflow_path}/workflow.yml', "a+") as f:
            f.write(args['loop'])
    # Commit to remote
    monorepo.git.add(all=True)
    monorepo.index.commit(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    monorepo.git.push('--set-upstream', monorepo.remote().name, 'master', '--force')

def parse_env():
    inputs = ['token', 'repos', 'loop']
    args = {}
    for input in inputs:
        args[input] = core.get_input(input, trim_whitespace = False)
    return args

def set_default_env():
    os.environ.setdefault('INPUT_TOKEN', os.environ.get('GITHUB_TOKEN', ''))

def main():
    try:
        set_default_env()
        args = parse_env()
        run_foreach(args)
    except Exception as e:
        core.set_failed(str(e))
        
if __name__ == "__main__":
    main()
