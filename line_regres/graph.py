import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

large = 22
med = 16
small = 12
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

def set_graph(x,y, y1, ostatki):
    gridsize = (3, 2)
    fig = plt.figure(figsize=(12, 8))
    ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=2)
    ax2 = plt.subplot2grid(gridsize, (2, 0))
    ax3 = plt.subplot2grid(gridsize, (2, 1))

    ax1.scatter(x=x.arr_data, y=y.arr_data, marker='o', c='r', edgecolor='b')
    ax1.plot(x.arr_data, y1, label="second", mec= None, lw=2, mew=2, ms=12)
    ax1.set_xlabel(x.name)
    ax1.set_ylabel(y.name)

    ax2.scatter(x=x.arr_data, y=ostatki, marker='o', c='r', edgecolor='b')
    ax2.set_xlabel(x.name)
    ax2.set_ylabel('ostatki')

    ax3 = stats.probplot(ostatki, dist='norm', plot=plt)

    plt.show()