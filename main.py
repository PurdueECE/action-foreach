import datetime
import os
import shutil

from actions_toolkit import core
from git import Repo
from github import Github, UnknownObjectException


def run_foreach(args):
    # env init
    monorepo_name = 'action_foreach_run'
    work_dir = os.environ.get('GITHUB_WORKSPACE', '/github/workspace') + f'/{monorepo_name}'
    # GitHub init
    github = Github(args['token'])
    org = github.get_organization(os.environ["GITHUB_REPOSITORY_OWNER"])
    try:
        remote = org.get_repo(monorepo_name)
    except UnknownObjectException as e:
        if e.status == 404:
            remote = org.create_repo(monorepo_name)
    # Clone monorepo
    if os.path.exists(work_dir):
        shutil.rmtree(work_dir)
    monorepo = Repo.clone_from(remote.clone_url, work_dir)
    workflow_path = f'{work_dir}/.github/workflows'
    os.makedirs(workflow_path, exist_ok = True)
    # Fill in monorepo
    for full_name in args['repos'].split(','):
        owner, name = full_name.split('/')
        repo_prefix = f'{owner}-{name}'
        # Create workflow file
        with open(f'{workflow_path}/{repo_prefix}-workflow.yml', "w") as f:
            f.write(f'env:\n')
            f.write(f'  REPO_DIR: {repo_prefix}\n')
            f.write(f'{args["action"]}\n')
        # Clone repo
        repo_dir = f"{work_dir}/{repo_prefix}"
        if os.path.exists(repo_dir):
            shutil.rmtree(repo_dir)
        Repo.clone_from(f'https://{args["token"]}:x-oauth-basic@github.com/{owner}/{name}.git', repo_dir)
        shutil.rmtree(f'{repo_dir}/.git')
    # Commit to remote
    monorepo.git.add('.')
    monorepo.index.commit(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    monorepo.git.push('--set-upstream', monorepo.remote().name, 'master', '--force')

def parse_env():
    inputs = ['token', 'repos', 'action']
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
