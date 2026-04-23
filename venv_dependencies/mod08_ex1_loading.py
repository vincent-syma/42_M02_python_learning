#!/usr/bin/env python3

import importlib

# ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

# combinations
BOLD_RED = BOLD + RED
BOLD_GREEN = BOLD + GREEN
BOLD_BLUE = BOLD + BLUE


def main() -> None:
    """Entry point of the program"""

    print("\n[LOADING STATUS]: Loading programs...")
    print("\nChecking dependencies:")

    packages = {
        "pandas": None,
        "numpy": None,
        "matplotlib": None
    }
    for name, module in packages.items():
        try:
            packages[name] = importlib.import_module(name)
            version = getattr(packages[name], "__version__", "unknown")
            print(f"{GREEN}[OK]{RESET} {name} ({version}) - ready")

        except ImportError:
            print(f"{RED}[MISSING]{RESET} {name} - not installed")

    if not all(packages.values()):
        print(f"\n{BOLD_RED}ERROR: Missing required dependencies!{RESET}")

        print("\nInstall dependencies using pip:")
        print(f"{ITALIC}(it is recommended running this in venv){RESET}")
        print(f"  {YELLOW}pip install -r requirements.txt{RESET}")
        print("\nOr using Poetry:")
        print(f"  {YELLOW}poetry install")
        print(f"  poetry run python loading.py{RESET}")

        print("\n----------------------------------------------")
        return

    print("\nDependency management comparison:")
    print("- pip uses requirements.txt for dependency lists")
    print("- Poetry uses pyproject.toml and manages virtual "
          "environments automatically")

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    data = np.random.randn(1000)

    df = pd.DataFrame(data, columns=["values"])
    df["rolling_mean"] = df["values"].rolling(window=50).mean()

    print(f"Mean: {df['values'].mean():.4f}")
    print(f"Std: {df['values'].std():.4f}")

    print("\nGenerating visualization...")

    plt.figure()
    plt.plot(df["values"], label="Raw Data")
    plt.plot(df["rolling_mean"], label="Rolling Mean", linewidth=2)
    plt.title("Matrix Data Analysis")
    plt.legend()
    plt.savefig("matrix_analysis.png")

    print("✅ Analysis complete!")
    print("Results saved to: matrix_analysis.png")

    print("\n----------------------------------------------")


if __name__ == "__main__":
    main()
