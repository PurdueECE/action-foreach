import datetime
import os
import shutil

from actions_toolkit import core
from git import Repo

def run_foreach():
    # Set up workflows path
    wf_dir = f'.github/workflows'
    os.makedirs(wf_dir, exist_ok = True)
    # Clone each repo
    workdir = core.get_input("workdir")
    for full_name in core.get_input('repos').split(','):
        owner, name = full_name.split('/')
        repo_prefix = f'{owner}-{name}'
        repo_dir = f'{workdir}/{repo_prefix}'
        # Create workflow file
        with open(f'{wf_dir}/action-foreach-{repo_prefix}-workflow.yml', "w") as f:
            f.write(f'env:\n')
            f.write(f'  REPO: {full_name}\n')
            f.write(f'  REPO_DIR: {repo_dir}\n')
            f.write(f'{core.get_input("workflow")}\n')
        # Clone repo
        if os.path.exists(repo_dir):
            shutil.rmtree(repo_dir)
        Repo.clone_from(f'https://{os.environ["GITHUB_TOKEN"]}:x-oauth-basic@github.com/{owner}/{name}.git', repo_dir)
        shutil.rmtree(f'{repo_dir}/.git') # deinit as git repo so it is pushed to GH properly
    # Commit to remote
    monorepo = Repo('.')
    monorepo.git.add('.')
    monorepo.index.commit(f'{os.environ["GITHUB_ACTION"]} - {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    monorepo.git.push('--set-upstream', monorepo.remote().name, 'master', '--force')

def env_setup():
    if os.environ.get('GITHUB_EVENT', '') == 'push':
        raise Exception('Refusing to run on push event to avoid recursive GH action runs.')

def main():
    try:
        env_setup()
        run_foreach()
    except Exception as e:
        core.set_failed(str(e))
        
if __name__ == "__main__":
    main()
