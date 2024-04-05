import matplotlib.pyplot as plt

left = [1, 2, 3, 4, 5, 6]
height = [10, 15, 45, 35, 5, 20]
tick_label = ['one', 'two', 'three', 'four', 'five', 'six']

colors = ['green', 'red', 'orange', 'purple', 'cyan', 'yellow']

plt.bar(left, height, tick_label=tick_label, width=0.6, color=colors)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('BAR CHART')


plt.grid(axis='y', linestyle='--', alpha=0.9)

for i, v in enumerate(height):
    plt.text(left[i] - 0.1, v + 1, str(v), color='black')


plt.legend(['Bars'], loc='upper right')

plt.show()


# STEPS:
# Import the matplotlib.pyplot module as plt.

# Define three lists:

# left: Represents the x-axis positions of the bars.
# height: Represents the heights of the bars.
# tick_label: Represents the labels for each bar.
# Define a list colors containing the colors for the bars.

# Create a bar chart using the plt.bar() function, passing left, height, and tick_label as arguments. Also, set the width of the bars to 0.6 and the colors of the bars using the color parameter.

# Add labels to the x-axis and y-axis using plt.xlabel() and plt.ylabel() respectively.

# Set the title of the plot using plt.title().

# Add grid lines to the y-axis with plt.grid(axis='y', linestyle='--', alpha=0.9).

# Add annotations to each bar showing the height value using a for loop and plt.text().

# Add a legend to the plot using plt.legend(['Bars'], loc='upper right'). This legend represents the bars in the bar chart.

# Display the plot using plt.show().



