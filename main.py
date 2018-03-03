#!~/usr/bin/env python

import pandas as pd

def export_columns(data_path, target_file):
    """ Loads into pandas and all column names to file """
    data = pd.read_csv(data_path)
    columns = data.columns
    contents = ''
    for c in columns:
        contents += str(c) + '\n'

    with open(target_file, 'w') as f:
        f.write(contents)


def main():
    data_file = 'data/nfl-play-by-play-2009-2016-v3.csv'
    target_file = 'data/columns.txt'
    export_columns(data_file, target_file)


if __name__ == '__main__':
    main()
