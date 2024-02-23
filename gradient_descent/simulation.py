import numpy as np

control_points = np.array([[0, 0, 0], [0, 1, 0], [1, 1, 1], [1, 0, 5], [2, 0, 0], [2, 1, 0], [3, 1, 0], [3, 0, 0], [102, 0, 0]])

# turn control points into a 1D array
control_points_array = control_points.flatten()


# returns distance to 
def cost_function(control_points_array):
    cost = 0
    for each in control_points_array:
        cost += abs(each)
    return cost

# print(cost_function(control_points_array))