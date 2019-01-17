# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 23:14:08 2018

@author: patel
"""

def subplot_hist(data, row = 4, column = 3, title = "Histogram of the white wine Predictors", height = 10, width = 20):
    # Create a figure instance, and the two subplots
    import matplotlib.pyplot as plt
    import seaborn as sns
    fig = plt.figure(figsize = (width, height))
    fig.suptitle(title, fontsize=25, y = 0.93)
    # Run loop over the all the variables
    for i in range(data.shape[1]):
        # Create the axis line
        ax = fig.add_subplot(row, column, i + 1)
        fig.subplots_adjust(hspace = .5)
        # Create histogram for each variable
        sns.distplot(data.iloc[:, i], ax=ax)
        ax.xaxis.get_label()
    # Show the plot
    plt.show()


def subplot_box(data, row = 4, column = 3, title = "Boxplot of the white wine Predictors", height = 10, width = 20):
    # Create a figure instance, and the two subplots
    import matplotlib.pyplot as plt
    import seaborn as sns
    fig = plt.figure(figsize = (width, height))
    fig.suptitle(title, fontsize=25, y = 0.93)
    # Run loop over the all the variables
    for i in range(data.shape[1]):
        # Create the axis line
        ax = fig.add_subplot(row, column, i + 1)
        fig.subplots_adjust(hspace = .5)
        # Create histogram for each variable
        sns.boxplot(data.iloc[:, i], ax=ax)
        ax.xaxis.get_label()
    # Show the plot
    plt.show()
    
