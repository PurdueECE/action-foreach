# Action Foreach
This action will run a specified job on a list of repos. It accomplishes this by cloning the specified repos into a single repo and creating a workflow file where a specified job is created for each repo in the list.

# Usage
```yaml
- uses: PurdueECE/action-foreach@master
  id: run_repos
  with:
    # Repo to clone all provided repos into. Defaults to ${{ github.repository }}
    monorepo: ${{ github.repository }}
    # Working directory under monorepo to clone repos to. Defaults to ./
    monorepo_workdir: ./
    # List of repos to run action for.
    repos: org/repo-1,org/repo-2,org/repo-3
    # Action YAML file contents to run on each repo.
    action:
name: Pylint - ${{ env.REPO }}
on: [push]
jobs:
  pylint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: PurdueECE/action-pylint@main
        with:
          path: ${{ env.REPO_DIR }}/Prelab06
```

The `REPO` environment variable is set in each repo's workflow file. It's format is `owner/name`.

The `REPO_DIR` environment variable is set in each repo's workflow file to be the subdirectory within the monorepo. This variable should be used if any paths within each repo need to be referenced.

# Testing
## Unit
Unit tests are in the `test_unit/` directory. They can be run with `pytest`.
## Integration
Integration test cases are in the `test_integration/` directory.
To test, you must install the [`act`](https://github.com/nektos/act) command line tool.
After install, run `make test`.