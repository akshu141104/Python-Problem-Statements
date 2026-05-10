
"""Project — "A/B Test Analyzer for a Website App"
Problem Statement:
A startup ran two versions of their landing page (A and B) for 2 weeks. Version A had 500 visitors, 45 conversions. Version B had 480 visitors, 62 conversions. Is B actually better, or is it just random chance? Build a tool to tell them statistically.
Stack: Python, SciPy, Pandas, Matplotlib
Input: Conversion counts for Group A and Group B
Output: Z-test or T-test result, p-value, confidence interval, YES/NO recommendation
Think about:
What is a null hypothesis here? What are you trying to disprove?
What p-value threshold (alpha) do you use and why 0.05?
What does it mean if p < 0.05 vs p > 0.05 in plain English?
What if sample sizes were very different between A and B?"""
"""



import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

st.title("📊 A/B Test Analyzer")

st.write("Compare two versions of a website and check if B is better statistically.")

# -----------------------------
# User Input
# -----------------------------
st.sidebar.header("Enter Data")

visitors_A = st.sidebar.number_input("Visitors A", value=500)
conversions_A = st.sidebar.number_input("Conversions A", value=45)

visitors_B = st.sidebar.number_input("Visitors B", value=480)
conversions_B = st.sidebar.number_input("Conversions B", value=62)

alpha = st.sidebar.selectbox("Select Significance Level (alpha)", [0.01, 0.05, 0.1], index=1)

# -----------------------------
# Calculation Button
# -----------------------------
if st.button("Analyze A/B Test"):

    # Conversion Rates
    p1 = conversions_A / visitors_A
    p2 = conversions_B / visitors_B

    st.subheader("📈 Conversion Rates")
    st.write(f"Version A: {round(p1, 4)}")
    st.write(f"Version B: {round(p2, 4)}")

    # -----------------------------
    # Z-Test
    # -----------------------------
    p_pool = (conversions_A + conversions_B) / (visitors_A + visitors_B)

    se = np.sqrt(p_pool * (1 - p_pool) * (1/visitors_A + 1/visitors_B))

    z_score = (p2 - p1) / se
    p_value = 2 * (1 - norm.cdf(abs(z_score)))

    st.subheader("🧪 Statistical Test")
    st.write(f"Z-score: {round(z_score, 4)}")
    st.write(f"P-value: {round(p_value, 4)}")

    # -----------------------------
    # Confidence Interval
    # -----------------------------
    diff = p2 - p1

    se_diff = np.sqrt(
        (p1 * (1 - p1)) / visitors_A +
        (p2 * (1 - p2)) / visitors_B
    )

    z_critical = norm.ppf(1 - alpha/2)
    margin_error = z_critical * se_diff

    ci_lower = diff - margin_error
    ci_upper = diff + margin_error

    st.subheader("📏 Confidence Interval")
    st.write(f"Lower: {round(ci_lower, 4)}")
    st.write(f"Upper: {round(ci_upper, 4)}")

    # -----------------------------
    # Decision
    # -----------------------------
    st.subheader("✅ Final Decision")

    if p_value < alpha:
        st.success("Reject H0 → YES: Version B is better 🎉")
    else:
        st.error("Fail to Reject H0 → NO: Difference is not significant")

    # -----------------------------
    # Visualization
    # -----------------------------
    st.subheader("📊 Visualization")

    labels = ['Version A', 'Version B']
    rates = [p1, p2]

    fig, ax = plt.subplots()
    ax.bar(labels, rates)
    ax.set_ylabel("Conversion Rate")
    ax.set_title("A/B Test Result")

    st.pyplot(fig)