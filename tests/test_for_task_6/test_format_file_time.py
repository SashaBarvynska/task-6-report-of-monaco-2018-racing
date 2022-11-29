import datetime

from task_6_racers_Barvynska.task_6 import format_file_time
from tests.CONSTANT import FILE_END, FILE_START


def test_format_file_time():
    with open(FILE_START, "r",) as start, open(
        FILE_END,
        "r",
    ) as end:

        assert format_file_time(start) == (
            ["SVF", "DRR"],
            [
                datetime.datetime(1900, 1, 1, 12, 2, 58, 917000),
                datetime.datetime(1900, 1, 1, 12, 14, 12, 54000),
            ],
        )
        assert format_file_time(end) == (
            ["DRR", "SVF"],
            [
                datetime.datetime(1900, 1, 1, 12, 11, 24, 67000),
                datetime.datetime(1900, 1, 1, 12, 4, 3, 332000),
            ],
        )
