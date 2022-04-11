# Action Foreach
This action will run a specified action on a list of repos. It accomplishes this by cloning the specified repos and generating workflow files for each repo whose contents are specified in this action.


# Usage
```yaml
- uses: PurdueECE/action-foreach@master
  id: run_repos
  with:
    # Personal access token
    token: ${{ github.token }}
    # Working directory to clone repos to. Defaults to 'action-foreach'.
    workdir: 'action-foreach'
    # List of repos to run action for.
    repos: org/repo-1,org/repo-2,org/repo-3
    # Workflow to run in each repo. Should be entered as string.
    workflow: '
name: Pylint Action
on: push
jobs:
  pylint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: PurdueECE/action-pylint@main
        with:
          path: ${{ env.REPO_DIR }}/Prelab06'
```
The `REPO` environment variable is set in each repo's workflow file. Its format is `owner/repo`.

The `REPO_DIR` environment variable is set in each repo's workflow file to be the subdirectory where the individual repo is located. This variable should be used if any paths within each repo need to be referenced in its workflow (see above example).

## Important Notes
It is recommended to set the trigger in the `workflow` input to `on: push`, otherwise the generated workflows will not run immediately.

It is NOT recommended to set the trigger for the workflow that calls `action-foreach` to be `on: push`. This is because an infinite recursion will occur: the foreach action will run on a push which will push a new commit with the generated workflows that will again cause the foreach action to be run.

To avoid the above scenario, this action will refuse to run if the event that triggered it is a `push`.

Therefore, it is recommended to set the trigger for this action to be either `on: workflow_dispatch` or `on: schedule`. Please see the [documentation](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows) for more details.


# Testing
## Unit
Unit tests are in the `test_unit/` directory. They can be run with `pytest`.
## Integration
Integration test cases are in the `test_integration/` directory.
To test, you must install the [`act`](https://github.com/nektos/act) command line tool.
After install, run `make test`.