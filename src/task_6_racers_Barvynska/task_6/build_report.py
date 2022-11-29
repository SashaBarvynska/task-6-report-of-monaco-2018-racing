from pandas import DataFrame
from tabulate import tabulate

'''build report for top 15 in table in a certain order: ascending or descending'''
def build_report(table_sorted: DataFrame) -> str:
    df_merged_colums = table_sorted[
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
        df_merged_colums.tail(len(table_sorted["speed"]) - 15),
        showindex=False,
        stralign="left",
        tablefmt="presto",
    )
    return (
        tabulate_df_merged_first_15
        + "\n______________________________________________________________\n"
        + tabulate_df_merged_last
    )
