import sys
from datetime import datetime
try:
    from pydantic import BaseModel, Field, ValidationError
except ModuleNotFoundError:
    print("Error, pydantic is missing. Run pip install pydantic.")
    sys.exit(2)


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_char=1, max_char=50)
    crew_size: int = Field(min_size=1, max_size=20)
    power_level: float = Field(min_percent=0.00, max_percent=100.0)
    oxygen_level: float = Field(min_percent=0.00, max_percent=100.0)
    last_maintenance = datetime
    is_operational: bool = True
    notes: str | None = Field(min_lenght=0, max_length=200)


def station_creation(data: dict[str, int | str | float | datetime
                                | bool]) -> SpaceStation:
    try:
        if "notes" in data:
            station = SpaceStation(
                        station_id=data['station_id'],
                        name=data['name'],
                        crew_size=data['crew_size'],
                        power_level=data['power_level'],
                        oxygen_level=data['oxygen_level'],
                        last_maintenance=data['last_maintenance'],
                        is_operational=data['is_operational'],
                        notes=data['notes']
                        )
        else:
            station = SpaceStation(
                        station_id=data['station_id'],
                        name=data['name'],
                        crew_size=data['crew_size'],
                        power_level=data['power_level'],
                        oxygen_level=data['oxygen_level'],
                        last_maintenance=data['last_maintenance'],
                        is_operational=data['is_operational']
                        )
        # station = SpaceStation(**data)
        return station
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            field = " -> ".join(map(str, error['loc']))
            print(f"'{field}': {error['msg']}")
        return None


def print_station(station: SpaceStation) -> None:
    print(f"ID: {station.station_id}")

    print(f"Name: {station.name}")

    if station.crew_size == 1:
        print(f"Crew: {station.crew_size} person")
    else:
        print(f"Crew: {station.crew_size} people")

    print(f"Power: {station.power_level}")

    print(f"Oxygen: {station.oxygen_level}")

    if not station.is_operational:
        print(f"Status: {False}")
    else:
        print(f"Status: {True}")

    if station.notes is not None:
        print(f"Notes: {station.notes}")


def main() -> None:
    station_infos = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": datetime.now(),
        "is_operational": True,
        "notes": "Yes, hello, I am a test for notes."
    }
    station = station_creation(station_infos)
    if station is None:
        return
    print("Valid station created:")
    print_station(station)
    print()

    print("========================================")
    station_infos = {
        "station_id": "ERROR001",
        "name": "International ERROR Station",
        "crew_size": 0,
        "power_level": 101.3,
        "oxygen_level": -1.3,
        "last_maintenance": "yes",
        "is_operational": "Trou"
    }
    station = station_creation(station_infos)
    if station is None:
        return
    print("Invalid station created:")
    print_station(station)
    print()


if __name__ == "__main__":
    print("Space Station Data Validation")
    print("========================================")
    main()
