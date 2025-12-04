"""
Generate line and bar charts from monthly sales data in JSON.

Usage:
    python generate_sales_charts.py [--input PATH] [--outdir DIR]

Outputs:
    line_chart.png, bar_chart.png (saved to --outdir)
"""
import argparse
import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DEFAULT_INPUT = "monthl_sales.json"


def load_data(input_path: Path) -> pd.DataFrame:
    try:
        with input_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise SystemExit(f"Input file not found: {input_path}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"Failed to parse JSON: {e}")

    df = pd.DataFrame(data)
    expected_cols = {"Month", "Sales"}
    if not expected_cols.issubset(df.columns):
        raise SystemExit(f"Input JSON must contain columns {expected_cols}; found {set(df.columns)}")

    # Preserve month order as provided; optionally enforce a categorical ordering
    if "Month" in df:
        # If months look like abbreviations, enforce standard order
        month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        if set(df["Month"]).issubset(set(month_order)):
            df["Month"] = pd.Categorical(df["Month"], categories=month_order, ordered=True)
            df = df.sort_values("Month")

    return df


def plot_line(df: pd.DataFrame, output: Path):
    plt.figure(figsize=(10, 5))
    plt.plot(df["Month"], df["Sales"], marker="o", linestyle="-", color="#1f77b4", linewidth=2)
    plt.title("Monthly Sales - Line Chart")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(output)
    plt.close()


def plot_bar(df: pd.DataFrame, output: Path):
    plt.figure(figsize=(10, 5))
    plt.bar(df["Month"], df["Sales"], color="#ff7f0e")
    plt.title("Monthly Sales - Bar Chart")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig(output)
    plt.close()


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate line and bar charts from monthly sales JSON data")
    parser.add_argument("--input", "-i", type=Path, default=Path(DEFAULT_INPUT), help="Path to monthl_sales.json (default: monthl_sales.json in current dir)")
    parser.add_argument("--outdir", "-o", type=Path, default=Path("."), help="Output directory for charts (default: current directory)")

    args = parser.parse_args(argv)

    df = load_data(args.input)
    outdir: Path = args.outdir
    outdir.mkdir(parents=True, exist_ok=True)

    line_path = outdir / "line_chart.png"
    bar_path = outdir / "bar_chart.png"

    plot_line(df, line_path)
    plot_bar(df, bar_path)

    print(f"Saved line chart to {line_path}")
    print(f"Saved bar chart to {bar_path}")


if __name__ == "__main__":
    main()
