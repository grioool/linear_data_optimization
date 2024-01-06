import numpy as np
from scipy.optimize import linprog


class LinearOptimizationProblems:
    def __init__(self):
        self.c1 = np.array([-1, -2])
        self.c2 = np.array([-20, -12, -40, -25])

        self.a1 = np.array([[2, 1], [-4, 5], [-1, -2], [-1, -5]])  # Problem 1
        self.a2 = np.array([[1, 1, 1, 1], [3, 2, 1, 0], [1, 2, 3, 3]])  # Problem 2

        self.b1 = np.array([20, 10, 2, -15])  # Problem 1
        self.b2 = np.array([50, 100, 90])  # Problem 2

        self.bounds1 = [(0, None), (0, None)]  # Problem 1
        self.bounds2 = [(0, None), (0, None), (0, None), (0, None)]  # Problem 2

    def solve(self):
        # Solve Problem 1
        result1 = linprog(self.c1, A_ub=self.a1, b_ub=self.b1, bounds=self.bounds1, method='highs')
        x, y = result1.x
        z_max = -result1.fun

        # Solve Problem 2
        result2 = linprog(self.c2, A_ub=self.a2, b_ub=self.b2, bounds=self.bounds2, method='highs')
        solution2 = result2.x
        max_profit2 = -result2.fun

        return (x, y, z_max), (solution2, max_profit2)


optimization_problems = LinearOptimizationProblems()
problem1_solution, problem2_solution = optimization_problems.solve()

if problem1_solution and problem2_solution:
    print("Problem 1 Solution:")
    print(f"x = {problem1_solution[0]:.2f}, y = {problem1_solution[1]:.2f}, Max z = {problem1_solution[2]:.2f}\n")

    print("Problem 2 Solution:")
    print(f"x1 = {problem2_solution[0][0]:.2f}, x2 = {problem2_solution[0][1]:.2f}, "
          f"x3 = {problem2_solution[0][2]:.2f}, x4 = {problem2_solution[0][3]:.2f}, "
          f"Max Profit = {problem2_solution[1]:.2f}")
else:
    print("No solution found.")
