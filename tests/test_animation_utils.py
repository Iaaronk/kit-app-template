import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "source"))
import animation_utils


def test_play_animation_signature():
    assert callable(animation_utils.play_animation)
    with pytest.raises(TypeError):
        animation_utils.play_animation()
