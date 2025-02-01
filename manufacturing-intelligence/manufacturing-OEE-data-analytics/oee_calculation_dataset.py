import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter

#dataset
df = pd.read_csv("C:/Users/zahra/Documents/Python-project/Train/OEE/oee_calculation_dataset.csv")
print(df.head(10))

#calculate availability, performance, and quality
df["Availability"] = df["Uptime (minutes)"] / (df["Uptime (minutes)"] + df["Downtime (minutes)"])
df["performance"] = df["Ideal Cycle Time (seconds)"] / df["Actual Cycle Time (seconds)"]
df["Quality"] = (df["Total Units Produced"] - df["Defective Units"]) / df["Total Units Produced"]

#calculate OEE
df["OEE"] = df["Availability"] * df["performance"] * df["Quality"]

#visualize OEE trends
sns.set(style="whitegrid")

plt.figure(figsize=(14, 7))
ax = sns.lineplot(data=df, x="Date", y="OEE", hue="Machine ID", marker="o")
plt.title("OEE Over Time by Machine", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("OEE (%)", fontsize=12)
ax.xaxis.set_major_formatter(DateFormatter("%b %d"))  # dates to month
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

#visualize average OEE by machine
plt.figure(figsize=(8,5))
sns.barplot(data=df, x="Machine ID", y="OEE", estimator="mean", ci=None)
plt.title("Average OEE by Machine", fontsize=16)
plt.xlabel("Machine ID", fontsize=12)
plt.ylabel("Average OEE (%)", fontsize=12)
plt.tight_layout()
plt.show()


#visualize OEE distribution by machine
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Machine ID", y="OEE")
plt.title("OEE Distribution by Machine", fontsize=16)
plt.xlabel("Machine ID", fontsize=12)
plt.ylabel("OEE (%)", fontsize=12)
plt.tight_layout()
plt.show()

#summary statistics
print("OEE Suammary Statistics:")
print(df["OEE"].describe())

#machines with low OEE
low_oee_threshold = 0.6  # Define a threshold for low OEE
low_oee_machines = df[df["OEE"] < low_oee_threshold]
print("\nMachines with Low OEE (< 60%):")
print(low_oee_machines[["Machine ID", "Date", "OEE"]])