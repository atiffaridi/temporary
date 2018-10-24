# Author: Atif Faridi
# Objective: Plot for stock price trend for a year

# importing required modules
from bokeh.plotting import figure, output_file, save
import pandas as pd

# path of stock data
path = 'INFY.NS.csv'

# read csv file using pandas
data = pd.read_csv(path, parse_dates=['Date'])

# convert datetime string to pandas datetime timestamp
data['Date'] = pd.to_datetime(data['Date'])

# create an initialize figure with parameters
p = figure(plot_width=800, plot_height=250, x_axis_label='Date', y_axis_label='Price', x_axis_type="datetime")

# draw trend line
p.line(data['Date'], data['Close'], color='navy', alpha=0.5)

# output html file for the plot
output_file("timeseries.html")

# save figure as html file
save(p)
