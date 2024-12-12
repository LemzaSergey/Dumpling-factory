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

dailyOutputFinishedProducts = float(arr[0])  # суточная выработка готовой продукции Qсут
t = float(arr[1])  # продолжительность рабочей смены

# I. Технологическая линия изготовления пельменей
dumplingMachineProductivity = float(
    arr[2]
)  # производительность пельменного автомата рпа

# II. Технологическая линия подготовки теста.
massFractionDough = float(arr[3])  # массовая доля теста в готовой продукции   ат %
kneadingMachinePerformance = float(
    arr[4]
)  # производительность тестомесильной машины   ртм

# III. Технологическая линия подготовки фарша.
cutterPerformance = float(arr[5])  # производительность куттера рк
massFractionMeat = float(arr[6])  # массовая доля мяса в готовой продукции   ам  %
massFractionEggs = float(arr[7])  # массовая доля яиц в готовой продукции   ая %
massFractionSalt = float(arr[8])  # массовая доля соли в готовой продукции   ас %
massFractionSpices = float(arr[9])  # массовая доля специй в готовой продукции   асп %

def print_name_arr(arr, name_arr):
    n = len(arr)
    for index in range(n):
        print(arr[index] + "  " + name_arr[index])
    return 1


print_name_arr(arr, name_arr)