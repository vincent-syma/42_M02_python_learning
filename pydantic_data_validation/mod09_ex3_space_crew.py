#!/usr/bin/env python3

from datetime import datetime

from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum

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


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    """Individual crew member class with validated fields"""

    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)  # years
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True  # = default


class SpaceMission(BaseModel):
    """Mission class with crew list and validated fields"""

    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)  # max 10 years
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)  # million dollars

    @model_validator(mode="after")
    def validate_safety_requirements(self) -> "SpaceMission":
        """Additional validation rules"""

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        leader = False
        experienced_crew = 0

        for member in self.crew:

            if not member.is_active:
                raise ValueError("All crew members must be active")

            if member.rank in {Rank.commander, Rank.captain}:
                leader = True

            if member.years_experience >= 5:
                experienced_crew += 1

        if not leader:
            raise ValueError("Mission must have at least one "
                             "Commander or Captain")

        experienced_ratio = experienced_crew / len(self.crew)
        if self.duration_days > 365 and experienced_ratio < 0.5:
            raise ValueError("Long missions (> 365 days) need "
                             "50% experienced crew (5+ years)")

        return self


def print_mission_info(mission: SpaceMission) -> None:
    """Display space mission info in readable format."""

    print("\n✅ Valid mission created:\n")
    print(f"{BOLD}Mission:{RESET}\t{mission.mission_name}")
    print(f"{BOLD}ID:{RESET}\t\t{mission.mission_id}")
    print(f"{BOLD}Destination:{RESET}\t{mission.destination}")
    print(f"{BOLD}Duration:{RESET}\t{mission.duration_days} days")
    print(f"{BOLD}Budget:{RESET}\t\t${mission.budget_millions}M")
    print(f"{BOLD}Crew size:{RESET}\t{len(mission.crew)}")

    print(f"\n{BOLD}Crew members:{RESET}")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) "
              f"- {member.specialization}")


def main() -> None:
    """Demonstration"""

    print(f"\n{BOLD}Space Mission Crew Validation{RESET}")
    print("-" * 40)

    # valid
    try:
        mission = SpaceMission(
            mission_name="Mars Colony Establishment",
            mission_id="M2024_MARS",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="001",
                    name="Sarah Connor",
                    rank="commander",
                    age=40,
                    specialization="Mission Command",
                    years_experience=10,
                    # is_active=True  # = default
                ),
                CrewMember(
                    member_id="002",
                    name="John Smith",
                    rank="lieutenant",
                    age=32,
                    specialization="Navigation",
                    years_experience=6,
                    # is_active=True  # = default
                ),
                CrewMember(
                    member_id="003",
                    name="Alice Johnson",
                    rank="officer",
                    age=26,
                    specialization="Engineering",
                    years_experience=3,
                    # is_active=True  # = default
                )
            ],
            # mission_status=,
            budget_millions=2500.0
        )
        print_mission_info(mission)

    except ValidationError as e:
        print(f"\n{BOLD_RED}Unxpected error(s):{RESET}\n")
        print(e.errors()[0]["msg"])
        # for err in e.errors():
        #     print(f"- {err['loc'][0]} → {err['msg']}")

    finally:
        print()
        print("-" * 40)

    # invalid
    try:
        mission = SpaceMission(
            mission_name="Mars Colony Establishment",
            mission_id="M2024_MARS",  # "2024_MARS"
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="001",
                    name="Sarah Connor",
                    rank="cadet",  # captain
                    age=40,  # 17
                    specialization="Mission Command",
                    years_experience=10,  # 1
                    # is_active=False
                ),
                CrewMember(
                    member_id="002",
                    name="John Smith",
                    rank="lieutenant",
                    age=32,
                    specialization="Navigation",
                    years_experience=6,
                    # is_active=True  # = default
                ),
                CrewMember(
                    member_id="003",
                    name="Alice Johnson",
                    rank="officer",
                    age=26,
                    specialization="Engineering",
                    years_experience=3,
                    # is_active=True  # = default
                )
            ],
            # mission_status=,
            budget_millions=2500.0
        )
        print_mission_info(mission)

    except ValidationError as e:
        print(f"\n{BOLD_RED}Expected error:{RESET}\n")
        print(f"- {e.errors()[0]['msg']}")
        # for err in e.errors():
        #     print(f"- {err['loc'][0]} → {err['msg']}")

    finally:
        print()
        print("-" * 40)


if __name__ == "__main__":
    main()
