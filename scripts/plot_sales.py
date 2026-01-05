from pathlib import Path
import json
import matplotlib.pyplot as plt


def load_data(json_path: Path):
    with json_path.open('r', encoding='utf-8') as f:
        data = json.load(f)
    months = [row['Month'] for row in data]
    sales = [row['Sales'] for row in data]
    return months, sales


def ensure_output_dir(out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)


def plot_line(months, sales, out_path: Path):
    plt.figure(figsize=(10, 5))
    plt.plot(months, sales, marker='o', linewidth=2)
    plt.title('Monthly Sales — Line Chart')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def plot_bar(months, sales, out_path: Path):
    plt.figure(figsize=(10, 5))
    bars = plt.bar(months, sales, color='#4c72b0')
    plt.title('Monthly Sales — Bar Chart')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def main():
    repo_root = Path(__file__).resolve().parents[1]
    json_path = repo_root / 'monthl_sales.json'
    out_dir = repo_root / 'output'
    ensure_output_dir(out_dir)

    months, sales = load_data(json_path)

    line_path = out_dir / 'line_chart.png'
    bar_path = out_dir / 'bar_chart.png'

    plot_line(months, sales, line_path)
    plot_bar(months, sales, bar_path)

    print(f'Generated: {line_path}')
    print(f'Generated: {bar_path}')


if __name__ == '__main__':
    main()
