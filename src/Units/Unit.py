import math


class Measurement(object):
    def __init__(self, _value):
        self.value = _value

    def get_value(self):
        return self.value


class Angle(Measurement):
    # All angles are converted to radians on construction
    def __init__(self, _value, _unit):
        self.rates = {
            'radians': 1,
            'degrees': math.pi / 180,
            'gradians': math.pi / 200
        }
        super().__init__(_value * self.rates[_unit.lower()])


class Distance(Measurement):
    # All distances are converted to meters on construction
    def __init__(self, _value, _unit):
        self.rates = {
            'meters': 1,
            'feet': 1/3.280839895,
            'inches': 1/3.280839895/12,
            'cubits': 0.4572
        }
        super().__init__(_value * self.rates[_unit.lower()])


class Duration(Measurement):
    # All durations are converted to seconds on construction
    def __init__(self, _value, _unit):
        self.rates = {
            'seconds': 1,
            'minutes': 60,
        }
        super().__init__(_value * self.rates[_unit.lower()])
