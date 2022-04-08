import os
from main import main
from unittest import mock

@mock.patch.dict(os.environ, {
  "GITHUB_ACTION": "Foreach Print",
  "INPUT_WORKDIR": "foreach_runs",
  "INPUT_REPOS": "PurdueECE364/prelabs-moffatw",#,PurdueECE364/prelabs-bbelli,PurdueECE364/prelabs-SOGIST1",
  "INPUT_WORKFLOW": """
name: Print Test
on: [push]
jobs:
  print:
    runs-on: ubuntu-latest
    steps:
      - run: "echo repo: ${{ env.REPO_DIR }}"
"""
    })
def test_print():
  main()