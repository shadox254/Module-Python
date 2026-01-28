import sys
from datetime import datetime
from enum import Enum
from typing import List
try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ModuleNotFoundError:
    print("Error, pydantic is missing. Run pip install pydantic.")
    sys.exit(2)


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation(self):
        if self.mission_id.startswith("M") is False:
            raise ValueError("Mission ID must start with \"M\"")

        high_rank_count = sum(1 for member in self.crew if member.rank is
                              Rank.CAPTAIN or member.rank is Rank.COMMANDER)
        if high_rank_count == 0:
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            experienced_member = sum(1 for member in self.crew if
                                     member.years_experience >= 5)
            if experienced_member < len(self.crew) / 2:
                raise ValueError("Long missions (> 365 days) need 50% \
experienced crew (5+ years)")

        all_active = all(member.is_active for member in self.crew)
        if all_active is False:
            raise ValueError("All crew members must be active")
        return self


def print_mission_infos(mission: SpaceMission) -> None:
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) - \
{member.specialization}")


def space_crew() -> None:
    try:
        first_crew = [
            CrewMember(member_id="COMM_001", name="Sarah Connor",
                       rank=Rank.COMMANDER, age=22,
                       specialization="Mission Command", years_experience=5),
            CrewMember(member_id="LTNT_001", name="John Smith",
                       rank=Rank.LIEUTENANT, age=78,
                       specialization="Navigation", years_experience=50),
            CrewMember(member_id="OFFI_001", name="Alice Johnson",
                       rank=Rank.OFFICER, age=55, specialization="Engineering",
                       years_experience=35)
        ]
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            field = "".join(map(str, error['loc']))
            print(f"'{field}': {error['msg']}")
        sys.exit(2)

    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=first_crew,
            budget_millions=2500.0
        )
    except ValidationError as e:
        for error in e.errors():
            clean_error = error['msg'].replace('Value error, ', '')
            print(clean_error)
        sys.exit(2)
    print("Valid mission created:")
    print_mission_infos(mission)
    print()

    print("=========================================")
    print("Expected validation error:")
    try:
        wrong_crew = [
            CrewMember(member_id="COMM_001", name="Sarah Connor",
                       rank=Rank.CADET, age=22,
                       specialization="Mission Command", years_experience=5)
        ]
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            field = "".join(map(str, error['loc']))
            print(f"'{field}': {error['msg']}")
        sys.exit(2)

    try:
        mission = SpaceMission(mission_id="M2024_MARS",
                               mission_name="Mars Colony Establishment",
                               destination="Mars", launch_date=datetime.now(),
                               duration_days=900, crew=wrong_crew,
                               budget_millions=2500.0)
    except ValidationError as e:
        for error in e.errors():
            clean_error = error['msg'].replace('Value error, ', '')
            print(clean_error)
    print()

    print("=========================================")
    print("Expected validation error:")
    try:
        wrong_crew = [
            CrewMember(member_id="COMM_001", name="Sarah Connor",
                       rank=Rank.CAPTAIN, age=22,
                       specialization="Mission Command", years_experience=5)
        ]
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            field = "".join(map(str, error['loc']))
            print(f"'{field}': {error['msg']}")
        sys.exit(2)

    try:
        mission = SpaceMission(mission_id="E2024_MARS",
                               mission_name="Mars Colony Establishment",
                               destination="Mars", launch_date=datetime.now(),
                               duration_days=900, crew=wrong_crew,
                               budget_millions=2500.0)
    except ValidationError as e:
        for error in e.errors():
            clean_error = error['msg'].replace('Value error, ', '')
            print(clean_error)
    print()

    print("=========================================")
    print("Expected validation error:")
    try:
        wrong_crew = [
            CrewMember(member_id="COMM_001", name="Sarah Connor",
                       rank=Rank.CAPTAIN, age=22,
                       specialization="Mission Command", years_experience=1)
        ]
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            field = "".join(map(str, error['loc']))
            print(f"'{field}': {error['msg']}")
        sys.exit(2)

    try:
        mission = SpaceMission(mission_id="M2024_MARS",
                               mission_name="Mars Colony Establishment",
                               destination="Mars", launch_date=datetime.now(),
                               duration_days=900, crew=wrong_crew,
                               budget_millions=2500.0)
    except ValidationError as e:
        for error in e.errors():
            clean_error = error['msg'].replace('Value error, ', '')
            print(clean_error)
    print()

    print("=========================================")
    print("Expected validation error:")
    try:
        wrong_crew = [
            CrewMember(member_id="COMM_001", name="Sarah Connor",
                       rank=Rank.CAPTAIN, age=22,
                       specialization="Mission Command", years_experience=5,
                       is_active=False)
        ]
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            field = "".join(map(str, error['loc']))
            print(f"'{field}': {error['msg']}")
        sys.exit(2)

    try:
        mission = SpaceMission(mission_id="M2024_MARS",
                               mission_name="Mars Colony Establishment",
                               destination="Mars", launch_date=datetime.now(),
                               duration_days=900, crew=wrong_crew,
                               budget_millions=2500.0)
    except ValidationError as e:
        for error in e.errors():
            clean_error = error['msg'].replace('Value error, ', '')
            print(clean_error)
    print()


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("=========================================")
    space_crew()
