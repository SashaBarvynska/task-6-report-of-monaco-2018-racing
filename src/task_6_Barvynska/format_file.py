import math
from datetime import datetime
from io import TextIOWrapper

from pandas import Timedelta


class FormatFile:
    def format_file_abbreviation_data(
        line_of_file: TextIOWrapper,
    ) -> tuple[list[str], list[str], list[str]]:
        racer_abbreviation, name_player, name_car, = (
            [],
            [],
            [],
        )

        for line in line_of_file.readlines():
            list = line.split("_")
            racer_abbreviation.append(list[0])
            name_player.append(list[1])
            name_car.append(list[2])

        return (
            racer_abbreviation,
            name_player,
            name_car,
        )

    def format_file_time(
        line_of_file: TextIOWrapper,
    ) -> tuple[list[str], list[datetime]]:
        racer_abbreviation, racer_time = [], []
        for line in line_of_file.read().split():
            racer_abbreviation.append(line[0:3])
            racer_time.append(datetime.strptime(line[14:], "%H:%M:%S.%f"))
        return racer_abbreviation, racer_time

    def calculate_speed(speed: datetime) -> str:
        return FormatFile.convert_time(Timedelta(speed).total_seconds())

    def convert_time(seconds: float) -> str:
        minutes = math.floor((seconds % 3600) / 60)
        seconds = seconds % 60
        return f"{minutes}:{seconds:06.3f}"
