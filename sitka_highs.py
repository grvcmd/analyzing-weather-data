import csv
from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib.axes import Axes


filename = "data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # call next() once to get the first line of the file

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates, and high and low temps from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    # Plot the high and low temps
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax: Axes
    ax.plot(dates, highs, c='red', alpha=0.6)
    ax.plot(dates, lows, c='blue', alpha=0.6)
    ax.fill_between(dates, highs, lows, facecolor='purple', alpha=0.1)

    # Format the plot
    ax.set_title("Daily high and low temperatures - 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel('Temperature (F)', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()






