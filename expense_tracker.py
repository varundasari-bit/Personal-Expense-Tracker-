import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# STEP 1: Generate Sample Data
# ----------------------------
np.random.seed(42)

categories = ["Food", "Travel", "Shopping", "Bills", "Entertainment"]

data = pd.DataFrame({
    "date": pd.date_range(start="2024-01-01", periods=100),
    "category": np.random.choice(categories, 100),
    "amount": np.random.randint(100, 5000, 100)
})

# Save dataset (so you can show it in repo)
data.to_csv("expenses.csv", index=False)

print("\n📊 Sample Data:")
print(data.head())

# ----------------------------
# STEP 2: Basic Analysis
# ----------------------------
print("\n📈 Total Spending:", data["amount"].sum())

category_spending = data.groupby("category")["amount"].sum()
print("\n💸 Spending by Category:\n", category_spending)

# ----------------------------
# STEP 3: Monthly Trend
# ----------------------------
data["month"] = data["date"].dt.to_period("M")

monthly_spending = data.groupby("month")["amount"].sum()

print("\n📅 Monthly Spending:\n", monthly_spending)

# ----------------------------
# STEP 4: Visualization
# ----------------------------
plt.figure()
category_spending.plot(kind="bar")
plt.title("Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("category_spending.png")

plt.figure()
monthly_spending.plot(kind="line")
plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("monthly_trend.png")

print("\n✅ Charts saved as images.")

# ----------------------------
# STEP 5: Insights (Basic)
# ----------------------------
top_category = category_spending.idxmax()
print(f"\n🔥 Highest spending category: {top_category}")

avg_spending = data["amount"].mean()
print(f"💡 Average expense: {avg_spending:.2f}")
