import numpy as np
from simulation import cost_function, control_points_array

# Approximate gradient of the cost function at point x using finite differences.
def approximate_gradient(cost_function, x, epsilon=1e-2):

    gradient = np.zeros_like(x)
    for i in range(len(x)):
        x_plus_delta = x.copy()
        x_plus_delta[i] += epsilon
        cost_plus_delta = cost_function(x_plus_delta)
        
        x_minus_delta = x.copy()
        x_minus_delta[i] -= epsilon
        cost_minus_delta = cost_function(x_minus_delta)
        
        gradient[i] = (cost_minus_delta - cost_plus_delta) / (2 * epsilon)

    # print(gradient)
    return gradient

def stochastic_gradient_descent(cost_function, initial_guess, learning_rate=0.01, max_iterations=20000, tolerance=1e-5):
    x = initial_guess
    iteration = 0

    while iteration < max_iterations:
        gradient = approximate_gradient(cost_function, x)
        x_new = x + learning_rate * gradient
        if np.linalg.norm(x_new - x) < tolerance:
            break
        x = x_new
        iteration += 1
    return x

# Example usage
initial_guess = control_points_array
minimized_params = stochastic_gradient_descent(cost_function, initial_guess)
print("Minimized parameters:", minimized_params)
print("Minimum value of cost function:", cost_function(minimized_params))
