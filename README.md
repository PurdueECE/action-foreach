# Action Foreach
This action run another action on a list of repos

# Usage
```yaml
- uses: PurdueECE/action-foreach@main
  id: run_repos
  with:
    # Comma-separated list of repos
    repos: PurdueECE364/prelabs-1,PurdueECE364/prelabs-2
    # Personal access token
    pat: ${{ secrets.GITHUB_TOKEN }}
    # action
    foreach: PurdueECE/action-dircheck
```

# Testing
## Unit
Unit tests are in the `test-unit/` directory. They can be run with `pytest`.
## Integration
Integration test cases are in the `test-integration/` directory.
To test, you must install the [`act`](https://github.com/nektos/act) command line tool.
After install, run `make test`.