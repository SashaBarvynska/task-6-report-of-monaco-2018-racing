import pytest

from task_6_racers_Barvynska.task_6 import convert_time


@pytest.mark.parametrize(
    "test_input, expected", [(64.415, "1:04.415"), (-167.987, "57:12.013")]
)
def test_convert_time(test_input, expected):
    assert convert_time(test_input) == expected
