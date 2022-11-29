import os
from argparse import Namespace

'''find files in a pointed folder'''
def find_files(args: Namespace) -> list:
    files_name = ["start.log", "end.log", "abbreviations.txt"]
    pathes = []

    for root, dir, files in os.walk(args):
        for i in files_name:
            if i in files:
                pathes.append(os.path.join(root, i))
    if not pathes:
        raise FileNotFoundError(f"Files '{args}' do not exist!")
    return pathes
