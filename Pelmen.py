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

# I. Технологическая линия изготовления пельменей
def dumpling_machines(dailyOutputFinishedProducts, t, dumplingMachineProductivity):
    Ptlp = dailyOutputFinishedProducts / (2 * t)
    N = math.ceil(Ptlp / dumplingMachineProductivity)
    print(Ptlp / dumplingMachineProductivity)
    return N

# II. Технологическая линия подготовки теста.
def dough_kneading_machines(
    dailyOutputFinishedProducts, t, massFractionDough, kneadingMachinePerformance
):
    Ptlp = dailyOutputFinishedProducts / (2 * t)
    Ptlt = Ptlp * massFractionDough / 100
    N = math.ceil(Ptlt / kneadingMachinePerformance)
    print(Ptlt / kneadingMachinePerformance)
    return N

# III. Технологическая линия подготовки фарша.
def cutter_machines(
    dailyOutputFinishedProducts, t, massFractionDough, cutterPerformance
):
    Ptlp = dailyOutputFinishedProducts / (2 * t)
    Ptlf = ((100 - massFractionDough) * Ptlp) / 100
    N = math.ceil(Ptlf / cutterPerformance)
    print(Ptlf / cutterPerformance)
    return N


def checkingAllIngredientsPlace(
    massFractionDough,
    massFractionMeat,
    massFractionEggs,
    massFractionSalt,
    massFractionSpices,
):
    if (
        massFractionDough
        + massFractionMeat
        + massFractionEggs
        + massFractionSalt
        + massFractionSpices
        == 100
    ):
        return True
    else:
        return False

if checkingAllIngredientsPlace(
    massFractionDough,
    massFractionMeat,
    massFractionEggs,
    massFractionSalt,
    massFractionSpices,
)==True:

    N_dumpling_machines = dumpling_machines(
        dailyOutputFinishedProducts, t, dumplingMachineProductivity
    )
    N_dough_kneading_machines = dough_kneading_machines(
        dailyOutputFinishedProducts, t, massFractionDough, kneadingMachinePerformance
    )
    N_cutter_machines = cutter_machines(
        dailyOutputFinishedProducts, t, massFractionDough, cutterPerformance
    )


    print(N_dumpling_machines)
    print(N_dough_kneading_machines)
    print(N_cutter_machines)
else:
    print("Invalid set of components")