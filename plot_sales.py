#!/usr/bin/env python3
"""
Generate a line chart and a bar chart from monthl_sales.json and save as PNG files.

Usage: python plot_sales.py

Requires: matplotlib
"""
import json
from pathlib import Path
import matplotlib.pyplot as plt


def load_data(json_path: Path):
    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    months = [item.get("Month") for item in data]
    sales = [item.get("Sales") for item in data]
    return months, sales


def plot_line(months, sales, out_path: Path):
    plt.figure(figsize=(10, 5))
    plt.plot(months, sales, marker="o", linestyle="-", color="#1f77b4")
    plt.title("Monthly Sales — Line Chart")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def plot_bar(months, sales, out_path: Path):
    plt.figure(figsize=(10, 5))
    plt.bar(months, sales, color="#ff7f0e")
    plt.title("Monthly Sales — Bar Chart")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def main():
    base = Path(__file__).parent
    json_path = base / "monthl_sales.json"
    if not json_path.exists():
        print(f"Data file not found: {json_path}")
        return

    months, sales = load_data(json_path)
    out_line = base / "line_chart.png"
    out_bar = base / "bar_chart.png"

    plot_line(months, sales, out_line)
    print(f"Saved line chart to {out_line}")
    plot_bar(months, sales, out_bar)
    print(f"Saved bar chart to {out_bar}")


if __name__ == "__main__":
    main()
