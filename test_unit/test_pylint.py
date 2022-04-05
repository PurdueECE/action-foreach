import os
from main import main
from unittest import mock

@mock.patch.dict(os.environ, {
    "GITHUB_WORKSPACE": "./test_unit/data",
    "GITHUB_REPOSITORY_OWNER": "PurdueECE",
    "INPUT_REPOS": "PurdueECE364/prelabs-kkunovsk,PurdueECE364/prelabs-ineizera,PurdueECE364/prelabs-akikos99",#,PurdueECE364/prelabs-Aznricerr,PurdueECE364/prelabs-sundeyuan114,PurdueECE364/prelabs-aowngong,PurdueECE364/prelabs-adrianchen8662,PurdueECE364/prelabs-christinefang,PurdueECE364/prelabs-bbelli,PurdueECE364/prelabs-wxjdsr,PurdueECE364/prelabs-ParkyGit,PurdueECE364/prelabs-siddmitra10,PurdueECE364/prelabs-SOGIST1,PurdueECE364/prelabs-wjorgebe,PurdueECE364/prelabs-dennynowak,PurdueECE364/prelabs-moffatw,PurdueECE364/prelabs-KevinMi2023p,PurdueECE364/prelabs-Ishaan-Jain,PurdueECE364/prelabs-aakashsiv,PurdueECE364/prelabs-AedanFrazier,PurdueECE364/prelabs-Eshaan0112,PurdueECE364/prelabs-PadNim14,PurdueECE364/prelabs-AaronFritz01",
    "INPUT_LOOP": """
    runs-on: ubuntu-latest
    steps:
      - run: "echo repo: ${{ github.repository }}"
"""
    })
def test_pylint():
    main()