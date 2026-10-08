"""
Depreciation Calculator
Reads assets from assets.csv and prints a straight-line
depreciation schedule for each asset.
"""
import csv


def straight_line(cost, salvage, life):
    """Annual depreciation = (cost - salvage value) / useful life."""
    return (cost - salvage) / life


def print_schedule(name, cost, salvage, life):
    annual = straight_line(cost, salvage, life)
    book_value = cost
    print(f"\n{name}  (Cost ${cost:,.0f}, Salvage ${salvage:,.0f}, Life {life} yrs)")
    print(f"{'Year':<6}{'Depreciation':>14}{'Accum. Depr.':>16}{'Book Value':>14}")
    accumulated = 0
    for year in range(1, life + 1):
        accumulated += annual
        book_value -= annual
        print(f"{year:<6}{annual:>14,.2f}{accumulated:>16,.2f}{book_value:>14,.2f}")


def main():
    with open("assets.csv", newline="") as f:
        for row in csv.DictReader(f):
            print_schedule(
                row["asset"],
                float(row["cost"]),
                float(row["salvage_value"]),
                int(row["useful_life_years"]),
            )


if __name__ == "__main__":
    main()
