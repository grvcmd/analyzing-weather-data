import csv

import matplotlib.pyplot as plt
from matplotlib.axes import Axes


filename = "data/sitka_weather_07-2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # call next() once to get the first line of the file

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get the high temps
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

    # Plot the high temps
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax: Axes
    ax.plot(highs, c='red')

    # Format the plot
    ax.set_title("Daily high temperatures, July 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    ax.set_ylabel('Temperature (F)', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()






