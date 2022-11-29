from task_6_racers_Barvynska.task_6 import format_file_abbreviation_data
from tests.CONSTANT import FILE_ABBREVIATIONS


def test_format_file_abbreviation_data():
    with open(
        FILE_ABBREVIATIONS,
        "r",
    ) as abbreviations:
        assert format_file_abbreviation_data(abbreviations) == (
            ["DRR", "SVF"],
            ["Daniel Ricciardo", "Sebastian Vettel"],
            ["RED BULL RACING TAG HEUER\n", "FERRARI\n"],
        )
