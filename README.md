# Action Foreach
This action will run a specified job on a list of repos. It accomplishes this by cloning the specified repos into a single repo and creating a workflow file where a specified job is created for each repo in the list.

# Usage
```yaml
- uses: PurdueECE/action-foreach@master
  id: run_repos
  with:
    # Comma-separated list of repos
    repos: org/repo-1,org/repo-2,org/repo-3
    # Personal access token
    token: ${{ github.token }}
    # Action to run in each repo
    action:
name: Foreach Action
on: [push]
jobs:
  print:
    runs-on: ubuntu-latest
    steps:
      - run: "echo repo: ${{ github.repository }}"
```

# Testing
## Unit
Unit tests are in the `test_unit/` directory. They can be run with `pytest`.
## Integration
Integration test cases are in the `test_integration/` directory.
To test, you must install the [`act`](https://github.com/nektos/act) command line tool.
After install, run `make test`.