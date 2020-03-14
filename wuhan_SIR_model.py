import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from scipy.optimize import curve_fit

from numba import njit

data = np.loadtxt("wuhan.txt")
print(data)

days = np.arange(0,len(data),1)

def SIR(t,beta,gamma):
    # Total population, N.
    N = 100000
    # Initial number of infected and recovered individuals, I0 and R0.
    I0, R0 = 239, 25
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

popt, pcov = curve_fit(SIR,days,data)
print(popt,pcov)

print("R0:",1/popt[0],"Recovery days:",1/popt[1])

plt.figure(0)
plt.scatter(days,data,label="data")
plt.plot(days,SIR(days,*popt),label="SIR fit")
plt.legend()