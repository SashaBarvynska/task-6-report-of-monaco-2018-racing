from argparse import ArgumentParser, Namespace

from src.task_6_Barvynska.drivers import Drivers
from src.task_6_Barvynska.files import Files


def init_args() -> Namespace:
    parser = ArgumentParser(description="Add driver")
    parser.add_argument("--files")
    parser.add_argument("--asc", action="store_false")
    parser.add_argument("--desc", action="store_true")
    parser.add_argument("--driver")
    args = parser.parse_args()
    return args


def main() -> None:
    args = init_args()
    if not args.files:
        raise Exception("Required argument not specified '--files'")
    files = Files.find_files(args.files)
    table = Drivers.build_report(*Files.open_files(*files))
    sorted_table = Drivers.sort_data(table, args.desc)
    Drivers.print_report(
        Drivers.info_driver(sorted_table, args.driver)
        if args.driver
        else Drivers.print_report(sorted_table)
    )
