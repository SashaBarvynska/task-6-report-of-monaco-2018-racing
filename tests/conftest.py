import random
from datetime import datetime, timedelta

from src.task_Barvynska.drivers import Driver

from .constants import ABBR, CARS, DRIVER_NAMES


def generate_random_driver(speed=None) -> Driver:
    driver = random.choice(DRIVER_NAMES)
    DRIVER_NAMES.remove(driver)
    car = random.choice(CARS)
    abbr = random.choice(ABBR)
    ABBR.remove(abbr)
    now = datetime.now()
    time_now = str(now)[11:-3]
    end_time = now + timedelta(seconds=random.randint(0, 120))
    time_end = str(end_time)[11:-3]
    d = Driver(abbr, driver, car, time_now, time_end)
    if speed:
        d.speed = speed
    else:
        d.set_speed()
    return d


def convert_driver_to_file_row(drivers: list[Driver], file: str) -> str:
    if file == "abb":
        return "\n".join(
            [
                f"{driver.abbreviation}_{driver.driver}_{driver.car}"
                for driver in drivers
            ]
        )
    if file == "start":
        return "\n".join(
            [
                f"{driver.abbreviation}2018-05-24_{driver.start_time}"
                for driver in drivers
            ]
        )
    if file == "end":
        return "\n".join(
            [f"{driver.abbreviation}2018-05-24_{driver.end_time}" for driver in drivers]
        )
    return ""


def convert_driver_to_file_dict(drivers: list[Driver], file: str) -> dict:
    drivers_dict = {}
    for driver in drivers:
        if file == "abb":
            drivers_dict.update(
                {driver.abbreviation: {"driver": driver.driver, "car": driver.car}}
            )
        if file == "start":
            drivers_dict.update({driver.abbreviation: driver.start_time})
        if file == "end":
            drivers_dict.update({driver.abbreviation: driver.end_time})
    return drivers_dict
