#!/usr/local/opt/python/bin/python3.7

import os
import glob
from random import randint
from random import choices

if __name__ == "__main__":

    rollTablesList = []
    rollTablesPath = "./tables/"

    for fileName in glob.glob(os.path.join(rollTablesPath, "*.table")):
        fileName = os.path.splitext(os.path.basename(fileName))[0]
        rollTablesList.append(fileName)

    while True:
        print("+=--- Available Roll Tables ---=+")
        for i in range(len(rollTablesList)):
            print("{}: {}".format(i + 1, rollTablesList[i].title()))
        print("Q: Quit")

        userChoice = input("+=--- What will you roll?: ")
        if userChoice.upper() == "Q":
            break

        if userChoice.islower() or int(userChoice) > len(rollTablesList):
            continue

        with open(rollTablesPath + rollTablesList[int(userChoice) - 1] + ".table") as f:

            weights, options = [], []
            for line in f:
                weight, option = line.strip().split(":")
                weights.append(int(weight))
                options.append(option.strip())

        # then in your loop
        print("\n+=----\n| " + choices(options, weights=weights)[0] + "\n+=----\n")
