from task_6_racers_Barvynska.task_6 import open_files
from tests.CONSTANT import EXPECTED, NAMES_FILES


def test_open_files():
    assert open_files(NAMES_FILES[0], NAMES_FILES[1], NAMES_FILES[2]) == EXPECTED
