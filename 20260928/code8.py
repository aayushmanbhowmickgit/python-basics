import matplotlib.pyplot as plt
import numpy as np

# 1. Define the x-axis range (from -10 to 10 with 400 points for smoothness)
x = np.linspace(-10, 10, 400)

# 2. Define the mathematical function
y = (x**2) * np.sin(x)

# 3. Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r"$f(x) = x^2 \sin(x)$", color="royalblue", linewidth=2)

# 4. Add labels, grid, and styling
plt.title("Plot of the Function $f(x) = x^2 \\sin(x)$", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("f(x)", fontsize=12)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # X-axis line
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")  # Y-axis line
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(fontsize=12)

# 5. Display the graph
plt.show()
