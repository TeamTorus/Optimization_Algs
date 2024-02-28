from scipy.optimize import minimize
from simulation import cost_function, control_points_array, rand_cp_arr

tolerance = 1e-5
options = {'maxiter': 500, 'disp': True, 'adaptive': True}
options2 = {'disp': True}

result = minimize(cost_function, control_points_array, method='Nelder-Mead', options=options2)

# Print the result
print("Optimized parameters:", result.x)
print("Minimum value of cost function:", result.fun)
