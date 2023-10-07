import numpy as np
import matplotlib.pyplot as plt


#Constanst
c = 299792458 # Speed of light in meters per second
v = np.linspace(0, 0.99*c, 100) # Array of relative velocities from 0 to 0.99c
earth_time = 1 # Years (1 year for the twin on Earth)


# Calculate time dilation and age difference for different velocities
gamma = 1 / np.sqrt(1 - (v**2/c**2)) # Lorentz factor 
traveler_time = earth_time / gamma # Time experienced by the traveling twin
age_difference = earth_time - traveler_time

# Create a plot
plt.figure(figsize=(8,6))
plt.plot(v/c, age_difference)
plt.title("Age Difference vs. Relative Velocity")
plt.xlabel("Relative Velocity (c)")
plt.ylabel("Age Difference (years)")

# Save the plot as an image file
plt.savefig("twin_paradox_plot.png")

# Display the plot
plt.show()