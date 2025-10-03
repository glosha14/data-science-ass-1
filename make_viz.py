import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "month": ["07/2019", "08/2019", "09/2019", "10/2019", "11/2019"],
    "Searches": [50, 53, 59, 56, 62],
    "Direct":    [39, 47, 42, 51, 51],
    "Social Media": [70, 80, 90, 87, 92]
}
df = pd.DataFrame(data)

# Create figure
fig, ax = plt.subplots(figsize=(9,5))
x = range(len(df))
width = 0.25

# Colors
colors = {"Searches": "#1f77b4", "Direct": "#e377c2", "Social Media": "#ff7f0e"}

# Bars
bars1 = ax.bar([p - width for p in x], df["Searches"], width, label="Searches", color=colors["Searches"])
bars2 = ax.bar(x, df["Direct"], width, label="Direct", color=colors["Direct"])
bars3 = ax.bar([p + width for p in x], df["Social Media"], width, label="Social Media", color=colors["Social Media"])

# Add value labels above bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 1, f"{height}",
                ha="center", va="bottom", fontsize=9, fontweight="bold")

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

# Axis labels and title
ax.set_xticks(x)
ax.set_xticklabels(df["month"])
ax.set_ylabel("visitors in thousands", fontweight="bold")
ax.set_xlabel("months", fontweight="bold")
ax.set_title("Visitors by web traffic sources", fontweight="bold")

# Legend at the bottom
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=3)

plt.tight_layout()
plt.savefig("visitors_by_source.png", dpi=150, bbox_inches="tight")
plt.show()
