import datetime
import os
import shutil

from git import Repo, Git
from actions_toolkit import core
from github import Github, Repository, UnknownObjectException


def run_foreach(args):
    # env init
    monorepo_name = 'action_foreach_run'
    workdir = os.environ.get('GITHUB_WORKSPACE', '/usr/src/app') + f'/{monorepo_name}'
    # GitHub init
    github = Github(args['token'])
    org = github.get_organization(os.environ["GITHUB_REPOSITORY_OWNER"])
    # Create monorepo
    for repo_name in args['repos'].split(','):
        # Clone the repo
        gh_repo = github.get_repo(repo_name)
        repo_dir = f"{workdir}/{repo_name}"
        Repo.clone_from(gh_repo.clone_url, repo_dir)
        shutil.rmtree(f'{repo_dir}/.git')
        # Copy action contents
        workflow_path = f'{repo_dir}/.github/workflows'
        os.makedirs(workflow_path, exist_ok = True)
        with open(f'{workflow_path}/workflow.yml', "w") as f:
            f.write(f"name: Foreach Run - {repo_name}\n")
            f.write(f"on: [workflow_dispatch]\n")
            f.write(f"env:\n    repo: {repo_name}\n")
            f.write(f"{args['loop']}\n")
    # Create remote if it doesn't exist
    try:
        remote = org.get_repo(monorepo_name)
    except UnknownObjectException as e:
        if e.status == 404:
            remote: Repository.Repository = org.create_repo(monorepo_name)
    # Commit the repo
    monorepo = Repo.init(workdir)
    monorepo.create_remote('origin', remote.clone_url)
    monorepo.git.add(all=True)
    monorepo.index.commit('initial files')
    monorepo.git.push('--set-upstream', monorepo.remote().name, 'master', '--force')
    shutil.rmtree(workdir)
    # Dispatch the workflow event
    workflows = remote.get_workflows()
    remaining = workflows.totalCount; idx = 0
    while remaining > 0:
        page = workflows.get_page(idx)
        for workflow in page:
            print(workflow.name)
        idx += 1
        remaining -= len(page)

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
