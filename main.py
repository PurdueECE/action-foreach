import datetime
import os
import shutil

from actions_toolkit import core
from git import Repo
from github import Github, UnknownObjectException


def run_foreach():
    # Get monorepo owner & name
    mr_owner, mr_name = core.get_input('monorepo').split('/')
    # GitHub init
    gh_api = Github(os.environ['GITHUB_TOKEN'])
    # Clone monorepo
    org = gh_api.get_organization(mr_owner)
    try:
        remote = org.get_repo(mr_name)
    except UnknownObjectException as e:
        if e.status == 404:
            remote = org.create_repo(mr_name)
    workdir = f'{os.environ["GITHUB_WORKSPACE"]}/{mr_name}'
    if os.path.exists(workdir):
        shutil.rmtree(workdir)
    monorepo = Repo.clone_from(remote.clone_url, workdir)
    # Set up workflows path
    wf_dir = f'{workdir}/.github/workflows'
    os.makedirs(wf_dir, exist_ok = True)
    # Clone each repo into monorepo
    mr_workdir = f'{workdir}/{core.get_input("monorepo_workdir")}'
    for full_name in core.get_input('repos').split(','):
        owner, name = full_name.split('/')
        repo_prefix = f'{owner}-{name}'
        repo_dir = f'{mr_workdir}/{repo_prefix}'
        # Create workflow file
        with open(f'{wf_dir}/{repo_prefix}-workflow.yml', "w") as f:
            f.write(f'env:\n')
            f.write(f'  REPO: {full_name}\n')
            f.write(f'  REPO_DIR: {os.path.relpath(mr_workdir, workdir)}\n')
            f.write(f'{core.get_input("action")}\n')
        # Clone repo
        if os.path.exists(repo_dir):
            shutil.rmtree(repo_dir)
        Repo.clone_from(f'https://{os.environ["GITHUB_TOKEN"]}:x-oauth-basic@github.com/{owner}/{name}.git', repo_dir)
        shutil.rmtree(f'{repo_dir}/.git') # deinit as git repo so it is pushed to GH properly
    # Commit to remote
    monorepo.git.add('.')
    monorepo.index.commit(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    monorepo.git.push('--set-upstream', monorepo.remote().name, 'master', '--force')

def set_default_env():
    #os.environ.setdefault('INPUT_MONOREPO', os.environ['GITHUB_REPOSITORY'])
    pass

def main():
    try:
        set_default_env()
        run_foreach()
    except Exception as e:
        core.set_failed(str(e))
        
if __name__ == "__main__":
    main()
