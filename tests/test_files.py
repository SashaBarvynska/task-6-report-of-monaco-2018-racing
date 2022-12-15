import pytest

from src.task_Barvynska import Files

from .constants import FILE_ABB, FILE_END, FILE_TIME, TEST_FOLDER_PATH


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (f"{TEST_FOLDER_PATH}\\open_all_file\\abbreviations.txt", FILE_ABB),
        (f"{TEST_FOLDER_PATH}\\open_all_file\\start.log", FILE_TIME),
        (f"{TEST_FOLDER_PATH}\\open_all_file\\end.log", FILE_END),
    ],
)
def test_open_files(test_input, expected):
    assert Files.open_files(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            f"{TEST_FOLDER_PATH}\\open_all_file",
            [
                f"{TEST_FOLDER_PATH}\\open_all_file\\start.log",
                f"{TEST_FOLDER_PATH}\\open_all_file\\end.log",
                f"{TEST_FOLDER_PATH}\\open_all_file\\abbreviations.txt",
            ],
        )
    ],
)
def test_find_all_files(test_input, expected):
    assert Files.find_files(test_input) == expected


@pytest.mark.parametrize(
    "test_input",
    [(f"{TEST_FOLDER_PATH}\\open_any_file")],
)
def test_find_any_files(test_input):
    with pytest.raises(Exception) as error:
        Files.find_files(test_input)
    assert str(error.value) == "Following files are missing: ['start.log']"
