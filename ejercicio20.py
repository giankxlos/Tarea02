import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
plt.plot(x, np.sin(x), 'y', label='Seno')
plt.plot(x, np.cos(x), 'b--', label='Coseno')
plt.title('Seno y Coseno')
plt.legend()
plt.show()