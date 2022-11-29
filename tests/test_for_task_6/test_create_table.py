from pandas.testing import assert_frame_equal

from task_6_racers_Barvynska.task_6 import create_table
from tests.CONSTANT import EXPECTED, EXPECTEDT_DF


def test_create_table():
    assert_frame_equal(create_table(*EXPECTED), EXPECTEDT_DF)
