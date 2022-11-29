from pandas import DataFrame

"""build a report on occupied space"""
def right_order_in_table(table: DataFrame, order: str) -> DataFrame:
    table_sorted: DataFrame = table.sort_values(
        by="speed", ascending=order, na_position="first"
    )

    table_sorted["place"] = list(range(1, (len(table_sorted["speed"])) + 1))
    table_sorted["place_racer"] = (
        table_sorted["place"].astype(str) + "." + table_sorted["racer"]
    )
    return table_sorted
