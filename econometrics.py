import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Custom CSS for styling the app (Pink background and white text)
st.markdown("""
    <style>
    body {
        background-color: #FFCCE5;
        color: white;
    }
    h1, h2, h3 {
        color: white;
    }
    .stButton>button {
        background-color: #FF77B9;
        color: white;
        font-weight: bold;
    }
    .stSlider>div>div>input {
        background-color: #FF77B9;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Header
st.title("Femme Finance")
st.header("The Future of Finance is Female")

# Portfolio Data (Simulated)
portfolio_data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Portfolio Value (€)": [1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200],
}

df_portfolio = pd.DataFrame(portfolio_data)

# Portfolio Amount Display
current_portfolio_value = df_portfolio["Portfolio Value (€)"].iloc[-1]
st.subheader(f"Current Portfolio Value: €{current_portfolio_value}")

# Investment Simulations Section
st.write("### Investment Simulations")
st.write("""
Simulate different investment strategies and see how they could impact your portfolio. Use sliders to adjust your risk level and monthly contributions.
""")

# Investment Risk and Monthly Contributions
risk_level = st.slider("Risk Level (1 = Low, 10 = High)", min_value=1, max_value=10, value=5)
monthly_contribution = st.slider("Monthly Contribution (€)", min_value=0, max_value=1000, value=200)

# Simulate Portfolio Growth Based on Input
simulated_growth = df_portfolio["Portfolio Value (€)"].copy()
for i in range(1, len(simulated_growth)):
    # Apply simulated growth based on risk and monthly contribution
    growth_factor = 1 + (risk_level / 1000)
    simulated_growth[i] = simulated_growth[i-1] * growth_factor + monthly_contribution

# Plot Simulated Growth
st.write("### Simulated Portfolio Growth (Based on Risk and Contributions)")
fig2, ax2 = plt.subplots()
ax2.plot(df_portfolio["Month"], simulated_growth, marker='x', color='#FF77B9')
ax2.set_title("Simulated Portfolio Growth", fontsize=14, color='white')
ax2.set_xlabel("Month", fontsize=12, color='white')
ax2.set_ylabel("Portfolio Value (€)", fontsize=12, color='white')
ax2.tick_params(axis='x', labelcolor='white')
ax2.tick_params(axis='y', labelcolor='white')
st.pyplot(fig2)

# Progress Tracker Section
st.write("### Progress Tracker")
st.write("""
Track your financial progress and set your financial goals. Stay motivated by measuring your growth!
""")
goal_value = st.slider("Set Your Investment Goal (€)", min_value=1000, max_value=10000, value=5000)
progress = (current_portfolio_value / goal_value) * 100

# Make sure progress doesn't exceed 100
progress = min(progress, 100)

# Display Progress Bar
st.write(f"Your current progress towards your goal: {progress:.2f}%")
st.progress(progress / 100)  # Pass the value as a float between 0.0 and 1.0

# Market News Section
st.write("### Market News")
st.write("""
Stay informed with the latest market trends. Here's a glimpse of what's happening in the financial world:
""")
# Example market news (static data for now)
market_news = [
    "Dow tumbles 10000 points, wiping out a chunk of Wednesday's historic rally: Live Updates",
    "Stocks Plunge as US-China Trade Tensions Deepen",
    "European stocks close 3.5% lower as Trump tariffs take effect,China and EU retaliate",
    "NASDAQ Soars to Best Day Since 2001 After Trumo Pauses Some Tariffs"
]

for news_item in market_news:
    st.write(f"- {news_item}")

# Educational Content Section
st.write("### Educational Content")
st.write("""
Learn about different investment options and strategies to grow your wealth. Here are some resources:
""")
st.write("""
- **Investing Basics**: Learn the fundamentals of investing, such as stocks, bonds, and ETFs.
- **Risk Management**: Understand how to assess risk and make educated investment choices.
- **Investment Strategies for Beginners**: Step-by-step guides to start your investment journey with confidence.
- **Long-Term Growth vs Short-Term Gains**: What you need to know about time horizons and market volatility.
""")

# Footer
st.write("### Empowering Women to Take Control of Their Financial Future")
import streamlit as st

# Display an image from a URL
st.image("https://www.istockphoto.com/photo/online-investment-winner-rich-woman-and-money-earning-gm1369340285-439118338", caption="Image from URL",  use_container_width =True)
