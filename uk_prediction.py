import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

from numba import njit

data = np.loadtxt("uk.txt")

def SIR(t, beta, gamma):
    # Total population, N.
    N = 600000 # UK approx. 6x Wuhan population
    # Initial number of infected and recovered individuals, I0 and R0.
    I0, R0 = 9, 0
    # Everyone else, S0, is susceptible to infection initially.
    S0 = N - I0 - R0

    # The SIR model differential equations.
    @njit
    def deriv(y, t, N, beta, gamma):
        S, I, R = y
        dSdt = -beta * S * I / N
        dIdt = beta * S * I / N - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt

    # Initial conditions vector
    y0 = S0, I0, R0
    # Integrate the SIR equations over the time grid, t.
    ret = odeint(deriv, y0, t, args=(N, beta, gamma))
    S, I, R = ret.T
    return I


day = np.arange(0, len(data), 1)
days = np.arange(0, len(data)+10, 1)

beta, gamma = [0.33838125, 0.06476182]

plt.figure(0)
plt.scatter(day, data,marker="x",c="r",label="Data")
plt.plot(days, SIR(days, beta, gamma),label="Wuhan model")
plt.savefig("UK_prediction")
plt.legend()
plt.title("UK Prediction")
plt.show()
