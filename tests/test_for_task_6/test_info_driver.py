import datetime

import pandas as pd
from tabulate import tabulate

from task_6_racers_Barvynska.task_6 import info_driver
from tests.CONSTANT import DATA


def test_info_driver():

    expected_for_driver_one = pd.DataFrame(
        {
            "abbreviation": ["DRR"],
            "start_time": [
                datetime.datetime(1900, 1, 1, 12, 14, 12, 54000),
            ],
            "end_time": [
                datetime.datetime(1900, 1, 1, 12, 11, 24, 67000),
            ],
            "racer": ["Daniel Ricciardo"],
            "car": ["RED BULL RACING TAG HEUER\n"],
            "speed": ["57:12.013"],
            "place": [2],
            "place_racer": ["2.Daniel Ricciardo"],
        }
    )
    expected_for_driver_one_tabulate = tabulate(
        expected_for_driver_one,
        stralign="left",
        showindex=False,
        headers=expected_for_driver_one,
    )

    assert info_driver(DATA, "Daniel") == expected_for_driver_one_tabulate
