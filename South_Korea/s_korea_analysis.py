import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
from scipy.integrate import odeint
from numba import njit

data = np.loadtxt("s_korea.txt")

data = data[5:35]

days = np.arange(0, len(data), 1)

def SIR(t, beta, gamma):
    # Total population, N.
    N = 100000 * 42/11  # S Korea has 51m population, wuhan has 11m
    # Initial number of infected and recovered individuals, I0 and R0.
    I0, R0 = data[0], 0
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

popt, pcov = curve_fit(SIR, days, data)
print(popt, pcov)

print("R0:", 1/popt[0], "Recovery days:", 1/popt[1])

plt.figure(0)
plt.scatter(days, data, label="data")
plt.plot(days, SIR(days, *popt), label="SIR fit")
plt.legend()
plt.title("S Korea SIR model")
plt.xlabel("Days")
plt.ylabel("Infected cases")
plt.savefig("s_korea_model")
plt.show()