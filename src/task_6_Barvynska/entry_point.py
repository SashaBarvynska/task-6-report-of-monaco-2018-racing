from argparse import ArgumentParser, Namespace

from .drivers import DriversTemp
from .files import Files
from .format_file import FormatFileTemp


def init_args() -> Namespace:
    parser = ArgumentParser(description="Add driver")
    parser.add_argument("--files", required=True)
    parser.add_argument("--asc", action="store_false")
    parser.add_argument("--desc", action="store_true")
    parser.add_argument("--driver")
    args = parser.parse_args()
    return args


def main() -> None:
    args = init_args()
    if not args.files:
        raise Exception("Required argument not specified '--files'")
    file_start, file_end, abbreviations_file = Files.find_files(args.files)
    list_drivers = DriversTemp.build_report(
        FormatFileTemp.format_file_abbreviation_data(
            Files.open_files(abbreviations_file)
        ),
        FormatFileTemp.format_file_time(Files.open_files(file_start)),
        FormatFileTemp.format_file_time(Files.open_files(file_end)),
    )
    if args.driver:
        DriversTemp.print_report(DriversTemp.info_driver(list_drivers, args.driver))
    else:
        order = bool(args.desc)
        DriversTemp.print_report(DriversTemp.sort_data(list_drivers, order))
