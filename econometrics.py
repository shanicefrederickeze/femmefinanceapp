import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and Introduction
st.title("Femme Finance")
st.header("Empowering Women to Take Charge of Their Finances")
st.write("""
This app helps you track your savings, understand your financial habits, and plan for a brighter future.
Let's start by calculating your monthly savings!
""")

# Input Fields for Financial Information
income = st.number_input("Monthly Income (€)", min_value=0, step=100)
expenses = st.number_input("Monthly Expenses (€)", min_value=0, step=100)

# Calculate Savings
savings = income - expenses
st.subheader(f"Your Monthly Savings: €{savings}")

# Display Financial Tips
st.write("### Financial Tips:")
st.write("""
- **Track Your Spending**: Make sure to track where your money is going to help make better spending decisions.
- **Start Budgeting**: Create a monthly budget to help allocate funds toward savings.
- **Emergency Fund**: Aim to save 3–6 months of living expenses for emergencies.
- **Invest for the Future**: Consider long-term investments like stocks or retirement accounts.
""")

# Chart: Savings Progress Over Time
st.write("### Savings Progress Chart")

# Generate Random Savings Data (for demo purposes)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
random_savings = [savings + (i * 50) for i in range(12)]  # Increment savings by €50 each month for demo

# Create DataFrame
df = pd.DataFrame({"Month": months, "Savings (€)": random_savings})

# Plot the savings
fig, ax = plt.subplots()
ax.plot(df["Month"], df["Savings (€)"], marker='o')
ax.set_title("Savings Progress Over Time")
ax.set_xlabel("Month")
ax.set_ylabel("Savings (€)")
plt.xticks(rotation=45)
st.pyplot(fig)

# Contact Section for Users to Reach Out
st.write("### Contact Femme Finance")
st.write("Have any questions? Reach out to us via email at femmefinance@yourdomain.com.")

# Customize as Needed for More Features
