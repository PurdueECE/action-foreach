import os
from main import main
from unittest import mock

@mock.patch.dict(os.environ, {
    "INPUT_MONOREPO": "PurdueECE/action-foreach",
    "INPUT_MONOREPO_WORKDIR": "foreach_runs",
    "INPUT_REPOS": "PurdueECE364/prelabs-moffatw",#,PurdueECE364/prelabs-bbelli,PurdueECE364/prelabs-SOGIST1",
    "INPUT_ACTION": """
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
"""
    })
def test_pylint():
  main()