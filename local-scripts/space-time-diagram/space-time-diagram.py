import matplotlib.pyplot as plt
import numpy as np

# Define the speed of light (c) and the original length (L0)
c = 3e8  # meters per second (speed of light)
L0 = 1.0  # meters (original length)

# Define the object's velocity relative to the speed of light (v)
v = 0.8 * c  # 80% of the speed of light

# Create an array of time values
time = np.linspace(0, 1.5, 100)  # seconds

# Calculate the corresponding contracted length at each time
contracted_length = L0 / np.sqrt(1 - (v**2 / c**2))

# Create a spacetime diagram
plt.figure(figsize=(10, 6))
plt.plot(time, time * v, label='Worldline (Proper Time)')
plt.axhline(y=L0, color='red', linestyle='--', label='Rest Length (L0)')
plt.axvline(x=contracted_length, color='green', linestyle='--', label='Contracted Length (L)')
plt.xlabel('Time (s)')
plt.ylabel('Space (m)')
plt.title('Spacetime Diagram in Special Relativity')
plt.grid()
plt.legend()

# Save the plot as an image file (e.g., PNG)
plt.savefig('spacetime_diagram.png')

# Display a message indicating where the file was saved
print('Spacetime diagram saved as spacetime_diagram.png')
