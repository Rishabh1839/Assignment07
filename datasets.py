# using numpy library
import numpy as np
# using matplotlib to plot the data into a graph
import matplotlib.pyplot as plt

# here I will be classifying living beings such as plants and animals
livingBeings = 500
plants = 500
animals = 500
# on this other part I will be classifying the rest of what includes as a living being such as fungi and insects
livingBeings2 = 500
fungi = 500
insects = 500

# here is our data
lB = 5000 + 500 * np.random.randn(livingBeings)
beings01 = 2000 + 500 * np.random.randn(plants)
beings02 = 300 + 500 * np.random.randn(animals)

# part 2 of our data for classifying living beings
lB2 = 10000 + 500 * np.random.randn(livingBeings2)
lBeings01 = 4000 + 500 * np.random.randn(fungi)
lBeings02 = 7000 + 500 * np.random.randn(insects)

# the next step will be to have our data being visualized in a histogram
#
#
#
#
plt.hist([lB, beings01, beings02, lB2, lBeings01, lBeings02], stacked=True,
         color=['r', 'g', 'w', 'b', 'k', 'c'], edgecolor='k')

#
plt.suptitle("Living beings")
# plotting the axis for it to fit all the data on graph
plt.axis('tight')
# shows the plot
plt.show()

