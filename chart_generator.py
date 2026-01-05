import json
import matplotlib.pyplot as plt

# Load the data
with open('monthl_sales.json', 'r') as f:
    data = json.load(f)

# Extract months and sales
months = [item['Month'] for item in data]
sales = [item['Sales'] for item in data]

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Line Chart
ax1.plot(months, sales, marker='o', linewidth=2, markersize=8, color='#2E86AB')
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Sales ($)', fontsize=12)
ax1.set_title('Monthly Sales - Line Chart', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.set_ylim(10000, 24000)

# Bar Chart
ax2.bar(months, sales, color='#A23B72', alpha=0.8, edgecolor='black', linewidth=1.2)
ax2.set_xlabel('Month', fontsize=12)
ax2.set_ylabel('Sales ($)', fontsize=12)
ax2.set_title('Monthly Sales - Bar Chart', fontsize=14, fontweight='bold')
ax2.set_ylim(10000, 24000)
ax2.grid(True, alpha=0.3, axis='y')

# Adjust layout and display
plt.tight_layout()
plt.savefig('monthly_sales_charts.png', dpi=300, bbox_inches='tight')
print("Charts saved as 'monthly_sales_charts.png'")
plt.show()
