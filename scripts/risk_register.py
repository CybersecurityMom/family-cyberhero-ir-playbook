#!/usr/bin/env python3
"""
Family CyberHero Risk Register (Beginner-friendly)
- Add risks about your pretend business
- List all risks in a simple table
- Saves to risk_register.csv in the same folder
"""

import csv
import os
from datetime import datetime

CSV_FILE = "risk_register.csv"
HEADERS = [
    "date", "business_name", "asset", "risk_description",
    "threat_actor", "likelihood_1_to_5", "impact_1_to_5", "notes"
]

def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)

def add_risk():
    print("\nAdd a new risk (press Enter to accept defaults or skip optional fields).")
    business = input("Business name: ").strip() or "My Family Business"
    asset = input("What are we protecting (asset)? ").strip() or "Tablet"
    desc = input("What could go wrong (risk description)? ").strip() or "Phishing link"
    actor = input("Who/what could cause it (threat actor)? ").strip() or "Phishy Fish"
    try:
        likelihood = int(input("Likelihood (1=low, 5=high): ").strip() or "3")
        impact = int(input("Impact (1=low, 5=high): ").strip() or "3")
    except ValueError:
        print("Please use numbers 1-5. Using default 3.")
        likelihood, impact = 3, 3
    notes = input("Notes (optional): ").strip()

    row = [
        datetime.now().strftime("%Y-%m-%d"),
        business, asset, desc, actor, likelihood, impact, notes
    ]
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)

    print("\n✅ Risk added!\n")

def list_risks():
    if not os.path.exists(CSV_FILE):
        print("\nNo risks yet. Add one with: python3 risk_register.py add\n")
        return

    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if len(rows) <= 1:
        print("\nNo risks yet. Add one with: python3 risk_register.py add\n")
        return

    print("\nYour Risk Register:\n")
    print("{:<12} {:<20} {:<15} {:<22} {:<14} {:<11} {:<9} {}".format(
        "date","business_name","asset","risk_description",
        "threat_actor","likelihood","impact","notes"
    ))
    print("-" * 120)
    for r in rows[1:]:
        date, business, asset, desc, actor, like, imp, notes = r
        print("{:<12} {:<20} {:<15} {:<22} {:<14} {:<11} {:<9} {}".format(
            date, business[:20], asset[:15], desc[:22], actor[:14], like, imp, notes[:40]
        ))
    print("")

def main():
    import sys
    init_csv()
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 risk_register.py add   # add a new risk")
        print("  python3 risk_register.py list  # see all risks")
        return

    cmd = sys.argv[1].lower()
    if cmd == "add":
        add_risk()
    elif cmd == "list":
        list_risks()
    else:
        print("Unknown command. Use 'add' or 'list'.")

if __name__ == "__main__":
    main()
