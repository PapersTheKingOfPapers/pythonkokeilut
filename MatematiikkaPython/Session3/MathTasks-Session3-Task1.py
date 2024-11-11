from matplotlib import pyplot as plt, patches
from fractions import Fraction
import numpy as np
import matplotlib as mpl

fig = plt.figure()
ax = fig.subplots()

# Add a circle representing the unit circle
ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

# Input array of angles in degrees
degree_angles = np.array([30, 45, 60, 90, 120, 150, 180, 270])

# Convert degrees to radians (for calculations)
radian_angles = degree_angles * (np.pi / 180)  # Degrees to radians

# Generate colors dynamically based on the number of points
color_list = ['red', 'green', 'blue', 'yellow', 'purple', 'brown']  # Define more colors if necessary
varit = np.array([color_list[i % len(color_list)] for i in range(len(degree_angles))])

def generate_text(degrees):
    if degrees == 90:
        return r'$\frac{\pi}{2}$'
    elif degrees == 180:
        return r'$\pi$'
    elif degrees == 360:
        return r'$2\pi$'
    else:
        frac = Fraction(degrees, 180)
        if frac.denominator == 1:
            return f"${frac.numerator}\\pi$"
        elif frac.numerator == 1:
            return f"$\\frac{{\\pi}}{{{frac.denominator}}}$"
        else:
            return f"$\\frac{{{frac.numerator}\\pi}}{{{frac.denominator}}}$"


text = [generate_text(degree) for degree in degree_angles]

# Function to calculate x, y based on the angle in radians
def calculate_coordinates(radians):
    x = np.cos(radians)
    y = np.sin(radians)
    return x, y

# Calculate x, y coordinates for each point using radians
x = np.array([calculate_coordinates(r)[0] for r in radian_angles])
y = np.array([calculate_coordinates(r)[1] for r in radian_angles])

plt.scatter(x, y, color=varit, marker='X')

for i in range(len(degree_angles)):
    plt.annotate(text[i],
                 xy=(float(x[i]), float(y[i])), xycoords='data',  # Force conversion to float
                 xytext=(+30, +5), textcoords='offset points', fontsize=12,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.show()
