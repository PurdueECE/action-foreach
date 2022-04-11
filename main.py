import datetime
import os
import shutil

from actions_toolkit import core
from git import Repo

def run_foreach():
    # Set up path
    wf_dir = f'.github/workflows'
    os.makedirs(wf_dir, exist_ok = True)
    # For each repo
    for full_name in core.get_input('repos').split(','):
        owner, name = full_name.split('/')
        repo_prefix = f'{owner}-{name}'
        # Create workflow file
        with open(f'{wf_dir}/action-foreach-{repo_prefix}-workflow.yml', "w") as f:
            f.write(f'name: {os.environ["GITHUB_WORKFLOW"]} - {repo_prefix}\n')
            f.write(f'on:\n')
            f.write(f'  workflow_run:\n')
            f.write(f'      workflows: [{os.environ["GITHUB_WORKFLOW"]}]\n')
            f.write(f'env:\n')
            f.write(f'  REPO: {full_name}\n')
            f.write(f'jobs:\n')
            f.writelines(map(lambda x: f'  {x}\n', os.environ["INPUT_JOBS"].splitlines()))
    # Commit to remote
    monorepo = Repo('.')
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
