import os
from main import main
from unittest import mock

@mock.patch.dict(os.environ, {
  "GITHUB_WORKFLOW": "Foreach Print",
  "GITHUB_REF_NAME": "main",
  "INPUT_WORKDIR": "test_data",
  "INPUT_REPOS": "PurdueECE364/prelabs-moffatw",#,PurdueECE364/prelabs-bbelli,PurdueECE364/prelabs-SOGIST1",
  "INPUT_WORKFLOW": """
name: Print Test
on:
  workflow_run:
    workflows: [${{ github.workflow }}]
jobs:
  print:
    runs-on: ubuntu-latest
    steps:
      - run: "echo repo: ${{ env.REPO }}"
"""
    })
def test_print():
  main()