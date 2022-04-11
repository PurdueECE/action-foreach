import os
from main import main
from unittest import mock

@mock.patch.dict(os.environ, {
  "GITHUB_WORKFLOW": "Dircheck Test",
  "GITHUB_REF_NAME": "main",
  "INPUT_REPOS": "PurdueECE364/prelabs-moffatw",#,PurdueECE364/prelabs-bbelli,PurdueECE364/prelabs-SOGIST1",
  "INPUT_JOBS": """dircheck:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v3
      with:
        repository: $REPO
        token: ${{ secrets.PAT }}
    - uses: PurdueECE/action-dircheck@main
      with:
        paths: Prelab08/src
"""
    })
def test_dircheck():
  main()