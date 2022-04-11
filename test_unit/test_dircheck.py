import os
from main import main
from unittest import mock

@mock.patch.dict(os.environ, {
  "GITHUB_WORKFLOW": "Foreach Dircheck",
  "GITHUB_REF_NAME": "main",
  "INPUT_WORKDIR": "test_data",
  "INPUT_REPOS": "PurdueECE364/prelabs-moffatw",#,PurdueECE364/prelabs-bbelli,PurdueECE364/prelabs-SOGIST1",
  "INPUT_WORKFLOW": """
name: Dircheck Test
on: [push]
jobs:
  dircheck:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: PurdueECE/action-dircheck@main
        with:
          paths: ${{ env.REPO_DIR }}/Prelab08/src
"""
    })
def test_dircheck():
  main()