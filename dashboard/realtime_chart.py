import matplotlib.pyplot as plt
import random

methane_levels = [random.randint(200, 600) for _ in range(10)]

time = list(range(10))

plt.plot(time, methane_levels)
plt.xlabel('Time')
plt.ylabel('Methane Level (ppm)')
plt.title('Methane Trend Analysis')
plt.grid(True)
plt.show()