from altair.utils.core import T
import streamlit as st


st.title("Black Scholes Modell", text_alignment= "center")

st.caption("The Black Scholes model is a mathematical framework used to determine the fair price of European call and put options by modeling the underlying asset price as a stochastic process with constant volatility and a constant risk-free interest rate.")

st.latex("S_{ t }N(d_{ 1 }) - Ke^{-rt}N(d_{ 2 })")



st.subheader("Structure and explaination of the formula:", text_alignment= "center")
st.markdown("**A** = current asset price  \n**K** = strike price  \n**r** = risk-free interest rate  \n**sigma($\sigma$)** = volatility  \n**t** = time to maturity (years)  \n**rd** = return", text_alignment= "center")

col1, col2 = st.columns(2, border=True)

with col1:
    st.latex(r"d_1 = \frac{ ln(\frac{ A }{ K })+(r+\frac{ \sigma^{ 2 } }{ 2 })(t) }{ \sigma\sqrt{ t } }")
    st.markdown("the probability that the option will be exercised", text_alignment= "center")

    

with col2:
    st.latex(r"d_2 = \frac{ ln(\frac{ A }{ K })+(r-\frac{ \sigma^{ 2 } }{ 2 })(t) }{ \sigma\sqrt{ t } }")
    st.markdown("the probability that the strike price will be reached at expiration", text_alignment= "center")

    st.space(size="small")
    st.markdown("**The formula is divided into three parameters:**", text_alignment= "center")
    st.markdown("1. the requiered return  \n2. the expected return  \n3. the standard deviation")


    st.space(size="small")
    st.markdown("the requiered return:", text_alignment= "center")
    st.latex(r"A*e^{ rd } = K")
    st.latex(r"e^{ rd } = \frac{ K }{ A }")
    st.latex(r"rd = ln\left( \frac{ K }{ A } \right)")

    st.space(size="small")
    st.markdown("the expected return:", text_alignment= "center")
    st.latex(r"\left( r-\frac{ \sigma^2 }{ 2 } \right)\left( t \right)")
    st.markdown("Note:  \nInterest rates drive growth; fluctuations reduce growth; time amplifies both", text_alignment= "center") 