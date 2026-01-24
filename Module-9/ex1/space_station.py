import sys
from datetime import datetime
try:
    from pydantic import BaseModel, Field, ValidationError
except ModuleNotFoundError:
    print("Error, pydantic is missing. Install it to run the program.")
    sys.exit(2)


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_char=1, max_char=50)
    crew_size: int = Field(min_size=1, max_size=20)
    power_level: float = Field(min_percent=0.00, max_percent=100.0)
    oxygen_level: float = Field(min_percent=0.00, max_percent=100.0)
    last_maintenance = datetime
    is_operational: bool = True
    notes: str = Field(min_lenght=0, max_length=200)


def station_creation(data: dict[str, int | str | float | datetime | bool]):
    try:
        


def main() -> None:
    pass


if __name__ == "__main__":
    print("Space Station Data Validation")
    print("========================================")
    main()