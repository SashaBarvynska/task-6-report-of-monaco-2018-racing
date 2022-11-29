import math

'''get the correct time from the number of minutes'''
def convert_time(seconds: float) -> str:
    minutes = math.floor((seconds % 3600) / 60)
    seconds = seconds % 60
    return f"{minutes}:{seconds:06.3f}"
