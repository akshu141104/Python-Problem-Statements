"""Project — "A/B Test Analyzer for a Website"
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

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# -----------------------------
# Input Data
# -----------------------------
visitors_A = 500
conversions_A = 45

visitors_B = 480
conversions_B = 62

# -----------------------------
# Conversion Rates
# -----------------------------
p1 = conversions_A / visitors_A
p2 = conversions_B / visitors_B

print("Conversion Rate A:", round(p1, 4))
print("Conversion Rate B:", round(p2, 4))

# -----------------------------
# Null Hypothesis:
# H0: p1 = p2 (no difference)
# -----------------------------

# -----------------------------
# Z-Test Calculation
# -----------------------------
p_pool = (conversions_A + conversions_B) / (visitors_A + visitors_B)

se = np.sqrt(p_pool * (1 - p_pool) * (1/visitors_A + 1/visitors_B))

z_score = (p2 - p1) / se

# Two-tailed test
p_value = 2 * (1 - norm.cdf(abs(z_score)))

print("\nZ-score:", round(z_score, 4))
print("P-value:", round(p_value, 4))

# -----------------------------
# Confidence Interval (95%)
# -----------------------------
diff = p2 - p1

se_diff = np.sqrt(
    (p1 * (1 - p1)) / visitors_A +
    (p2 * (1 - p2)) / visitors_B
)

z_critical = norm.ppf(0.975)  # 95% CI

margin_error = z_critical * se_diff

ci_lower = diff - margin_error
ci_upper = diff + margin_error

print("\n95% Confidence Interval:")
print("Lower:", round(ci_lower, 4))
print("Upper:", round(ci_upper, 4))

# -----------------------------
# Decision
# -----------------------------
alpha = 0.05

print("\n--- Final Decision ---")

if p_value < alpha:
    print("Reject Null Hypothesis (H0)")
    print("YES ✅: Version B is statistically better")
else:
    print("Fail to Reject Null Hypothesis (H0)")
    print("NO ❌: Difference may be due to random chance")

# -----------------------------
# Visualization
# -----------------------------
labels = ['Version A', 'Version B']
rates = [p1, p2]

plt.bar(labels, rates)
plt.title("A/B Test Conversion Rates")
plt.ylabel("Conversion Rate")
plt.show()

"""
output:
Conversion Rate A: 0.09
Conversion Rate B: 0.1292

Z-score: 1.9653
P-value: 0.0494

95% Confidence Interval:
Lower: 0.0001
Upper: 0.0783

--- Final Decision ---
Reject Null Hypothesis (H0)
YES ✅: Version B is statistically better

"""