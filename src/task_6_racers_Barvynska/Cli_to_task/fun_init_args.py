from argparse import ArgumentParser, Namespace

'''create agrumets for CLI'''
def init_args() -> Namespace:
    parser = ArgumentParser(description="Add driver")
    parser.add_argument("--files")
    parser.add_argument("--asc", action="store_true")
    parser.add_argument("--desc", action="store_false")
    parser.add_argument("--driver")
    args = parser.parse_args()
    return args
