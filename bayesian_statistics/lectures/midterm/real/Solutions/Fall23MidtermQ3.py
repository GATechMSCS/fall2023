# -*- coding: utf-8 -*-
# @Author: Aaron Reding
# @Date:   2023-03-13 03:09:54
# @Last Modified by:   aaronreding
# @Last Modified time: 2023-10-22 21:09:23

import numpy as np
from tqdm.auto import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.style as style
import pandas as pd
from scipy.stats import invgamma


def stats(df):
    style.use("bmh")
    fig, axs = plt.subplots(ncols=3, figsize=(12, 4))

    for i, col in enumerate(df.columns):
        col_mean = df[col].mean()
        col_credible_interval = np.quantile(df[col], [0.025, 0.975])

        print(f"{col}:")
        print(f"\tMean: {col_mean:.3f}")
        print(
            f"\t95% Equitailed Credible Interval: [{col_credible_interval[0]:.3f}",
            f"{col_credible_interval[1]:.3f}]",
        )

        sns.histplot(df[col], ax=axs[i], stat="density")
        axs[i].set_xlabel(col)
        if i != 0:
            axs[i].set_ylabel("")

    fig.savefig("Q3histograms.png")


def norm_var(v2):
    return 1/(1 + (1/v2))


def norm_loc(other_theta, v2, y):
    return (y - other_theta) * norm_var(v2)


def main():
    rng = np.random.default_rng(333)

    burn = 500
    samples = 100000 + burn

    theta1_array = np.zeros(samples)
    theta2_array = np.zeros(samples)
    v2_array = np.zeros(samples)

    # params
    a = b = 10
    y = .5

    # inits
    v2 = 0.5
    theta1 = theta2 = 1


    for i in tqdm(range(samples)):
        theta1 = rng.normal(loc=norm_loc(theta2, v2, y), scale=norm_var(v2) ** 0.5)
        theta1_array[i] = theta1

        theta2 = rng.normal(loc=norm_loc(theta1, v2, y), scale=norm_var(v2) ** 0.5)
        theta2_array[i] = theta2

        ig_scale = 0.5 * (theta1**2 + theta2**2) + b
        v2 = 1 / rng.gamma(shape=a + 1, scale=1 / ig_scale)
        # v2 = invgamma.rvs(a=a + 1, scale=ig_scale) # equivalent
        v2_array[i] = v2

    v2s = v2_array[burn:]
    theta1s = theta1_array[burn:]
    theta2s = theta2_array[burn:]

    results = pd.DataFrame(
        {"$\\nu_2$": v2_array, "$\\theta_1$": theta1_array, "$\\theta_2$": theta2_array}
    )

    stats(results)


if __name__ == "__main__":
    main()
