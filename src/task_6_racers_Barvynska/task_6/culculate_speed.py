from pandas import Series, Timedelta

from .convert_time import convert_time

'''calculates the difference between 2 dates with time'''
def culculate_speed(start_time: Series, end_time: Series) -> list[str]:
    return list(
        map(
            lambda x: convert_time(Timedelta(x).total_seconds()),
            (end_time - start_time).tolist(),
        )
    )
