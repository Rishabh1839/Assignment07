print("=" * 30)
print("Classifying our own Data sets")
print("Created by Rishabh Singh")
print("=" * 30)
print("What is the purpose of this program?")
print("In Machine learning, classification is the problem of identifying to which of a set of categories a new")
print("observation belongs, on the basis of a training set of data containing observations whose category membership")
print("is known. In this program we have used to numpy library for supporting a large multi dimensional arrays and")
print("matrices. The other library we have used is Matplotlib which is an numerical mathematical extension for the")
print("numpy library. Here we will be classifying living beings such as plants and animals. I set their value for 500")
print("on the other part I classified the rest of what includes as a living being such as fungi and insects.")
print(
    "We will be classifying our data for the categories we chose. Then pretty much we have to label the data and plot")
print("the remaining data. The output will show us a colorful graph that shows the classification of our data.")

# using numpy library
import numpy as np
# using matplotlib to plot the data into a graph
import matplotlib.pyplot as plt

# here  will be classifying living beings such as plants and animals
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
# labeling the colors
# LB = living beings = red
# beings01 = green
# beings 02 = yellow
# LB2 = Living beings 2 = blue
# lBeings01 = living beings 01 = black
# lBeings02 = living beings 02 = cyan
plt.hist([lB, beings01, beings02, lB2, lBeings01, lBeings02], stacked=True,
         color=['r', 'g', 'y', 'b', 'k', 'c'], edgecolor='k')
# here is the subtitle for our graph that we created
plt.suptitle("Living beings")
# plotting the axis for it to fit all the data on graph
plt.axis('tight')
# shows the plot
plt.show()
