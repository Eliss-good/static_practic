import numpy as np
import matplotlib.pyplot as plt


def set_graph_one(x,y,y1):
    large = 22; med = 16; small = 12
    params = {'axes.titlesize': large,
            'legend.fontsize': med,
            'figure.figsize': (16, 10),
            'axes.labelsize': med,
            'axes.titlesize': med,
            'xtick.labelsize': med,
            'ytick.labelsize': med,
            'figure.titlesize': large}
    plt.rcParams.update(params)
    plt.style.use('seaborn-whitegrid')

    fig, (ax1) = plt.subplots(
        nrows=1, ncols=1,
        figsize=(8, 4)
    )
    
    ax1.scatter(x=x.arr_data, y=y.arr_data, marker='o', c='r', edgecolor='b')
    ax1.plot(x.arr_data, y1, label="second", mec= None, lw=2, mew=2, ms=12)
    ax1.set_xlabel(x.name)
    ax1.set_ylabel(y.name)

    plt.show()

def set_graph_two(x1,y1,x2,y2):
    plt.plot(x1, y1, label="second", mec= None, lw=2, mew=2, ms=12)

    plt.show()