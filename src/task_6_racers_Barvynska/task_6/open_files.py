from .format_file_abbreviation_data import format_file_abbreviation_data
from .format_file_time import format_file_time

'''find files with certain names in the specified folder'''
def open_files(
    file_start: list, file_end: list, file_abbreviation: list
) -> tuple[list, list, list, list, list, list, list]:

    with open(file_start, "r") as reader_start, open(file_end, "r") as reader_end, open(
        file_abbreviation, "r"
    ) as reader_abbreviations:

        start_abbreviation, start_time = format_file_time(reader_start)
        end_abbreviation, end_time = format_file_time(reader_end)
        abbreviation, racer, car = format_file_abbreviation_data(reader_abbreviations)
    return (
        start_abbreviation,
        start_time,
        end_abbreviation,
        end_time,
        abbreviation,
        racer,
        car,
    )
