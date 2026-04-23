#!/usr/bin/env python3

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError

# python3 -m venv venv
# source venv/bin/activate
# pip install "pydantic>=2"

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


class SpaceStation(BaseModel):
    """Spacestation class with validated fields"""

    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=500)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)  # 0.0-100.0 percent
    oxygen_level: float = Field(..., ge=0.0, le=100.0)  # 0.0-100.0 percent
    last_maintenance: datetime
    is_operational: bool = True  # = default
    notes: Optional[str] = Field(default=None, max_length=200)


def print_station_info(station: SpaceStation) -> None:
    """Display station info in readable format."""

    status: str = ("Operational"
                   if station.is_operational
                   else "Offline")

    print("\n✅ Valid station created:\n")
    print(f"{BOLD}ID:{RESET}\t\t  {station.station_id}")
    print(f"{BOLD}Name:{RESET}\t\t  {station.name}")
    print(f"{BOLD}Crew:{RESET}\t\t  {station.crew_size} people")
    print(f"{BOLD}Power:{RESET}\t\t  {station.power_level}%")
    print(f"{BOLD}Oxygen:{RESET}\t\t  {station.oxygen_level}%")
    print(f"{BOLD}Last maintenance:{RESET} {station.last_maintenance}")
    print(f"{BOLD}Status:{RESET}\t\t  {status}\n")
    print(f"{BOLD}Notes:{RESET}\t\t  {station.notes}")


def main() -> None:
    """Demonstration"""

    print(f"\n{BOLD}Space Station Data Validation{RESET}")
    print("-" * 40)

    # valid
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size="6",  # string is valid
            power_level=85.5,
            oxygen_level=92.3,
            # last_maintenance="2026-03-01T12:00:00",  # datetime.now()
            last_maintenance=datetime.now(),
            # notes="This is a note"
        )
        print_station_info(station)

    except ValidationError as e:
        print(f"\n{BOLD_RED}Unexpected error(s):{RESET}\n")
        for err in e.errors():
            print(f"- {err['loc'][0]} → {err['msg']}")

    finally:
        print()
        print("-" * 40)

    # invalid
    try:
        SpaceStation(
            station_id="42",  # 3-10
            name="",  # 1-500
            crew_size=25,  # 1-20
            power_level="abc",  # 0-100, float
            oxygen_level=-1  # 0-100, float
            # maintenance missing
        )
    except ValidationError as e:
        print(f"\n{BOLD_RED}Expected error(s):{RESET}\n")
        for err in e.errors():
            print(f"- {err['loc'][0]} → {err['msg']}")

    finally:
        print()
        print("-" * 40)


if __name__ == "__main__":
    main()
