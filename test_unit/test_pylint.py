import os
from main import main
from unittest import mock

@mock.patch.dict(os.environ, {
  "GITHUB_WORKFLOW": "Foreach Pylint",
  "GITHUB_REF_NAME": "main",
  "INPUT_WORKDIR": "test_data",
  "INPUT_REPOS": "PurdueECE364/prelabs-moffatw",#,PurdueECE364/prelabs-bbelli,PurdueECE364/prelabs-SOGIST1",
  "INPUT_WORKFLOW": """
name: Pylint Test
on:
  workflow_run:
    workflows: [${{ github.workflow }}]
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