import datetime
import os
import shutil

from actions_toolkit import core
from git import Repo

def run_foreach():
    # Set up paths
    wf_dir = f'.github/workflows'
    os.makedirs(wf_dir, exist_ok = True)
    wf_prefix = os.environ["GITHUB_WORKFLOW"].replace(" ", "-")
    workdir = f'{core.get_input("workdir")}'
    # Create each workflow & clone repo
    for full_name in core.get_input('repos').split(','):
        owner, name = full_name.split('/')
        repo_prefix = f'{owner}-{name}'
        repo_dir = f'{workdir}/{repo_prefix}'
        os.makedirs(repo_dir, exist_ok = True)
        # Create workflow file
        with open(f'{wf_dir}/{wf_prefix}-{repo_prefix}.yml', "w") as f:
            f.write(f'name: {os.environ["GITHUB_WORKFLOW"]} - {repo_prefix}\n')
            f.write(f'on:\n')
            f.write(f'  workflow_run:\n')
            f.write(f'      workflows: [{os.environ["GITHUB_WORKFLOW"]}]\n')
            f.write(f'env:\n')
            f.write(f'  REPO: {full_name}\n')
            f.write(f'  REPO_DIR: {repo_dir}\n')
            f.write(f'jobs:\n')
            f.writelines(map(lambda x: f'  {x}\n', os.environ["INPUT_JOBS"].splitlines()))
        # Delete existing repo
        if os.environ['INPUT_REUSE'] == 'false':
            shutil.rmtree(repo_dir, ignore_errors=True)
        # Clone new repo
        if os.path.exists(repo_dir) == False:
            Repo.clone_from(f'https://{core.get_input("token")}:x-oauth-basic@github.com/{owner}/{name}.git', repo_dir)
        # Deinit git repo so it is pushed to GH properly
        shutil.rmtree(f'{repo_dir}/.git', ignore_errors= True)
    # Commit to remote
    monorepo = Repo('.')
    monorepo.git.add(workdir)
    monorepo.git.add(wf_dir)
    monorepo.index.commit(f'{os.environ["GITHUB_WORKFLOW"]} - {datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")}')
    monorepo.git.push('--set-upstream', monorepo.remote().name, os.environ['GITHUB_REF_NAME'], '--force')

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
