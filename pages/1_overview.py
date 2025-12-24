import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from streamlit.elements.media import YOUTUBE_RE

asset_price = 100
sigma = 0.2
x_1 = np.arange(0.0, 20, 0.3)
x_2 = np.arange(20, 25, 0.3)


last_value = 10
y_1 = np.array([])
for val in x_1:
    if (last_value >= 5):
        rand = np.random.randint(last_value - 1, last_value + 3)
    else:
        rand=np.random.randint(0, last_value + 3)

    last_value = rand
    y_1 = np.append(y_1, rand)

fig1, ax = plt.subplots()

ax.plot(x_1, y_1,)


#y_2 = last_value + np.sin(sigma * np.pi*5 * x_2)
last_value2 = last_value
y_2 = np.array([])
y_3 = np.array([])
for val in x_2:
    y_2 = np.append(y_2, last_value)
    y_3 = np.append(y_3, last_value2)
    last_value = last_value + sigma
    last_value2 = last_value2 - sigma

ax.plot(x_2, y_2, color="#f5ad42")
ax.plot(x_2, y_3, color="#f5ad42")

st.pyplot(fig1)


