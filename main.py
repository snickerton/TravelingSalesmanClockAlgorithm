import matplotlib.pyplot as plt
from matplotlib import collections as mc
import numpy as np
from math import atan2
import math
import BruteForce

drawline = True
try_brute_force = True
show_animation = True
animation_pause = .1
point_labels_on = False

NUMBER_OF_POINTS = 11
POINTS_MAX_RANGE = 100
rng = np.random.RandomState(1)
x_values = rng.rand(NUMBER_OF_POINTS) * POINTS_MAX_RANGE
y_values = rng.rand(NUMBER_OF_POINTS) * POINTS_MAX_RANGE
point_labels = [str(x) for x in range(NUMBER_OF_POINTS)]
angles_to_center = []

total_path_length = 0

# find average point
avg_x_values = sum(x_values) / len(x_values)
avg_y_values = sum(y_values) / len(y_values)
print("Average point: {}, {}".format(avg_x_values, avg_y_values))
center = (avg_x_values, avg_y_values)

# center = (91, 10)
# one line: [(x_values,y_values), (x,y_values)]
lines = []

left_center = (0, center[1])

coors = list(zip(x_values, y_values))
print("Coordinates: ", str(coors))

# find angle of left_center_point > center > point_in_coors
for i, point in enumerate(coors):
    vector_center_to_point = np.subtract(point, center)
    vector_center_to_left_center = np.subtract(left_center, center)

    # instead of dot product we do this to maintain angles > 180
    ang_c_p = atan2(*vector_center_to_point)
    ang_c_l = atan2(*vector_center_to_left_center)
    # FUCK IT'S IN RADIANS
    angle = (ang_c_p - ang_c_l) * 180 / np.pi

    angles_to_center.append(angle)
    point_labels[i] = point_labels[i] + ", " + str(angle)

coors_with_angles = list(zip(coors, angles_to_center))
# sort coordinates by ascending angles (clockwise)
coors_with_angles.sort(key=lambda x: x[1])
print("Coordinates with angles: ", coors_with_angles)

print("Labels for points: ", point_labels)

# def create_lines_for_path(coors_with_angles)
# Create lines array for drawing lines between
# AND calculate total path length

prev_point = coors_with_angles[0][0]
for i, item in enumerate(coors_with_angles[1:]):
    point = item[0]
    lines.append([prev_point, point])
    vector = np.subtract(point, prev_point)
    total_path_length += math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    prev_point = point

point = coors_with_angles[0][0]
lines.append([point, prev_point])
vector = np.subtract(point, prev_point)
total_path_length += math.sqrt(vector[0] ** 2 + vector[1] ** 2)

print("asdlkfjasld", len(coors_with_angles))

print(lines)
print(*lines[0])

print("\n*************\nFINAL PATH: ", total_path_length)

human_guess = [x for x in range(NUMBER_OF_POINTS)] + [0]
print(human_guess)

lis = []
with open("BestPath.txt", "w") as f:
    f.write("Begin \n")
bf = BruteForce.BruteForce(total_path_length)
print("init bf with pl: ", bf.smallest_route)

# OK SO THIS IS STUPID/CRAZY/GENIUS
# We use a "raise Exception" to "break;" out of the recursive function bf.bruteforce if our path length has improved by .01 (the four param in the method)
# In the exception method we write our desired return value (in this case, the first path that improves more than 10%)
# then we repr() the exception to change it to a string
# then substring it to get just the exception message (the array)
# then eval() the array to change it to code

try:
    print("beginning try")
    if(try_brute_force):
        bf.brute_force(lis, coors.copy(), [x for x in range(len(coors))], .01)
except Exception as e:
    human_guess = eval(str(repr(e))[11:-2])
    print("Bot guess: ", human_guess)

if human_guess == [x for x in range(NUMBER_OF_POINTS)] + [0]:
    print("Bot was unable to find better solution than given one")
    # human_guess = [x for x in range(NUMBER_OF_POINTS)]

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 7))

for ax in axes:
    ax.plot(x_values, y_values, 'o')

    if (point_labels_on):
        for i, txt in enumerate(point_labels):
            ax.text(x_values[i], y_values[i], txt)

plt.axes(axes[0])
test = 0
if drawline == True:
    plt.plot(center[0], center[1], "ro")
    # animate lines drawing
    for line in lines:
        # l = [line[0][0], line[1][0]], [line[0][1], line[1][1]]
        vector = np.subtract(line[0], line[1])
        ds = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
        test += ds
        plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], label=ds)
        # plt.legend()
        if(animation_pause):
            plt.pause(animation_pause)
    plt.title("Clock Algo: " + str(total_path_length))

    print(test)
    plt.axes(axes[1])
    path2 = 0
    prev_point = coors[human_guess[0]]
    for index in human_guess[1:]:
        point = coors[index]
        plt.plot([prev_point[0],point[0]], [prev_point[1], point[1]])
        if (animation_pause):
            plt.pause(animation_pause)
        vector = np.subtract(point, prev_point)
        path2 += math.sqrt(vector[0] ** 2 + vector[1] ** 2)
        prev_point = point

    point = coors[human_guess[0]]
    plt.plot([prev_point[0], point[0]], [prev_point[1], point[1]])
    if (animation_pause):
        plt.pause(animation_pause)
    vector = np.subtract(point, prev_point)
    path2 += math.sqrt(vector[0] ** 2 + vector[1] ** 2)

    plt.title("Brute Force Limited: " + str(path2))
    plt.pause(animation_pause)

    print("FINAL PATH2: ", path2)

plt.show()
