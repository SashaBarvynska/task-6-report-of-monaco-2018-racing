from argparse import Namespace
from unittest.mock import patch

import pytest

from src.task_Barvynska.drivers import Driver
from src.task_Barvynska.entry_point import main

from .constants import (
    DICT_ABB,
    DICT_TIME,
    FILE_ABB,
    FILE_END,
    LIST_DRIVERS,
    SORT_LIST_DRIVERS,
    TEST_FOLDER_PATH,
)


@patch(
    "src.task_Barvynska.entry_point.init_args",
    return_value=Namespace(files=None, asc=True, desc=False, driver=None),
)
def test_main_without_args(mock_init_args):
    with pytest.raises(Exception) as error:
        main()
    assert str(error.value) == "Required argument not specified '--files'"
    mock_init_args.assert_called_with()


@patch(
    "src.task_Barvynska.entry_point.init_args",
    return_value=Namespace(
        files=f"{TEST_FOLDER_PATH}\\open_all_file", asc=True, desc=False, driver=None
    ),
)
@patch(
    "src.task_Barvynska.files.Files.find_files",
    return_value=[
        f"{TEST_FOLDER_PATH}\\open_all_file\\start.log",
        f"{TEST_FOLDER_PATH}\\open_all_file\\end.log",
        f"{TEST_FOLDER_PATH}\\open_all_file\\abbreviations.txt",
    ],
)
@patch(
    "src.task_Barvynska.format_file.FormatFile.format_file_abbreviation_data",
    return_value=DICT_ABB,
)
@patch(
    "src.task_Barvynska.format_file.FormatFile.format_file_time",
    return_value=DICT_TIME,
)
@patch("src.task_Barvynska.drivers.Drivers.build_report", return_value=LIST_DRIVERS)
def test_main_with_file(
    mock_build_report,
    mock_format_file_time,
    mock_format_file_abbreviation_data,
    mock_find_files,
    mock_init_args,
):
    main()
    mock_build_report.assert_called_with(DICT_ABB, DICT_TIME, DICT_TIME)
    mock_format_file_time.assert_called_with(FILE_END)
    mock_format_file_abbreviation_data.assert_called_with(FILE_ABB)
    mock_find_files.assert_called_with(f"{TEST_FOLDER_PATH}\\open_all_file")
    mock_init_args.asssert_called_once()


@patch(
    "src.task_Barvynska.entry_point.init_args",
    return_value=Namespace(
        files=f"{TEST_FOLDER_PATH}\\open_all_file",
        asc=True,
        desc=False,
        driver="Daniel Ricciardo",
    ),
)
@patch(
    "src.task_Barvynska.drivers.Drivers.info_driver",
    return_value=[
        Driver(
            "DRR",
            "Daniel Ricciardo",
            "RED BULL RACING TAG HEUER",
            "12:14:12.054",
            "12:11:24.067",
            "57:12.013",
        )
    ],
)
def test_main_with_driver(mock_info_driver, mock_init_args):
    main()
    mock_info_driver.assert_called_with(LIST_DRIVERS, "Daniel Ricciardo")
    mock_init_args.asssert_called_once()


@patch(
    "src.task_Barvynska.entry_point.init_args",
    return_value=Namespace(
        files=f"{TEST_FOLDER_PATH}\\open_all_file", asc=True, desc=False, driver=None
    ),
)
@patch("src.task_Barvynska.drivers.Drivers.sort_data", return_value=SORT_LIST_DRIVERS)
def test_main_sort_data_asc(mock_sort_data, mock_init_args):
    main()
    mock_sort_data.assert_called_with(LIST_DRIVERS, False)
    mock_init_args.asssert_called_once()


@patch(
    "src.task_Barvynska.entry_point.init_args",
    return_value=Namespace(
        files=f"{TEST_FOLDER_PATH}\\open_all_file", asc=False, desc=True, driver=None
    ),
)
@patch("src.task_Barvynska.drivers.Drivers.sort_data", return_value=LIST_DRIVERS)
def test_main_sort_data_desc(mock_sort_data, mock_init_args):
    main()
    mock_sort_data.assert_called_with(LIST_DRIVERS, True)
    mock_init_args.asssert_called_once()
