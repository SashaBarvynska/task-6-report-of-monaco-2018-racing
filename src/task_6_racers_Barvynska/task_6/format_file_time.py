from datetime import datetime
from io import TextIOWrapper

'''converting to the correct format a list with strings and data from a file'''
def format_file_time(line_of_file: TextIOWrapper) -> tuple[list, list]:
    racer_abbreviation, racer_time = [], []
    for line in line_of_file.read().split():
        racer_abbreviation.append(line[0:3])
        racer_time.append(datetime.strptime(line[14:], "%H:%M:%S.%f"))
    return racer_abbreviation, racer_time
