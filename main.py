# ----------------------------------------------------------------
#                   Shell Sort Visualization
#                  Made by Monter, John Paul S.
#                Design and Analysis of Algorithms
# ----------------------------------------------------------------

from random import randint
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def shellSort(array):
    global COMPARISON
    global figure1, bar1, set1, bar_container
    n = len(array)
    gap = n // 2
    x = np.arange(0, len(array), 1)

    while gap > 0:
        for z in range(gap, n):
            COMPARISON += 1
            temp = array[z]
            j = z
            set1.cla()
            set1.set_title("Shell Sort", fontsize=48, fontweight='bold')
            set1.text(X, Y, 'COMPARISON: %s' % COMPARISON, fontsize=14, color='white')
            colors = ['gray'] * len(array)
            colors[z] = 'red'
            colors[z - gap] = 'red'
            bar_container = set1.bar(x, array, color=colors)
            set1.bar_label(bar_container, fmt='{:,.0f}')
            set1.axis('off')
            bar1.draw()
            window.update()
            window.after(SPEED)

            while j >= gap and array[j - gap] > temp:
                COMPARISON += 1
                array[j] = array[j - gap]
                j -= gap
                set1.cla()
                set1.set_title("Shell Sort", fontsize=48, fontweight='bold')
                set1.text(X, Y, 'COMPARISON: %s' % COMPARISON, fontsize=14, color='white')
                colors = ['gray'] * len(array)
                colors[j] = 'tab:orange'
                colors[j + gap] = 'tab:blue'
                bar_container = set1.bar(x, array, color=colors)
                set1.bar_label(bar_container, fmt='{:,.0f}')
                set1.axis('off')
                bar1.draw()
                window.update()
                window.after(SPEED)

            array[j] = temp
            set1.cla()
            set1.set_title("Shell Sort", fontsize=48, fontweight='bold')
            set1.text(X, Y, 'COMPARISON: %s' % COMPARISON, fontsize=14, color='white')
            colors = ['gray'] * len(array)
            colors[j] = 'tab:green'
            if j > gap:
                colors[j - gap] = 'tab:green'
            else:
                colors[gap - j] = 'tab:green'
            bar_container = set1.bar(x, array, color=colors)
            set1.bar_label(bar_container, fmt='{:,.0f}')
            set1.axis('off')
            bar1.draw()
            window.update()
            window.after(SPEED)

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
    window = tk.Tk()
    window.title("Shell Sort Visualizer")
    window.geometry("1280x768")

    COMPARISON = 0
    MAX = 100
    SPEED = 1
    X = 0
    Y = 100
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
    figure1 = plt.Figure(figsize=(6, 5), dpi=100)
    set1 = figure1.add_subplot(111)

    bar1 = FigureCanvasTkAgg(figure1, window)
    bar1.get_tk_widget().pack(side="top", fill="both", expand=True)

    print("Unsorted List: ", listOfElements)
    sortedArray = shellSort(listOfElements)
    for k in range(elements):
        set1.cla()
        set1.set_title("Shell Sort", fontsize=48, fontweight='bold')
        set1.text(X, Y, 'COMPARISON: %s' % COMPARISON, fontsize=14, color='white')
        colors1 = ['grey'] * elements
        colors1[:k + 1] = ['green'] * (k + 1)
        bar_container = set1.bar(list(range(elements)), sortedArray, color=colors1)
        set1.bar_label(bar_container, fmt='{:,.0f}')
        set1.axis('off')
        bar1.draw()
        window.update()
        window.after(SPEED)

    print("Sorted List: ", sortedArray)
    set1.cla()
    set1.set_title("Shell Sort", fontsize=48, fontweight='bold')
    set1.text(X, Y, 'COMPARISON: %s' % COMPARISON, fontsize=14, color='white')
    bar_container = set1.bar(list(range(elements)), sortedArray, color="green")
    set1.bar_label(bar_container, fmt='{:,.0f}')
    set1.axis('off')
    bar1.draw()
    window.update()
    window.after(10)

    window.mainloop()
