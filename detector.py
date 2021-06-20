from typing import Tuple

from invader import Invader


class InvaderDetector:
    def __init__(self, invader: Invader, coordinates: Tuple[int, int], accuracy: float):
        self.invader = invader.name
        self.coordinates = coordinates
        self.accuracy = accuracy

    def __str__(self):
        return f'{self.invader}: Coordinates: {self.coordinates}, Accuracy = {self.accuracy} '
