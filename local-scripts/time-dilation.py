import numpy as np
from scipy.constants import c
from sympy import Symbol, Eq, solve, sqrt

# Define the speed of the moving observer relative to the stationary observer
v = 0.8 * c  # 80% of the speed of light

# Define the stationary observer's time (proper time)
t0 = Symbol('t0', real=True, positive=True)

# Define the time dilation equation
gamma = 1 / sqrt(1 - (v**2 / c**2))
time_dilation_eq = Eq(gamma, t0)

# Solve for the moving observer's time
t_moving = solve(time_dilation_eq, t0)

# Calculate the time dilation factor (gamma)
gamma_value = gamma.evalf(subs={t0: 1})

# Print the results
print(f"Speed of the moving observer: {v}")
print(f"Time dilation factor (gamma): {gamma_value}")
print(f"Proper time (stationary observer): 1 second")
print(f"Time for the moving observer: {t_moving[0]:.2f} seconds")
