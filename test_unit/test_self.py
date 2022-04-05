import os
from main import main
from unittest import mock

@mock.patch.dict(os.environ, {
    "GITHUB_WORKSPACE": "./test_unit/data",
    "GITHUB_REPOSITORY_OWNER": "PurdueECE",
    "INPUT_REPOS": "PurdueECE/action-foreach",
    "INPUT_LOOP": """
    runs-on: ubuntu-latest
    steps:
      - run: "echo repo: ${{ github.repository }}"
"""
    })
def test_self():
    main()