import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.style.use("seaborn-darkgrid")


params = [0.5, 1, 2, 3]
theta = np.linspace(0, 1, 100)

fig, ax = plt.subplots(len(params), len(params), sharex=True, sharey=True)

for i, alpha in enumerate(params):
    for j, beta in enumerate(params):
        # draw lines
        y = stats.beta(alpha, beta).pdf(theta)
        ax[i, j].plot(theta, y)

        # draw legend
        ax[i, j].plot(0, 0, label=f"$\\alpha={alpha}$", alpha=0)
        ax[i, j].plot(0, 0, label=f"$\\beta={beta}$", alpha=0)
        ax[i, j].legend(fontsize=12)

fig.text(0.5, 0.04, "$\\theta$", ha="center")
fig.text(0.04, 0.5, "$PDF$", va="center", rotation="vertical")

plt.show()
