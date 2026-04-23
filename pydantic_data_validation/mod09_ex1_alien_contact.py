#!/usr/bin/env python3

from datetime import datetime
from typing import Optional

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


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """AlienContact class with validated fields"""

    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)  # 0.0-10.0 scale
    duration_minutes: int = Field(..., ge=1, le=1440)  # max 24 hours
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False  # = default

    @model_validator(mode="after")
    def validate_business_rules(self) -> "AlienContact":
        """Additional validation rules"""

        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (self.contact_type == ContactType.telepathic
           and self.witness_count < 3):
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals should include received messages")

        return self


def print_alien_contact_info(contact: AlienContact) -> None:
    """Display alien contact info in readable format."""

    print("\n✅ Valid alien contact created:\n")
    print(f"{BOLD}ID:{RESET}\t\t {contact.contact_id}")
    print(f"{BOLD}Timestamp:{RESET}\t {contact.timestamp}")
    print(f"{BOLD}Location:{RESET}\t {contact.location}")
    print(f"{BOLD}Contact type:{RESET}\t {contact.contact_type.value}")
    print(f"{BOLD}Signal strength:{RESET} {contact.signal_strength}/10")
    print(f"{BOLD}Duration:{RESET}\t {contact.duration_minutes} minutes")
    print(f"{BOLD}Witnesses:{RESET}\t {contact.witness_count} people")
    print(f"{BOLD}Verified:{RESET}\t {contact.is_verified}\n")
    print(f"{BOLD}Message received:{RESET} '{contact.message_received}'")


def main() -> None:
    """Demonstration"""

    print(f"\n{BOLD}Alien Contact Log Validation{RESET}")
    print("-" * 40)

    # valid
    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2026-03-01T12:00:00",
            location="Area 51, Nevada",
            contact_type="radio",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received='Greetings from Zeta Reticuli',
            is_verified=True
        )
        print_alien_contact_info(contact)

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
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type="telepathic",
            signal_strength=7,
            duration_minutes=1000,
            witness_count=1,
            message_received="",
            is_verified=True
        )
        print_alien_contact_info(contact)

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
