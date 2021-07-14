import csv
from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

filename = "data/death_valley_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates, and high and low temps for death valley
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # Plot the high and low temps for death valley
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax: Axes
    ax.plot(dates, highs, c='red', alpha=0.6)
    ax.plot(dates, lows, c='blue', alpha=0.6)
    ax.fill_between(dates, highs, lows, facecolor='purple', alpha=0.1)

    # Format the plot
    title = "Daily high and low tempaeratures - 2018\nDeath Valley, CA"
    ax.set_title(title, fontsize=20)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel('Temperature (F)', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()