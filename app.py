from altair.utils.core import T
import streamlit as st


st.title("Black Scholes Modell", text_alignment= "center")

st.caption("The Black Scholes model is a mathematical framework used to determine the fair price of European call and put options by modeling the underlying asset price as a stochastic process with constant volatility and a constant risk-free interest rate.")

st.latex("S_{ t }N(d_{ 1 }) - Ke^{-rt}N(d_{ 2 })")



st.subheader("Structure and explaination of the formula:", text_alignment= "center")
st.markdown("**A** = current asset price  \n**K** = strike price  \n**r** = risk-free interest rate  \n**sigma($\sigma$)** = volatility  \n**t** = time to maturity (years)  \n**rd** = return", text_alignment= "center")

col1, col2 = st.columns(2, border=True)

with col2:
    st.space(size="small")
    st.latex(r"d_1 = \frac{ ln(\frac{ A }{ K })+(r+\frac{ \sigma^{ 2 } }{ 2 })(t) }{ \sigma\sqrt{ t } }")
    st.markdown("the probability that the option will be exercised", text_alignment= "center")

    st.space(size="small")
    st.markdown("**The formula is divided into two parameters:**", text_alignment= "center")
    st.markdown("1.probability option ends in the money  \n2. probability how far option ends in the money")
    st.caption("to understand the formula, you need to understand the structure from $d_2$", text_alignment= "center")

    st.space(size="small")
    st.markdown("<u>probability option ends in the money:</u>", text_alignment= "center", unsafe_allow_html=True)
    st.markdown("follows from $d_2$", text_alignment= "center")

    st.space(size="small")
    st.markdown("<u>probability how far option ends in the money:</u>", text_alignment= "center", unsafe_allow_html=True)
    st.markdown("Is indicated by the addition of the standard deviation instead of the subtraction in $d_2$", text_alignment= "center")
    st.latex(r"d_1 = \left( r+\frac{ \sigma^2 }{ 2 } \right)")
    st.latex(r"d_2 = \left( r-\frac{ \sigma^2 }{ 2 } \right)")
    st.markdown("The reason behind this is, that the option holder benefits from positive price movements, if the strike price gets reached. Which increases the value of the option and consequently the option-price", text_alignment= "center")

with col1:
    st.space(size="small")
    st.latex(r"d_2 = \frac{ ln(\frac{ A }{ K })+(r-\frac{ \sigma^{ 2 } }{ 2 })(t) }{ \sigma\sqrt{ t } }")
    st.markdown("the probability that the strike price will be reached at expiration", text_alignment= "center")

    st.space(size="small")
    st.markdown("**The formula is divided into three parameters:**", text_alignment= "center")
    st.markdown("1. the requiered return  \n2. the expected return  \n3. the standard deviation")


    st.space(size="small")
    st.markdown("<u>the requiered return:</u>", text_alignment= "center", unsafe_allow_html=True)
    st.latex(r"A*e^{ rd } = K")
    st.latex(r"e^{ rd } = \frac{ K }{ A }")
    st.latex(r"rd = ln\left( \frac{ K }{ A } \right)")

    st.space(size="small")
    st.markdown("<u>the expected return:</u>", text_alignment= "center", unsafe_allow_html=True)
    st.latex(r"\left( r-\frac{ \sigma^2 }{ 2 } \right)\left( t \right)")
    st.markdown("Note:  \nInterest rates drive growth; fluctuations reduce growth; time amplifies both", text_alignment= "center")

    st.space(size="small")
    st.markdown("<u>the standard deviation:</u>", text_alignment= "center", unsafe_allow_html=True)
    st.latex(r"\sigma\sqrt{ t }")
    st.markdown("counts the standard deviations over time", text_alignment= "center")
    st.caption("Since the Gaussian bell curve is defined with a standard deviation of one, this division allows the formula to be used for all stocks", text_alignment= "center")
    
    st.space(size="small")
    st.markdown("Put together, the formula looks like this:", text_alignment= "center")
    st.latex(r"\frac{ ln(\frac{ K }{ A })-(r-\frac{ \sigma^{ 2 } }{ 2 })(t) }{ \sigma\sqrt{ t } }")
    st.markdown("But this doesn't equal with the formula at the top", text_alignment= "center")
    st.markdown("Since the normal distribution is defined from negative infinity and the normal distribution has the property of being symmetrical, a sign change can be made to calculate the standard deviation to the right of the curve", text_alignment="center")
    st.latex(r"-\left(\frac{ ln(\frac{ K }{ A })-(r-\frac{ \sigma^{ 2 } }{ 2 })(t) }{ \sigma\sqrt{ t } }\right)")
    st.latex(r"= -\frac{ ln(K)-ln(A)-(r-\frac{ \sigma^{ 2 } }{ 2 })(t) }{ \sigma\sqrt{ t } }")
    st.latex(r"= \frac{ -ln(K)+ln(A)+(r-\frac{ \sigma^{ 2 } }{ 2 })(t) }{ \sigma\sqrt{ t } }")
    st.latex(r"= \frac{ ln(\frac{ A }{ K })+(r-\frac{ \sigma^{ 2 } }{ 2 })(t) }{ \sigma\sqrt{ t } }")