import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Define symbolic variables
v, c, L0, L = sp.symbols('v c L0 L')

# Length contraction formula
L_contracted = L0 / sp.sqrt(1 - (v**2 / c**2))

# Define values for the speed of light (c), original length (L0), and velocity (v)
c_value = 3e8  # meters per second (speed of light)
L0_value = 1.0  # meters (original length)

# Create a lambda function to evaluate the contracted length numerically
contracted_length_func = sp.lambdify(v, L_contracted.subs({c: c_value, L0: L0_value}), modules=["numpy"])

# Define a range of velocities
velocities = np.linspace(0, 0.99, 100) * c_value

# Calculate the contracted lengths for these velocities
contracted_lengths = [contracted_length_func(v) for v in velocities]

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(velocities / c_value, contracted_lengths, label='Contracted Length')
plt.xlabel('Velocity (v/c)')
plt.ylabel('Contracted Length (L)')
plt.title('Length Contraction in Special Relativity')
plt.grid()
plt.legend()

# Save the plot as an image file (e.g., PNG)
plt.savefig('length_contraction_plot.png')

# Display a message indicating where the file was saved
print('Plot saved as length_contraction_plot.png')

# Show the plot (optional, you can comment this line out if you don't want to display the plot)
plt.show()

