import sys
from datetime import datetime
from enum import Enum
try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ModuleNotFoundError:
    print("Error, pydantic is missing. Run pip install pydantic.")
    sys.exit(2)


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validator(self):
        if self.contact_id.startswith("AC") is False:
            raise ValueError("Error, Contact ID must start with \"AC\" (Alien \
Contact)")

        if self.contact_type is ContactType.PHYSICAL:
            if self.is_verified is False:
                raise ValueError("Error, Physical contact reports must be \
verified")

        if self.contact_type is ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise ValueError("Error, Telepathic contact requires at least \
3 witnesses")

        if self.signal_strength > 7.0:
            if self.message_received is None:
                raise ValueError("Strong signals (> 7.0) should include \
received messages")
        return self


def print_contact_infos(contact: AlienContact) -> None:
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received is not None:
        print(f"Message: {contact.message_received}")


def contact_creation(data: dict[str, datetime | str | ContactType | float |
                                int | bool]) -> AlienContact:
    try:
        contact = AlienContact(
            contact_id=data["contact_id"],
            timestamp=data["timestamp"],
            location=data["location"],
            contact_type=data["contact_type"],
            signal_strength=data["signal_strength"],
            duration_minutes=data["duration_minutes"],
            witness_count=data["witness_count"],
            message_received=data["message_received"]
        )
    except ValidationError as e:
        for error in e.errors():
            clean_error = error['msg'].replace('Value error, ', '')
            print(clean_error)
        sys.exit(2)
    return contact


def alien_contact() -> None:
    contact_infos = {
        "contact_id": "AC_2024_001",
        "timestamp": datetime.now(),
        "location": "Area 51, Nevada",
        "contact_type": ContactType.RADIO,
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli"
    }
    contact = contact_creation(contact_infos)
    print_contact_infos(contact)
    print()

    print("======================================")
    print("Expected validation error:")
    contact_infos = {
        "contact_id": "AC_2024_001",
        "timestamp": datetime.now(),
        "location": "Area 51, Nevada",
        "contact_type": ContactType.TELEPATHIC,
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 2,
        "message_received": "Greetings from Zeta Reticuli"
    }
    contact = contact_creation(contact_infos)


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("======================================")
    alien_contact()
