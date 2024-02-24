import numpy as np
from simulation import cost_function, rand_cp_arr

def nelder_mead(cost_function, initial_simplex, alpha=1, beta=0.5, gamma=2, max_iterations=10, tol=1e-10):

    num_variables = len(initial_simplex[0])
    num_vertices = num_variables + 1
    
    # Initialize simplex
    simplex = initial_simplex
    simplex_values = [cost_function(point) for point in simplex]
    
    # Main optimization loop
    for iteration in range(max_iterations):
        # Sort vertices based on function values
        sorted_indices = np.argsort(simplex_values)
        sorted_simplex = [simplex[i] for i in sorted_indices]
        sorted_values = [simplex_values[i] for i in sorted_indices]
        
        # Calculate centroid (excluding worst point)
        centroid = np.mean(sorted_simplex[:-1], axis=0)
        print(sorted_values)
        
        # Reflect
        reflected_point = centroid + alpha * (centroid - sorted_simplex[-1])
        reflected_value = cost_function(reflected_point)
        print("Worst: ", sorted_simplex[-1])
        print("Worst value: ", sorted_values[-1])
        print("Best value: ", sorted_values[0])
        print("Reflected:", reflected_point)
        print(reflected_value)
        
        if sorted_values[0] <= reflected_value < sorted_values[-2]:
            # Replace worst point with reflected point
            simplex[-1] = reflected_point
            simplex_values[-1] = reflected_value
        elif reflected_value < sorted_values[0]:
            # Expand
            expanded_point = centroid + gamma * (reflected_point - centroid)
            expanded_value = cost_function(expanded_point)
            if expanded_value < reflected_value:
                simplex[-1] = expanded_point
                simplex_values[-1] = expanded_value
            else:
                simplex[-1] = reflected_point
                simplex_values[-1] = reflected_value
        else:
            # Contract
            contracted_point = centroid + beta * (sorted_simplex[-1] - centroid)
            contracted_value = cost_function(contracted_point)
            if contracted_value < sorted_values[-1]:
                simplex[-1] = contracted_point
                simplex_values[-1] = contracted_value
            else:
                # Shrink
                for i in range(1, num_vertices):
                    simplex[i] = sorted_simplex[0] + 0.5 * (simplex[i] - sorted_simplex[0])
                    simplex_values[i] = cost_function(simplex[i])
        
        # Check convergence
        # if np.max(np.abs(np.array(sorted_values) - sorted_values[0])) < tol:
        #     break
    
    sorted_indices = np.argsort(simplex_values)
    sorted_simplex = [simplex[i] for i in sorted_indices]
    sorted_values = [simplex_values[i] for i in sorted_indices]

    # Return best point
    best_index = np.argmin(simplex_values)
    best_point = simplex[best_index]
    best_value = simplex_values[best_index]
    
    return best_point, best_value

num_parameters = 27
best_point, best_value = nelder_mead(cost_function, rand_cp_arr)
print("Best point:", best_point)
print("Best value:", best_value)
