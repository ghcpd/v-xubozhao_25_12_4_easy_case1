import json
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Paths
BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "monthl_sales.json"
LINE_OUT = BASE_DIR / "sales_line_chart.png"
BAR_OUT = BASE_DIR / "sales_bar_chart.png"

# Load data
with open(DATA_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Ensure month order
month_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)
df = df.sort_values('Month')

# Line chart
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['Month'], df['Sales'], marker='o', linewidth=2, color='#1f77b4')
ax.set_title('Monthly Sales (Line Chart)', fontsize=14, fontweight='bold')
ax.set_xlabel('Month')
ax.set_ylabel('Sales ($)')
ax.grid(alpha=0.3)

# Annotate max point
max_idx = df['Sales'].idxmax()
ax.annotate(f"${df.loc[max_idx,'Sales']:,.0f}",
            xy=(df.loc[max_idx,'Month'], df.loc[max_idx,'Sales']),
            xytext=(0, 8), textcoords='offset points', ha='center', fontsize=9, fontweight='bold')

plt.tight_layout()
fig.savefig(LINE_OUT, dpi=150)
plt.close(fig)

# Bar chart
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df['Month'], df['Sales'], color='#ff7f0e')
ax.set_title('Monthly Sales (Bar Chart)', fontsize=14, fontweight='bold')
ax.set_xlabel('Month')
ax.set_ylabel('Sales ($)')
ax.grid(axis='y', alpha=0.3)

# Add value labels
for i, val in enumerate(df['Sales']):
    ax.text(i, val + 300, f"${val:,}", ha='center', fontsize=9)

plt.tight_layout()
fig.savefig(BAR_OUT, dpi=150)
plt.close(fig)

print(f"Saved charts:\n - {LINE_OUT}\n - {BAR_OUT}")
