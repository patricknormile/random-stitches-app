import os
import sys
from pathlib import Path
import random
import pytest

this_folder = Path(__file__).parent
root_folder = this_folder.parent

src_path = os.path.join(str(root_folder), "src")
sys.path.append(src_path)

from create_random_stitches import random_stitch

def test_random_stitch():
    random.seed(0)
    assert random_stitch() == "back"
    for i in range(5) :
        assert random_stitch() in ["back","front"]