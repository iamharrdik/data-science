import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Sales Dashboard")
st.markdown("Data Science Dashboard using Python and Streamlit")

# Load Data
df = pd.read_csv("sales.csv")

# Sidebar
st.sidebar.header("Filters")
month = st.sidebar.selectbox(
    "Select Month",
    ["All"] + list(df["Month"])
)

# Filter Data
if month != "All":
    filtered_df = df[df["Month"] == month]
else:
    filtered_df = df

# Display Data
st.subheader("Dataset")
st.dataframe(filtered_df)

# Metrics
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Sales",
    f"{filtered_df['Sales'].sum()}"
)

col2.metric(
    "Total Profit",
    f"{filtered_df['Profit'].sum()}"
)

col3.metric(
    "Average Sales",
    f"{filtered_df['Sales'].mean():.2f}"
)

# Line Chart
st.subheader("Sales Trend")

fig1, ax1 = plt.subplots(figsize=(8,4))
ax1.plot(
    df["Month"],
    df["Sales"],
    marker="o"
)
ax1.set_title("Monthly Sales")
ax1.set_xlabel("Month")
ax1.set_ylabel("Sales")
st.pyplot(fig1)

# Bar Chart
st.subheader("Profit Analysis")

fig2, ax2 = plt.subplots(figsize=(8,4))
ax2.bar(
    df["Month"],
    df["Profit"]
)
ax2.set_title("Monthly Profit")
ax2.set_xlabel("Month")
ax2.set_ylabel("Profit")
st.pyplot(fig2)

# Statistics
st.subheader("Statistical Summary")
st.write(df.describe())

# Download Data
st.subheader("Download Dataset")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="sales_data.csv",
    mime="text/csv"
)

# Footer
st.markdown("---")
st.markdown("Created using Python, Pandas, Matplotlib and Streamlit")