import os
from main import main
from unittest import mock

@mock.patch.dict(os.environ, {
    "GITHUB_WORKSPACE": "./test_unit/data",
    "GITHUB_REPOSITORY_OWNER": "PurdueECE",
    "INPUT_REPOS": "PurdueECE364/prelabs-moffatw",#,PurdueECE364/prelabs-bbelli,PurdueECE364/prelabs-SOGIST1",
    "INPUT_ACTION": """
name: Pylint - ${{ env.REPO_DIR }}
on: [push]
jobs:
  pylint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: PurdueECE/action-pylint@main
        with:
          path: ${{ env.REPO_DIR }}/Prelab06
"""
    })
def test_pylint():
  main()