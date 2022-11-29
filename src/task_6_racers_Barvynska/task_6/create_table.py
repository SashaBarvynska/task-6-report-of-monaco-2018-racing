from pandas import DataFrame

from .culculate_speed import culculate_speed

'''create table from list with data'''
def create_table(
    start_abbreviation: list,
    start_time: list,
    end_abbreviation: list,
    end_time: list,
    abbreviation: list,
    racer: list,
    car: list,
) -> DataFrame:

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
    df_merged: DataFrame = table_start_time.merge(
        table_end_time, on="abbreviation"
    ).merge(table_abbreviation, on="abbreviation")

    df_merged["speed"] = culculate_speed(df_merged["start_time"], df_merged["end_time"])
    return df_merged
