import datetime

import pandas as pd
from tabulate import tabulate

PARH_TO_FOLDER_WITH_FILES = (
    "D:\\Sasha\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\data"
)
NAMES_FILES = [
    "D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\data\\start.log",
    "D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\data\\end.log",
    "D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\data\\abbreviations.txt",
]
FILE_START = "D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\data\\start.log"
FILE_END = "D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\data\\end.log"
FILE_ABBREVIATIONS = "D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\data\\abbreviations.txt"
DATA_OF_TABLE = [
    ["MES", "RGH"],
    [
        "datetime.datetime(1900, 1, 1, 12, 5, 58, 778000)",
        "datetime.datetime(1900, 1, 1, 12, 6, 27, 441000)",
    ],
    ["MCLAREN RENAULT\n", "WILLIAMS MERCEDES\n"],
]
DATA = pd.DataFrame(
    {
        "abbreviation": ["SVF", "DRR"],
        "start_time": [
            datetime.datetime(1900, 1, 1, 12, 2, 58, 917000),
            datetime.datetime(1900, 1, 1, 12, 14, 12, 54000),
        ],
        "end_time": [
            datetime.datetime(1900, 1, 1, 12, 4, 3, 332000),
            datetime.datetime(1900, 1, 1, 12, 11, 24, 67000),
        ],
        "racer": ["Sebastian Vettel", "Daniel Ricciardo"],
        "car": ["FERRARI\n", "RED BULL RACING TAG HEUER\n"],
        "speed": ["1:04.415", "57:12.013"],
        "place": [1, 2],
        "place_racer": ["1.Sebastian Vettel", "2.Daniel Ricciardo"],
    }
)
DATA_IN_ORDER_ASC = pd.DataFrame(
    {
        "abbreviation": ["SVF", "DRR"],
        "start_time": [
            datetime.datetime(1900, 1, 1, 12, 2, 58, 917000),
            datetime.datetime(1900, 1, 1, 12, 14, 12, 54000),
        ],
        "end_time": [
            datetime.datetime(1900, 1, 1, 12, 4, 3, 332000),
            datetime.datetime(1900, 1, 1, 12, 11, 24, 67000),
        ],
        "racer": ["Sebastian Vettel", "Daniel Ricciardo"],
        "car": ["FERRARI\n", "RED BULL RACING TAG HEUER\n"],
        "speed": ["1:04.415", "57:12.013"],
        "place": [1, 2],
        "place_racer": ["1.Sebastian Vettel", "2.Daniel Ricciardo"],
    }
)
DATA_IN_ORDER_DESC = pd.DataFrame(
    {
        "abbreviation": ["DRR", "SVF"],
        "start_time": [
            datetime.datetime(1900, 1, 1, 12, 14, 12, 54000),
            datetime.datetime(1900, 1, 1, 12, 2, 58, 917000),
        ],
        "end_time": [
            datetime.datetime(1900, 1, 1, 12, 11, 24, 67000),
            datetime.datetime(1900, 1, 1, 12, 4, 3, 332000),
        ],
        "racer": ["Daniel Ricciardo", "Sebastian Vettel"],
        "car": ["RED BULL RACING TAG HEUER\n", "FERRARI\n"],
        "speed": ["57:12.013", "1:04.415"],
        "place": [2, 1],
        "place_racer": ["2.Daniel Ricciardo", "1.Sebastian Vettel"],
    }
)
PARH_TO_FOLDER_WITH_FILES_TOP_15 = (
    "D:\\Sasha\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\data_top_15"
)
NAMES_FILES_TOP_15 = [
    "D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\data_top_15\\start.log",
    "D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\data_top_15\\end.log",
    "D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\data_top_15\\abbreviations.txt",
]
FILE_START_TOP_15 = "D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\data_top_15\\start.log"
FILE_END_TOP_15 = "D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\data_top_15\\end.log"
FILE_ABBREVIATIONS_TOP_15 = "D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\data_top_15\\abbreviations.txt"
TABLES_IN_ORDER_ASC = pd.DataFrame(
    {
        "place_racer": [
            "1.Sebastian Vettel",
            "2.Valtteri Bottas",
            "3.Stoffel Vandoorne",
            "4.Kimi RГ¤ikkГ¶nen",
            "5.Fernando Alonso",
            "6.Charles Leclerc",
            "7.Sergio Perez",
            "8.Romain Grosjean",
            "9.Pierre Gasly",
            "10.Carlos Sainz",
            "11.Nico Hulkenberg",
            "12.Brendon Hartley",
            "13.Marcus Ericsson",
            "14.Lance Stroll",
            "15.Kevin Magnussen",
            "16.Lewis Hamilton",
            "17.Esteban Ocon",
            "18.Sergey Sirotkin",
            "19.Daniel Ricciardo",
        ],
        "car": [
            "FERRARI\n",
            "MERCEDES\n",
            "MCLAREN RENAULT\n",
            "FERRARI\n",
            "MCLAREN RENAULT\n",
            "SAUBER FERRARI\n",
            "FORCE INDIA MERCEDES\n",
            "HAAS FERRARI\n",
            "SCUDERIA TORO ROSSO HONDA\n",
            "RENAULT\n",
            "RENAULT\n",
            "SCUDERIA TORO ROSSO HONDA\n",
            "SAUBER FERRARI\n",
            "WILLIAMS MERCEDES\n",
            "HAAS FERRARI\n",
            "MERCEDES\n",
            "FORCE INDIA MERCEDES\n",
            "WILLIAMS MERCEDES\n",
            "RED BULL RACING TAG HEUER\n",
        ],
        "speed": [
            "1:04.415",
            "1:12.434",
            "1:12.463",
            "1:12.639",
            "1:12.657",
            "1:12.829",
            "1:12.848",
            "1:12.930",
            "1:12.941",
            "1:12.950",
            "1:13.065",
            "1:13.179",
            "1:13.265",
            "1:13.323",
            "1:13.393",
            "53:12.460",
            "54:13.028",
            "55:12.706",
            "57:12.013",
        ],
    }
)
TABLES_IN_ORDER_DESC = pd.DataFrame(
    {
        "place_racer": [
            "1.Daniel Ricciardo",
            "2.Sergey Sirotkin",
            "3.Esteban Ocon",
            "4.Lewis Hamilton",
            "5.Kevin Magnussen",
            "6.Lance Stroll",
            "7.Marcus Ericsson",
            "8.Brendon Hartley",
            "9.Nico Hulkenberg",
            "10.Carlos Sainz",
            "11.Pierre Gasly",
            "12.Romain Grosjean",
            "13.Sergio Perez",
            "14`.Charles Leclerc",
            "15.Fernando Alonso",
            "16.Kimi RГ¤ikkГ¶nen",
            "17.Stoffel Vandoorne",
            "18.Valtteri Bottas",
            "19.Sebastian Vettel",
        ],
        "car": [
            "RED BULL RACING TAG HEUER\n",
            "WILLIAMS MERCEDES\n",
            "FORCE INDIA MERCEDES\n",
            "MERCEDES\n",
            "HAAS FERRARI\n",
            "WILLIAMS MERCEDES\n",
            "SAUBER FERRARI\n",
            "SCUDERIA TORO ROSSO HONDA\n",
            "RENAULT\n",
            "RENAULT\n",
            "SCUDERIA TORO ROSSO HONDA\n",
            "HAAS FERRARI\n",
            "FORCE INDIA MERCEDES\n",
            "SAUBER FERRARI\n",
            "MCLAREN RENAULT\n",
            "FERRARI\n",
            "MCLAREN RENAULT\n",
            "MERCEDES\n",
            "FERRARI\n",
        ],
        "speed": [
            "57:12.013",
            "55:12.706",
            "54:13.028",
            "53:12.460",
            "1:13.393",
            "1:13.323",
            "1:13.265",
            "1:13.179",
            "1:13.065",
            "1:12.950",
            "1:12.941",
            "1:12.930",
            "1:12.848",
            "1:12.829",
            "1:12.657",
            "1:12.639",
            "1:12.463",
            "1:12.434",
            "1:04.415",
        ],
    }
)
tabulate_df_merged_first_15_asc = tabulate(
    TABLES_IN_ORDER_ASC.head(15),
    headers=TABLES_IN_ORDER_ASC,
    showindex=False,
    stralign="left",
    tablefmt="presto",
)
tabulate_df_merged_last_asc = tabulate(
    TABLES_IN_ORDER_ASC.tail(len(TABLES_IN_ORDER_ASC["speed"]) - 15),
    showindex=False,
    stralign="left",
    tablefmt="presto",
)
RESULT_ASC = (
    tabulate_df_merged_first_15_asc
    + "\n______________________________________________________________\n"
    + tabulate_df_merged_last_asc
)

tabulate_df_merged_first_15_desc = tabulate(
    TABLES_IN_ORDER_DESC.head(15),
    headers=TABLES_IN_ORDER_DESC,
    showindex=False,
    stralign="left",
    tablefmt="presto",
)
tabulate_df_merged_last_desc = tabulate(
    TABLES_IN_ORDER_DESC.tail(len(TABLES_IN_ORDER_DESC["speed"]) - 15),
    showindex=False,
    stralign="left",
    tablefmt="presto",
)
RESULT_DESC = (
    tabulate_df_merged_first_15_desc
    + "\n______________________________________________________________\n"
    + tabulate_df_merged_last_desc
)

EXPECTED = (
    ["SVF", "DRR"],
    [
        datetime.datetime(1900, 1, 1, 12, 2, 58, 917000),
        datetime.datetime(1900, 1, 1, 12, 14, 12, 54000),
    ],
    ["DRR", "SVF"],
    [
        datetime.datetime(1900, 1, 1, 12, 11, 24, 67000),
        datetime.datetime(1900, 1, 1, 12, 4, 3, 332000),
    ],
    ["DRR", "SVF"],
    ["Daniel Ricciardo", "Sebastian Vettel"],
    ["RED BULL RACING TAG HEUER\n", "FERRARI\n"],
)
EXPECTEDT_DF = pd.DataFrame(
    {
        "abbreviation": ["SVF", "DRR"],
        "start_time": [
            datetime.datetime(1900, 1, 1, 12, 2, 58, 917000),
            datetime.datetime(1900, 1, 1, 12, 14, 12, 54000),
        ],
        "end_time": [
            datetime.datetime(1900, 1, 1, 12, 4, 3, 332000),
            datetime.datetime(1900, 1, 1, 12, 11, 24, 67000),
        ],
        "racer": ["Sebastian Vettel", "Daniel Ricciardo"],
        "car": ["FERRARI\n", "RED BULL RACING TAG HEUER\n"],
        "speed": ["1:04.415", "57:12.013"],
    }
)
