import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.style.use("seaborn-darkgrid")

n_params = [1, 2, 4]
theta_params = [0.25, 0.5, 0.75]

x = np.arange(max(n_params) + 1)

fig, ax = plt.subplots(len(n_params), len(theta_params), sharex=True, sharey=True)

for i, n in enumerate(n_params):
    for j, theta in enumerate(theta_params):
        # draw lines
        y = stats.binom(n=n, p=theta).pmf(x)
        ax[i, j].vlines(x, 0, y, colors="b", lw=5)

        # draw legend
        ax[i, j].plot(0, 0, label=f"$n={n}$", alpha=0)
        ax[i, j].plot(0, 0, label=f"$\\theta={theta}$", alpha=0)
        ax[i, j].legend(fontsize=12)

        # draw tick mark
        ax[i, j].set_ylim(0, 1)

ax[2, 1].set_xlabel("$y$")
ax[1, 0].set_ylabel("$p(y|\\theta)$")
ax[0, 0].set_xticks(x)

plt.show()
