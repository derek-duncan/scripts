import glob
import os
import sys
import csv

def namething():
    files = glob.glob(os.path.join(os.path.dirname(__file__), '*.txt'))
    file_len = len(files)
    files = [os.path.basename(f) for f in files]

    lol = [[1,2,3],[4,5,6],[7,8,9]]
    item_length = len(lol[0])
    print (files)

    with open(os.path.join(os.path.dirname(__file__), 'test.csv'), "w") as ex_file:
        file_writer = csv.writer(ex_file)
        file_writer.writerow(files)
namething()