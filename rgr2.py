import matplotlib.pyplot as plt
import tkinter as tk
import math
import numpy as np


def toFloat(x):
    return float(x)


def inputNum(text):
    while True:
        try:
            return toFloat(input(text))
        except:
            pass
        print("\nInput any number.")


def inputParam():
    a = inputNum("Input a: ")
    b = inputNum("Input b: ")
    xmin = inputNum("Input xmin: ")
    while True:
        try:
            xmax = input("Input xmax: ")
            xmax = toFloat(xmax)
            while xmax < xmin:
                xmax = print("\nSorry, xmax must be bigger than xmin.\n")
            break
        except:
            pass
        print("\nInput any number." + " ")
    while True:
        try:
            stepd = input("Input discretization step: ")
            stepd = toFloat(stepd)
            while stepd <= 0:
                stepd = input("\nStep must be bigger than zero.\n")
            break
        except:
            pass
        print("\nInput any number.")
    if stepd <= 5:
        step = stepd / 5
    else:
        step = stepd / stepd
    tempx = [xmin, xmax]
    tempy = [0, 0]
    return a, b, xmin, xmax, stepd, step, tempx, tempy


def update1(plt, ax, x, y, a, b, tempx, tempy, butt):
    x.clear()
    y.clear()
    ax.cla()
    loop = np.arange(xmin, xmax, step)
    for i in loop:
        if i / a < 0 or i + 5 < 0 or i == 0 or a-3*b*math.sqrt(i+5) == 0 or (math.log10(i/a)+(b/2*i))/(a-3*b*math.sqrt(i+5)) < 0:
            pass
        else:
            x.append(i)
            y.append(math.sqrt((math.log10(i/a)+(b/2*i))/(a-3*b*math.sqrt(i+5))) - 16)
    ax.scatter(x, y, s=5, c='g')
    ax.scatter(tempx, tempy, s=20, c='b', marker='s', label='ends')
    ax.legend()
    plt.ylabel("Level")
    plt.xlabel("Time")
    plt.show()
    butt.config(command=lambda: update2(plt, ax, x, y, a, b, tempx, tempy, butt))
    ax.set_title(label='Analogue Signal', fontsize=20, color="green", loc='center')


def update2(plt, ax, x, y, a, b, tempx, tempy, butt):
    x.clear()
    y.clear()
    ax.cla()
    loop = np.arange(xmin, xmax, stepd)
    for i in loop:
        if i / a < 0 or i + 5 < 0 or i == 0 or a - 3 * b * math.sqrt(i + 5) == 0 or (math.log10(i/a)+(b/2*i))/(a-3*b*math.sqrt(i+5)) < 0:
            pass
        else:
            x.append(i)
            y.append(math.sqrt((math.log10(i/a)+(b/2*i))/(a-3*b*math.sqrt(i+5)))-16)
    ax.scatter(x, y, s=5, c='g')
    ax.scatter(tempx, tempy, s=20, c='b', marker='s', label='ends')
    ax.legend()
    plt.ylabel("Level")
    plt.xlabel("Time")
    plt.show()
    butt.config(command=lambda: update3(plt, ax, x, y, a, b, tempx, tempy, butt))
    ax.set_title(label='Quantization by time', fontsize=20, color="green", loc='center')


def update3(plt, ax, x, y, a, b, tempx, tempy, butt):
    x.clear()
    y.clear()
    ax.cla()
    loop = np.arange(xmin, xmax, step)
    for i in loop:
        if i / a < 0 or i + 5 < 0 or i == 0 or a - 3 * b * math.sqrt(i + 5) == 0 or (math.log10(i/a)+(b/2*i))/(a-3*b*math.sqrt(i+5)) < 0:
            pass
        else:
            x.append(i)
            temp = (math.sqrt((math.log10(i/a)+(b/2*i))/(a-3*b*math.sqrt(i+5)))-16)
            y.append(temp + (stepd-(temp % stepd)))
    ax.scatter(x, y, s=5, c='g')
    ax.scatter(tempx, tempy, s=20, c='b', marker='s', label='ends')
    ax.legend()
    plt.ylabel("Level")
    plt.xlabel("Time")
    plt.show()
    butt.config(command=lambda: update4(plt, ax, x, y, a, b, tempx, tempy, butt))
    ax.set_title(label='Quantization by level', fontsize=20, color="green", loc='center')


def update4(plt, ax, x, y, a, b, tempx, tempy, butt):
    x.clear()
    y.clear()
    ax.cla()
    loop = np.arange(xmin, xmax, stepd)
    for i in loop:
        if i / a < 0 or i + 5 < 0 or i == 0 or a - 3 * b * math.sqrt(i + 5) == 0 or (math.log10(i/a)+(b/2*i))/(a-3*b*math.sqrt(i+5)) < 0:
            pass
        else:
            x.append(i)
            temp = (math.sqrt((math.log10(i / a) + (b / 2 * i)) / (a - 3 * b * math.sqrt(i + 5))) - 16)
            y.append(temp + (stepd-(temp % stepd)))
    ax.scatter(x, y, s=5, c='g')
    ax.scatter(tempx, tempy, s=20, c='b', marker='s', label='ends')
    ax.legend()
    plt.ylabel("Level")
    plt.xlabel("Time")
    plt.show()
    butt.config(command=lambda: update1(plt, ax, x, y, a, b, tempx, tempy, butt))
    ax.set_title(label='Digital Signal', fontsize=20, color="green", loc='center')


def refresh1():
    update1(plt)


def refresh2():
    update2(plt)


def refresh3():
    update3(plt)


def refresh4():
    update4(plt)

def anew():
    global a, b, xmin, xmax, stepd, step, tempx, tempy
    a, b, xmin, xmax, stepd, step, tempx, tempy = inputParam()
    refresh1()

fig, ax = plt.subplots()
x = [-3, -2, -1, 0, 1, 2, 3, 0, 0, 0, 0, 0]
y = [1, 0, -0.5, 0, -0.5, 0, 1, 2, 3, -1, 1, -0.5]
a, b, xmin, xmax, stepd, step, tempx, tempy = inputParam()

butt = tk.Button(text='Next', command=lambda: update1(plt, ax, x, y, a, b, tempx, tempy, butt))
butt.pack()
restart = tk.Button(text='Restart', command=anew)
restart.pack()

ax.set_title(label='Welcome!', fontsize=20, color="green", loc='center')
ax.scatter(x, y, s=30, c='r')
plt.show()
