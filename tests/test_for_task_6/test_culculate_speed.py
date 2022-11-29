import pandas as pd
import pytest

from task_6_racers_Barvynska.task_6 import culculate_speed


@pytest.mark.parametrize(
    "test_input_1, test_input_2, expected",
    [
        (
            pd.Series("1900-01-01 12:02:58.917"),
            pd.Series("1900-01-01 12:11:24.067"),
            ["1:04.415"],
        ),
        (
            pd.Series("1900-01-01 12:14:12.054"),
            pd.Series("1900-01-01 12:04:03.332"),
            ["57:12.013"],
        ),
    ],
)
def culculate_speed(test_input_1, test_input_2, expected):
    assert culculate_speed(test_input_1, test_input_2) == expected
