from pandas import DataFrame
from tabulate import tabulate

'''create a table with info about a specific driver'''
def info_driver(table_sorted: DataFrame, driver: str) -> str:
    return tabulate(
        table_sorted[table_sorted["racer"].str.contains(driver)],
        stralign="left",
        showindex=False,
        headers=table_sorted,
    )
