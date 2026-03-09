#!/usr/bin/env python3
"""
Simple script to print mobile market prices in Pakistan (approximate values).
"""

data = {
    "Samsung Galaxy S23": 200000,
    "iPhone 14": 270000,
    "Xiaomi Redmi Note 12": 65000,
    "Realme 11": 45000,
    "Tecno Spark 10": 30000,
}


def format_price(p):
    return f"PKR {p:,.0f}"


def print_all():
    print("Mobile Market Prices in Pakistan (approx.)")
    print("-" * 46)
    for model, price in data.items():
        print(f"{model:35} {format_price(price)}")


def lookup(model):
    model_lower = model.lower()
    found = False
    for m, p in data.items():
        if model_lower in m.lower():
            print(f"{m:35} {format_price(p)}")
            found = True
    if not found:
        print("Model not found. Available models:")
        for m in data:
            print(" -", m)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Print mobile market prices in Pakistan")
    parser.add_argument("--model", "-m", help="Model name to lookup (partial match allowed)")
    args = parser.parse_args()
    if args.model:
        lookup(args.model)
    else:
        print_all()


if __name__ == "__main__":
    main()
