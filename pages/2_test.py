import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


P0 = 100
P_target = 110
strike_price = 120
n_days = 100
# volatility per day
sigma = 0.02
t = 0.4

# Calculate the required total log return -> also used in Black-Scholes
total_log_return = np.log(P_target / P0)

log_returns = np.random.normal(0, sigma, n_days)

sum_log_returns = np.sum(log_returns)

log_returns_corrected = log_returns * (total_log_return / sum_log_returns)

prices = P0 * np.exp(np.cumsum(log_returns_corrected))

fig, ax = plt.subplots()
ax.plot(prices)
ax.set_title("Simulierter Aktienkurs")
ax.set_xlabel("Zeit")
ax.set_ylabel("Preis")




# strike price line
ax.axhline(y=strike_price, color='r', linestyle='--')

st.pyplot(fig)
