#!~/usr/bin/env python

import pandas as pd
import numpy as np

def main():
    data = pd.read_csv('data/nfl-play-by-play-2009-2016-v3.csv')
    columns = data.columns
    print(columns[0:5])

if __name__=='__main__':
    main()
