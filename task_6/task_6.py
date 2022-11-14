import math
from datetime import datetime
from io import TextIOWrapper

from pandas import DataFrame, Series, Timedelta
from tabulate import tabulate


def build_report(file_start, file_end, file_abbreviation, order, driver) -> str:
    with open(file_start, "r") as reader_start, open(file_end, "r") as reader_end, open(
        file_abbreviation, "r"
    ) as reader_abbreviations:
        start_abbreviation, start_time = format_file_time(reader_start)
        end_abbreviation, end_time = format_file_time(reader_end)
        abbreviation, racer, car = format_file_abbreviation_data(reader_abbreviations)

        table_start_time = DataFrame(
            {
                "abbreviation": start_abbreviation,
                "start_time": start_time,
            }
        )

        table_end_time = DataFrame(
            {
                "abbreviation": end_abbreviation,
                "end_time": end_time,
            }
        )

        table_abbreviation = DataFrame(
            {
                "abbreviation": abbreviation,
                "racer": racer,
                "car": car,
            }
        )

        df_merged = table_start_time.merge(table_end_time, on="abbreviation").merge(
            table_abbreviation, on="abbreviation"
        )

        df_merged["speed"] = culculate_speed(
            df_merged["start_time"], df_merged["end_time"]
        )

        df_sorted = df_merged.sort_values(
            by="speed", ascending=order, na_position="first"
        )

        df_sorted["place"] = list(range(1, (len(df_sorted["speed"])) + 1))
        df_sorted["place_racer"] = (
            df_sorted["place"].astype(str) + "." + df_sorted["racer"]
        )
        if driver:
            return tabulate(
                df_sorted[df_sorted["racer"].str.contains(driver)],
                stralign="left",
                showindex=False,
                headers=df_sorted,
            )

        df_merged_colums = df_sorted[
            [
                "place_racer",
                "car",
                "speed",
            ]
        ]

        tabulate_df_merged_first_15 = tabulate(
            df_merged_colums.head(15),
            headers=df_merged_colums,
            showindex=False,
            stralign="left",
            tablefmt="presto",
        )

        tabulate_df_merged_last = tabulate(
            df_merged_colums.tail(len(df_sorted["speed"]) - 15),
            showindex=False,
            stralign="left",
            tablefmt="presto",
        )

        return (
            tabulate_df_merged_first_15
            + "\n______________________________________________________________\n"
            + tabulate_df_merged_last
        )


def convert_time(seconds: float) -> str:
    minutes = math.floor((seconds % 3600) / 60)
    seconds = seconds % 60
    return f"{minutes}:{seconds:06.3f}"


def format_file_time(line_of_file: TextIOWrapper) -> tuple[list, list]:
    racer_abbreviation, racer_time = [], []
    for line in line_of_file.read().split():
        racer_abbreviation.append(line[0:3])
        racer_time.append(datetime.strptime(line[14:], "%H:%M:%S.%f"))
    return racer_abbreviation, racer_time


def format_file_abbreviation_data(
    line_of_file: TextIOWrapper,
) -> tuple[list, list, list]:

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


def culculate_speed(start_time: Series, end_time: Series) -> list[str]:
    return list(
        map(
            lambda x: convert_time(Timedelta(x).total_seconds()),
            (end_time - start_time).tolist(),
        )
    )


def print_report(report: str) -> None:
    print(report)
