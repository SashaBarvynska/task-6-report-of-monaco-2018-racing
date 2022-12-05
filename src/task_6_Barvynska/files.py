import os
from datetime import datetime

from .format_file import FormatFile


class Files:
    def open_files(
        file_start: str, file_end: str, file_abbreviation: str
    ) -> tuple[
        list[str],
        list[datetime],
        list[str],
        list[datetime],
        list[str],
        list[str],
        list[str],
    ]:

        with open(file_start, "r") as reader_start, open(
            file_end, "r"
        ) as reader_end, open(file_abbreviation, "r") as reader_abbreviations:

            start_abbreviation, start_time = FormatFile.format_file_time(reader_start)
            end_abbreviation, end_time = FormatFile.format_file_time(reader_end)
            abbreviation, racer, car = FormatFile.format_file_abbreviation_data(
                reader_abbreviations
            )
        return (
            start_abbreviation,
            start_time,
            end_abbreviation,
            end_time,
            abbreviation,
            racer,
            car,
        )

    def find_files(path_to_folder: str) -> list[str, str, str]:
        files_name = ["start.log", "end.log", "abbreviations.txt"]
        pathes = []
        [
            [pathes.append(os.path.join(root, i)) for i in files_name if i in files]
            for root, _, files in os.walk(path_to_folder)
        ]
        files_in_folders = list(map(lambda x: x.split("\\")[-1], pathes))
        missing_files = list(filter(lambda x: x not in files_in_folders, files_name))

        if missing_files:
            raise FileNotFoundError(f"Following files are missing: {missing_files}")
        return pathes
