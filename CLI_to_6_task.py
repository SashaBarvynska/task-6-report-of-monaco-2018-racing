from argparse import ArgumentParser, Namespace

from task_6 import build_report, print_report


def init_args() -> Namespace:
    parser = ArgumentParser(description="Add driver")
    parser.add_argument("--driver")
    parser.add_argument("--asc", action="store_true")
    parser.add_argument("--desc", action="store_false")
    args = parser.parse_args()
    return args


def main():
    args = init_args()
    return print_report(
        build_report(
            "task_6/start.log",
            "task_6/end.log",
            "task_6/abbreviations.txt",
            args.desc,
            args.driver,
        )
    )
