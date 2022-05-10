# Deprecation Notice
This repository has been deprecated because [build matrices](https://docs.github.com/en/github-ae@latest/actions/using-jobs/using-a-matrix-for-your-jobs) can accomplish this function. See [PurdueECE/action-find-repos](https://github.com/PurdueECE/action-find-repos#run-job-on-each-repository) for an example on how to retrieve a list of repos and run a job on each one.

# Action Foreach
This action will run a specified action on a list of repos. It accomplishes this by cloning the specified repos and generating workflow files for each repo whose contents are specified in this action.

# Usage
```yaml
name: Foreach Action
on: [workflow_dispatch]

jobs:
  foreach:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: PurdueECE/action-foreach@v2
        with:
          # Personal access token
          token: ${{ github.token }}
          # List of repos to run action for.
          repos: org/repo-1,org/repo-2,org/repo-3
          # Working directory to clone repos to. Defaults to .
          workdir: 'action-foreach-runs'
          # Re-use repos if they exist in workdir.
          reuse: false
          # Jobs to run for each repo. Should be entered using YAML [literal style](https://yaml.org/spec/1.2.2/#812-literal-style)
          jobs: |
            print:
              runs-on: ubuntu-latest
              steps:
                - run: echo "repo = $REPO"
            pylint:
              runs-on: ubuntu-latest
              steps:
                - uses: actions/checkout@v3
                - uses: PurdueECE/action-pylint@main
                  with:
                    path: $REPO_DIR/Prelab06'
```
The `REPO` environment variable is set in each repo's workflow file. Its format is `owner/repo` (see example above).

The `REPO_DIR` environment variable is set in each repo's workflow file to be the subdirectory where the individual repo is located. This variable should be used if any paths within each repo need to be referenced in its workflow (see example above).


# Testing
Unit tests are in the `test_unit/` directory. They can be run with `pytest`.
