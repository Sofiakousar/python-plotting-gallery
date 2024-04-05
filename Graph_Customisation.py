import matplotlib.pyplot as plt


x = [3, 4, 7,8]
y = [4, 4, 6,8]

plt.plot(x, y, color='purple', linestyle='dashed',linewidth=4,marker='*',markerfacecolor='blue',markersize=12)

plt.ylim(2,9)
plt.xlim(2,9)


plt.xlabel('X Axis')

plt.ylabel( 'Y Axis')

plt.title('Colored Line and Scatter Plot')

plt.show()
