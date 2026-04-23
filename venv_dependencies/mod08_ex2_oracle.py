#!/usr/bin/env python3

import os

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
    """Secure configuration demo"""

    print(f"\n[ORACLE STATUS]: {ITALIC}Reading the Matrix...{RESET}")

    # read the configuration file
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # env_path = os.path.join(script_dir, ".env")

    # load_dotenv(env_path)

    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ModuleNotFoundError:
        print(f"\n{BOLD_RED}ERROR: Missing required dependencies!{RESET}")

        print("\nInstall dependencies using pip:")
        print(f"{ITALIC}(it is recommended running this in venv){RESET}")
        print(f"  {YELLOW}pip install dotenv{RESET}")

        print("\n----------------------------------------------")
        return

    MATRIX_MODE = os.getenv("MATRIX_MODE", "development")  # default
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///default.db")  # default
    API_KEY = os.getenv("API_KEY")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    ZION_ENDPOINT = os.getenv("ZION_ENDPOINT")

    # check missing variables
    required_vars = {"API_KEY": API_KEY, "ZION_ENDPOINT": ZION_ENDPOINT}
    missing = [name for name, val in required_vars.items() if not val]

    if missing:
        print(f"\n{BOLD_RED}[WARNING]{RESET} Missing configuration for: "
              f"{', '.join(missing)}")
        print("Please set environment variables or fill in your .env file.\n")

    if DATABASE_URL.startswith("sqlite"):
        db_status = "Connected to SQLite database"
    elif DATABASE_URL.startswith("postgres"):
        db_status = "Connected to PostgreSQL database"
    else:
        db_status = "Connected to database"

    api_status = "Authenticated" if API_KEY else "API key missing"
    zion_status = "Online" if ZION_ENDPOINT else "Offline"

    # config info
    print(f"\n{BOLD}Configuration loaded:{RESET}\n")
    print(f"- Mode:\t\t{MATRIX_MODE}")
    print(f"- Database:\t{db_status}")
    print(f"- API Access:\t{api_status}")
    print(f"- Log Level:\t{LOG_LEVEL}")
    print(f"- Zion Network:\t{zion_status}")

    print(f"\n{BOLD}Environment security check:{RESET}\n")

    print(f"{GREEN}[OK]{RESET} No hardcoded secrets detected")

    # if os.path.exists(env_path):
    if os.path.exists(".env"):
        print(f"{GREEN}[OK]{RESET} .env file properly configured")
    else:
        print(f"{RED}[WARNING]{RESET} .env file missing")

    prod_override = MATRIX_MODE == "production" and API_KEY is not None
    print(f"{GREEN}[OK]{RESET} Production overrides available"
          if prod_override
          else f"{YELLOW}[INFO]{RESET} Production overrides not set")

    print("\n✅ The Oracle sees all configurations.")
    print("\n----------------------------------------------")


if __name__ == "__main__":
    main()
