from typing import Optional
from ses.schemas.schemas import Location
from ses.core.repository import MongoRepo

class LocationService:
    def __init__(self):
        self.repo = MongoRepo(
            Location,
            "mongodb://localhost:27017",
            "ses"
        )

    def get_location_by_campus(self, campus: str) -> Optional[Location]:
        return self.repo.get_by({"campus": campus})

    def add_location(self, location: Location):
        self.repo.add(location)