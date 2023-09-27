import math

class Measurement(object):
    def __init__(self, _value: float, _rates: dict) -> None:
        self.rates = _rates
        self.value = _value

    def __eq__(self, other) -> bool:
        assert type(self) == type(other), "Attempted comparison across types."
        return self.value == other.value

    def __gt__(self, other) -> bool:
        assert type(self) == type(other), "Attempted comparison across types."
        return self.value > other.value

    def __lt__(self, other) -> bool:
        assert type(self) == type(other), "Attempted comparison across types."
        return self.value < other.value

    def __ge__(self, other) -> bool:
        assert type(self) == type(other), "Attempted comparison across types."
        return self.value >= other.value

    def __le__(self, other) -> bool:
        assert type(self) == type(other), "Attempted comparison across types."
        return self.value <= other.value

    def get_as(self, unit: str) -> float:
        return self.value / self.rates[unit.lower()]


class Angle(Measurement):
    # All angles are converted to radians on construction
    def __init__(self, _value: float, _unit: str) -> None:
        self.rates = {
            'radians': 1,
            'degrees': math.pi / 180,
            'gradians': math.pi / 200
        }
        super().__init__(_value * self.rates[_unit.lower()], self.rates)

    def __add__(self, other):
        assert type(self) == type(other), "Attempted addition across types."
        return Angle(self.get_as("radians") + other.get_as("radians"), "radians")

    def __sub__(self, other):
        assert type(self) == type(other), "Attempted subtraction across types."
        return Angle(self.get_as("radians") - other.get_as("radians"), "radians")

class Distance(Measurement):
    # All distances are converted to meters on construction
    def __init__(self, _value: float, _unit: str) -> None:
        self.rates = {
            'meters': 1,
            'feet': 1/3.280839895,
            'miles': 5280/3.280839895,
            'nautical miles': 1852,
            'inches': 1/3.280839895/12,
            'cubits': 0.4572
        }
        super().__init__(_value * self.rates[_unit.lower()], self.rates)

    def __add__(self, other):
        assert type(self) == type(other), "Attempted addition across types."
        return Angle(self.get_as("meters") + other.get_as("meters"), "meters")

    def __sub__(self, other):
        assert type(self) == type(other), "Attempted subtraction across types."
        return Angle(self.get_as("meters") - other.get_as("meters"), "meters")

class Duration(Measurement):
    # All durations are converted to seconds on construction
    def __init__(self, _value, _unit:str) -> None:
        self.rates = {
            'seconds': 1,
            'minutes': 60,
        }
        super().__init__(_value * self.rates[_unit.lower()], self.rates)

    def __add__(self, other):
        assert type(self) == type(other), "Attempted addition across types."
        return Angle(self.get_as("seconds") + other.get_as("seconds"), "seconds")

    def __sub__(self, other):
        assert type(self) == type(other), "Attempted subtraction across types."
        return Angle(self.get_as("seconds") - other.get_as("seconds"), "seconds")

class Position(object):
    center = () # Tuple of Angles: (Latitude, longitude)

    @staticmethod
    def set_center(latitude:Angle, longitude:Angle)->None:
        # TODO: add conversion
        Position.center = (latitude, longitude)

    def __init__(self, relativeX:Distance):
        self.rates = {}