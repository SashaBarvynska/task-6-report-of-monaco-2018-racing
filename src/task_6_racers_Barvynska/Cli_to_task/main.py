import inspect

from task_6_racers_Barvynska.Cli_to_task import find_files, init_args
from task_6_racers_Barvynska.task_6 import (build_report, create_table,
                                            info_driver, open_files,
                                            print_report, right_order_in_table)

'''show built report'''
def main() -> None:
    print(inspect.getfile(init_args), "////////////////////////////////////////////")
    args = init_args()

    if not args.files:
        raise Exception("Required not specified argument '--files'")
    files = find_files(args.files)
    table = create_table(*open_files(*files))
    sorted_table = right_order_in_table(table, args.desc)
    print_report(
        info_driver(sorted_table, args.driver)
        if args.driver
        else build_report(sorted_table)
    )
