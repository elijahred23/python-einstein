import numpy as numpy
from scipy.constants import c
from sympy import Symbol, Eq, solve, sqrt

v = 0.9 * c

t0 = Symbol('t0', real=True, positive=True)

gamma = 1 / sqrt(1 - (v**2 / c**2))

time_dilation_eq = Eq(gamma, t0)


t_moving = solve(time_dilation_eq, t0)

gamma_value = gamma.evalf(subs={t0:1})

print(f"Speed of the moving observer: {v}")
print(f"Time dilation factor (gamm): {gamma_value}")
print(f"Proper time (stationary observer): 1 second")
print(f"Time for the moving observer: {t_moving[0]:.2f} seconds")