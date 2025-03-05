from datetime import datetime

class Flight:
    def __init__(self, id: int, course: list[str], departure: datetime, arrival: datetime):
        self.id = id
        self.course = course
        self.departure = departure
        self.arrival = arrival
