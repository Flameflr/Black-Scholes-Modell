import streamlit as st


st.title("Black Scholes Modell")

st.write("The Black Scholes model is a mathematical framework used to determine the fair price of European call and put options by modeling the underlying asset price as a stochastic process with constant volatility and a constant risk-free interest rate.")

st.latex("S_{ t }N(d_{ 1 }) - Ke^{-rt}N(d_{ 2 })")