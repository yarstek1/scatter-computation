import matplotlib.pyplot as plt
import statistics
from math import sqrt


def plot_confidence_interval(x, values, z=1.96, color='#2187bb', horizontal_line_width=0.25):
    mean = statistics.mean(values)
    stdev = statistics.stdev(values)
    confidence_interval = z * stdev / sqrt(len(values))

    left = x - horizontal_line_width / 2
    top = mean - confidence_interval
    right = x + horizontal_line_width / 2
    bottom = mean + confidence_interval
    plt.plot([x, x], [top, bottom], color=color,  linewidth=0.8)
    plt.plot([left, right], [top, top], color=color, linewidth=0.8)
    plt.plot([left, right], [bottom, bottom], color=color, linewidth=0.8)
    plt.plot(x, mean, 'o', color='#f44336')

    return mean, confidence_interval

def whisker_plot(x, mean, confidence_interval, color_dot, marker_dot, color_whisker, z=1.96, horizontal_line_width=0.25):

    left = x - horizontal_line_width / 2
    top = mean - confidence_interval
    right = x + horizontal_line_width / 2
    bottom = mean + confidence_interval
    plt.plot([x, x], [top, bottom], color=color_whisker, linewidth=0.8)
    plt.plot([left, right], [top, top], color=color_whisker, linewidth=0.8)
    plt.plot([left, right], [bottom, bottom], color=color_whisker, linewidth=0.8)
    plt.plot(x, mean, marker = marker_dot, color=color_dot)
