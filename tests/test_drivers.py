import datetime

import pytest

from src.task_6_Barvynska import Driver, DriversTemp

test_driver = Driver('DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER', '12:11:24.067', '12:14:12.054')


def test_get_time_difference():
    assert test_driver.get_time_difference() == datetime.timedelta(seconds=167, microseconds=987000)


def test_convert_time():
    assert test_driver.convert_time(64.415) == '1:04.415'


def test_set_speed():
    test_driver.set_speed()
    assert test_driver.speed == '2:47.987'


@pytest.mark.parametrize(
    "test_input_1, test_input_2, test_input_3, expected",
    [
        ({'DRR': {'driver': 'Daniel Ricciardo', 'car': 'RED BULL RACING TAG HEUER'}},  {'DRR': '12:14:12.054'}, {'DRR': '12:11:24.067'}, [Driver('DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER', '12:14:12.054', '12:11:24.067', '57:12.013')]),
        ({'SVF': {'driver': 'Sebastian Vettel', 'car': 'FERRARI'}, 'LHM': {'driver': 'Lewis Hamilton', 'car': 'MERCEDES'}},  {'SVF': '12:02:58.917', 'LHM': '12:18:20.125'}, {'SVF': '12:04:03.332', 'LHM': '12:11:32.585'}, [Driver('SVF', 'Sebastian Vettel', 'FERRARI', '12:02:58.917', '12:04:03.332', '1:04.415'), Driver('LHM', 'Lewis Hamilton', 'MERCEDES', '12:18:20.125', '12:11:32.585', '53:12.460')])
    ],
)
def test_build_report(test_input_1, test_input_2, test_input_3, expected):
    assert DriversTemp.build_report(test_input_1, test_input_2, test_input_3) == expected


@pytest.mark.parametrize(
    "test_input_1, test_input_2, expected",
    [
        ([Driver('SVF', 'Sebastian Vettel', 'FERRARI', '12:02:58.917', '12:04:03.332', '1:04.415'), Driver('DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER', '12:14:12.054', '12:11:24.067', '57:12.013')], True, [Driver('DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER', '12:14:12.054', '12:11:24.067', '57:12.013'), Driver('SVF', 'Sebastian Vettel', 'FERRARI', '12:02:58.917', '12:04:03.332', '1:04.415')]),
        ([Driver('SVF', 'Sebastian Vettel', 'FERRARI', '12:02:58.917', '12:04:03.332', '1:04.415'), Driver('DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER', '12:14:12.054', '12:11:24.067', '57:12.013')], False, [Driver('SVF', 'Sebastian Vettel', 'FERRARI', '12:02:58.917', '12:04:03.332', '1:04.415'), Driver('DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER', '12:14:12.054', '12:11:24.067', '57:12.013')]),
    ],
)
def test_sort_data(test_input_1, test_input_2, expected):
    assert DriversTemp.sort_data(test_input_1, test_input_2) == expected


@pytest.mark.parametrize(
    "test_input_1, test_input_2, expected",
    [
        ([Driver('DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER', '12:14:12.054', '12:11:24.067', '57:12.013'), Driver('SVF', 'Sebastian Vettel', 'FERRARI', '12:02:58.917', '12:04:03.332', '1:04.415')], "Sebastian Vettel", [Driver('SVF', 'Sebastian Vettel', 'FERRARI', '12:02:58.917', '12:04:03.332', '1:04.415')]),
        ([Driver('MES', 'Marcus Ericsson', 'SAUBER FERRARI', '12:04:45.513', '12:05:58.778', '1:13.265'), Driver('LSW', 'Lance Stroll', 'WILLIAMS MERCEDES', '12:06:13.511', '12:07:26.834', '1:13.323'), Driver('KMH', 'Kevin Magnussen', 'HAAS FERRARI', '12:02:51.003', '12:04:04.396', '1:13.393')], "Lance Stroll", [Driver('LSW', 'Lance Stroll', 'WILLIAMS MERCEDES', '12:06:13.511', '12:07:26.834', '1:13.323')])
    ],
)
def test_info_driver(test_input_1, test_input_2, expected):
    assert DriversTemp.info_driver(test_input_1, test_input_2) == expected
