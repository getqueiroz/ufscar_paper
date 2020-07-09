from enum import Enum

class Mode(Enum):
    MAXIMAZING = 0
    MINIMAZING = 1

class Feature:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.desired_value = 0
        self.values = []
        self.mode = Mode.MAXIMAZING
