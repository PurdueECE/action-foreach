import datetime
import os
import shutil

from actions_toolkit import core
from git import Repo

def run_foreach():
    # Set up paths
    wf_dir = f'.github/workflows'
    os.makedirs(wf_dir, exist_ok = True)
    workdir = f'{core.get_input("workdir")}/run-{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}'
    # Clone each repo
    for full_name in core.get_input('repos').split(','):
        owner, name = full_name.split('/')
        repo_prefix = f'{owner}-{name}'
        repo_dir = f'{workdir}/{repo_prefix}'
        os.makedirs(repo_dir, exist_ok = True)
        # Create workflow file
        with open(f'{wf_dir}/action-foreach-{repo_prefix}-workflow.yml', "w") as f:
            f.write(f'env:\n')
            f.write(f'  REPO: {full_name}\n')
            f.write(f'  REPO_DIR: {repo_dir}\n')
            f.write(f'{core.get_input("workflow", trim_whitespace = False)}\n')
        # Clone repo
        if os.path.exists(repo_dir):
            shutil.rmtree(repo_dir)
        Repo.clone_from(f'https://{core.get_input("token")}:x-oauth-basic@github.com/{owner}/{name}.git', repo_dir)
        shutil.rmtree(f'{repo_dir}/.git') # deinit as git repo so it is pushed to GH properly
    # Commit to remote
    monorepo = Repo('.')
    monorepo.git.add(workdir)
    monorepo.git.add(wf_dir)
    monorepo.index.commit(f'{core.get_input("token")} - {datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")}')
    monorepo.git.push('--set-upstream', monorepo.remote().name, os.environ['GITHUB_REF_NAME'])

def env_setup():
    if os.environ.get('GITHUB_EVENT', '') == 'push':
        raise Exception('Refusing to run on push event to avoid recursive runs.')
    os.environ.setdefault('INPUT_TOKEN', os.environ.get('GITHUB_TOKEN', ''))

def main():
    try:
        env_setup()
        run_foreach()
    except Exception as e:
        core.set_failed(str(e))
        
if __name__ == "__main__":
    main()
