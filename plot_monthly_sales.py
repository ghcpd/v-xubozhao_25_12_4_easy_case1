import json
from pathlib import Path
import matplotlib.pyplot as plt


def load_data(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def make_plots(data, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)

    months = [d['Month'] for d in data]
    sales = [d['Sales'] for d in data]

    # Line chart
    plt.figure(figsize=(10, 5))
    plt.plot(months, sales, marker='o', linewidth=2, color='#1f77b4')
    plt.title('Monthly Sales — Line Chart')
    plt.xlabel('Month')
    plt.ylabel('Sales (USD)')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    line_path = out_dir / 'monthly_sales_line.png'
    plt.savefig(line_path)
    plt.close()

    # Bar chart
    plt.figure(figsize=(10, 5))
    bars = plt.bar(months, sales, color='#ff7f0e', edgecolor='black')
    plt.title('Monthly Sales — Bar Chart')
    plt.xlabel('Month')
    plt.ylabel('Sales (USD)')
    plt.grid(axis='y', alpha=0.3)

    # Add value labels on top of bars
    for b in bars:
        h = b.get_height()
        plt.annotate(f'{h:,}', xy=(b.get_x() + b.get_width() / 2, h),
                     xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    bar_path = out_dir / 'monthly_sales_bar.png'
    plt.savefig(bar_path)
    plt.close()

    return line_path, bar_path


def main():
    base = Path(__file__).parent
    data_file = base / 'monthl_sales.json'
    out_dir = base / 'plots'

    data = load_data(data_file)
    line, bar = make_plots(data, out_dir)

    print('Saved line chart to:', line)
    print('Saved bar chart to:', bar)


if __name__ == '__main__':
    main()
