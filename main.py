# ----------------------------------------------------------------
#                   Shell Sort Visualization
#                  Made by Monter, John Paul S.
#                Design and Analysis of Algorithms
# ----------------------------------------------------------------

from random import randint
import matplotlib.pyplot as plt
import numpy as np


def shellSort(array):
    global COMPARISON
    n = len(array)
    gap = n // 2
    x = np.arange(0, len(array), 1)

    while gap > 0:
        for z in range(gap, n):
            COMPARISON += 1
            temp = array[z]
            j = z
            plt.title("Shell Sort", fontsize=48, fontweight='bold')
            plt.text(X, Y, 'COMPARISON: %s' % COMPARISON, fontsize=14, color='white')
            colors = ['gray'] * len(array)
            colors[z] = 'red'
            colors[z - gap] = 'red'
            plt.bar(x, array, color=colors)
            plt.axis('off')
            plt.pause(SPEED)
            plt.clf()

            while j >= gap and array[j - gap] > temp:
                COMPARISON += 1
                array[j] = array[j - gap]
                j -= gap
                plt.title("Shell Sort", fontsize=48, fontweight='bold')
                plt.text(X, Y, 'COMPARISON: %s' % COMPARISON, fontsize=14, color='white')
                colors = ['gray'] * len(array)
                colors[j] = 'tab:orange'
                colors[j + gap] = 'tab:blue'
                plt.bar(x, array, color=colors)
                plt.axis('off')
                plt.pause(SPEED)
                plt.clf()

            array[j] = temp
            plt.title("Shell Sort", fontsize=48, fontweight='bold')
            plt.text(X, Y, 'COMPARISON: %s' % COMPARISON, fontsize=14, color='white')
            colors = ['gray'] * len(array)
            colors[j] = 'tab:green'
            if j > gap:
                colors[j - gap] = 'tab:green'
            else:
                colors[gap - j] = 'tab:green'
            plt.bar(x, array, color=colors)
            plt.axis('off')
            plt.pause(SPEED)
            plt.clf()

        gap //= 2

    return array


def getInput(prompt, x):
    if x == 1:
        valid = True
        while valid:
            try:
                enter = int(input(prompt))
                if enter <= 0:
                    print("Enter number greater than 0")
                else:
                    return enter
            except ValueError:
                print("Enter Number only")
    else:
        valid = True
        while valid:
            try:
                enter = input(prompt)
                loweredEnter = enter.lower()
                if loweredEnter == 'y' or loweredEnter == "yes":
                    return True
                elif loweredEnter == 'n' or loweredEnter == "no":
                    return False
                else:
                    print("Yes or No only!!")
            except ValueError:
                print("Enter Yes or No only!")


if __name__ == "__main__":
    COMPARISON = 0
    MAX = 100
    SPEED = 0.0000000000000000000001
    X = -20
    Y = 110
    elements = getInput("Enter number of Elements: ", 1)

    listOfElements = [] * elements
    if elements >= 10:
        check = getInput("Auto Generate Elements [Y/N]: ", 2)
        if check:
            for i in range(1, elements + 1):
                listOfElements.append(randint(1, MAX))
        else:
            for i in range(1, elements + 1):
                listOfElements.append(getInput("Enter Element %i: " % i, 1))
    else:
        for i in range(1, elements + 1):
            listOfElements.append(getInput("Enter Element %i: " % i, 1))

    plt.rcParams['toolbar'] = 'None'
    plt.style.use('dark_background')
    print("Unsorted List: ", listOfElements)
    sortedArray = shellSort(listOfElements)
    for k in range(elements):
        plt.title("Shell Sort", fontsize=48, fontweight='bold')
        plt.text(X, Y, 'COMPARISON: %s' % COMPARISON, fontsize=14, color='white')
        colors1 = ['grey'] * elements
        colors1[:k+1] = ['green'] * (k + 1)
        plt.bar(list(range(elements)), sortedArray, color=colors1)
        plt.axis('off')
        plt.pause(SPEED)
        plt.clf()

    print("Sorted List: ", sortedArray)
    plt.title("Shell Sort", fontsize=48, fontweight='bold')
    plt.text(X, Y, 'COMPARISON: %s' % COMPARISON, fontsize=14, color='white')
    plt.bar(list(range(elements)), sortedArray, color="green")
    plt.axis('off')
    plt.show()
