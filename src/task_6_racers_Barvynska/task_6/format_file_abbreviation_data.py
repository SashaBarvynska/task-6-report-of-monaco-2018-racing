from io import TextIOWrapper

'''converting to the correct format a list with strings from a file'''
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
