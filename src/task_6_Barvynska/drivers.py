import math
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from pandas import Timedelta


@dataclass()
class Driver:
    abbreviation: str
    driver: str
    car: str
    start_time: str
    end_time: str
    speed: str = Optional[str]

    def get_time_difference(self) -> datetime:
        end = datetime.strptime(self.end_time, "%H:%M:%S.%f")
        start = datetime.strptime(self.start_time, "%H:%M:%S.%f")
        return end - start

    def set_speed(self) -> None:
        diff = self.get_time_difference()
        sec = Timedelta(diff).total_seconds()
        self.speed = self.convert_time(sec)

    def convert_time(self, seconds) -> str:
        minutes = math.floor((seconds % 3600) / 60)
        seconds = seconds % 60
        return f"{minutes}:{seconds:06.3f}"

    def __repr__(self):
        return str(
            (
                self.abbreviation,
                self.driver,
                self.car,
                self.start_time,
                self.end_time,
                self.speed,
            )
        )


class DriversTemp:

    @classmethod
    def build_report(
        cls,
        content_abbreviations_file: dict[str: dict[str: str]],
        content_file_start: dict[str: dict[str: datetime]],
        content_file_end: dict[str: dict[str: datetime]],
    ) -> list[str]:
        drivers = []
        for abr, value in content_abbreviations_file.items():
            driver_object = Driver(
                abbreviation=abr,
                driver=value["driver"],
                car=value["car"],
                start_time=content_file_start[abr],
                end_time=content_file_end[abr],
            )
            driver_object.set_speed()
            drivers.append(driver_object)
        return drivers

    @staticmethod
    def sort_data(drivers: list[str], order: str) -> list[str]:
        return sorted(drivers, key=lambda x: x.speed, reverse=order)

    @staticmethod
    def info_driver(drivers: list[str], driver: str) -> list[str]:
        return [driver_object for driver_object in drivers if driver_object.driver == driver]

    @staticmethod
    def print_report(sorted_list: list[str]) -> None:
        for index, value in enumerate(sorted_list):
            print(f"{index + 1}.{value.driver}     |{value.car}     |{value.speed}")
            if index == 14:
                print(
                    "__________________________________________________________________________"
                )
