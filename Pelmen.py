#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from os import read
import re
import math

def import_file_csv():
    Arr = []
    with open("../data.csv", "r") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            Arr.append(row[0])

    return Arr


arr = import_file_csv()

def import_file_csv_name_arr():
    Arr = []
    with open("../data.csv", "r") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            Arr.append(row[1])

    return Arr


name_arr = import_file_csv_name_arr()