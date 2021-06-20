from typing import List, Iterable

from invader import Invader
from detector import InvaderDetector


class Radar:
    def __init__(self, radar_sample: List[List[str]], accuracy: float, known_invaders: List[Invader]):
        self.radar_sample = radar_sample
        self.accuracy = accuracy
        self.known_invaders = known_invaders

    def find_invaders(self) -> Iterable[InvaderDetector]:
        for invader in self.known_invaders:
            ideal_number_of_matches = len(invader.matrix) * len(invader.matrix[0])
            for i1 in range(len(self.radar_sample)):
                for j1 in range(len(self.radar_sample[i1])):

                    match_count = 0

                    for i2 in range(len(invader.matrix)):
                        for j2 in range(len(invader.matrix[i2])):

                            if i1 + i2 < len(self.radar_sample) and j1 + j2 < len(self.radar_sample[i1]):
                                radar_cell = self.radar_sample[i1 + i2][j1 + j2]
                                invader_cell = invader.matrix[i2][j2]

                                if radar_cell == invader_cell:
                                    match_count += 1

                    accuracy = match_count / ideal_number_of_matches
                    if accuracy >= self.accuracy:
                        yield InvaderDetector(invader, (i1, j1), accuracy)
