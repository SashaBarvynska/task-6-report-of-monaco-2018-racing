import numpy as np

from .format_file import FormatFile


class Drivers:
    def build_report(
        start_abbreviation: list,
        start_time: list,
        end_abbreviation: list,
        end_time: list,
        abbreviation: list,
        racer: list,
        car: list,
    ) -> list[str, str, str]:

        table_1 = Drivers.__create_sorted_table(start_abbreviation, start_time)
        table_2 = Drivers.__create_sorted_table(end_abbreviation, end_time)
        table_3 = Drivers.__sort_by_key_in_dict(
            dict(zip(abbreviation, zip(racer, car)))
        )

        list_abbreviation, list_speed = [], []
        for key in table_1.keys() & table_2.keys():
            list_abbreviation.append(key)
            list_speed.append(
                FormatFile.calculate_speed(np.subtract(table_2[key], table_1[key]))
            )

        table_4 = Drivers.__create_sorted_table(list_abbreviation, list_speed)
        dict2_sorted: dict = {
            abbreviation: table_4[abbreviation] for abbreviation in table_3.keys()
        }
        sorted_dictionary = Drivers.__create_sorted_table(
            table_3.keys(),
            zip(table_3.values(), dict2_sorted.values()),
        )

        list_drivers = []
        for row in sorted_dictionary.values():
            full_list = []
            (driver, car), speed = row
            driver, car = (driver, car)
            full_list.append(driver), full_list.append(car), full_list.append(
                speed
            ), list_drivers.append(full_list)
        return list_drivers

    def __sort_by_key_in_dict(table: dict) -> dict:
        return {abbreviation: table[abbreviation] for abbreviation in sorted(table)}

    def __create_sorted_table(key: list, value: list) -> dict:
        table = dict(zip(key, value))
        return Drivers.__sort_by_key_in_dict(table)

    def sort_data(
        sort_drivers: list[str, str, str], order=False
    ) -> list[int, str, str, str]:
        sort_drivers, sort_drivers_plus_place = (
            sorted(sort_drivers, key=lambda x: x[-1], reverse=order),
            [],
        )
        for index, value in enumerate(sort_drivers):
            value.insert(0, index + 1)
            sort_drivers_plus_place.append(value)

        return sort_drivers_plus_place

    def info_driver(
        table_sorted: list[int, str, str, str], driver: str
    ) -> list[int, str, str, str]:
        return list(filter(lambda x: x[1] == driver, table_sorted))

    def print_report(list_order: list[int, str, str, str]) -> None:
        for index, value in enumerate(list_order or []):
            print(*value, sep=" |", end="\n")
            if index == 14:
                print("_____________________________________________________________")
