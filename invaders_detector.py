from typing import List

from radar import Radar
from invader import Invader


def multiline_string_to_matrix(multiline_string: str) -> List[List[str]]:
    lines = []
    for line in filter(None, multiline_string.split('\n')):
        lines.append(list(line.strip()))

    return lines


def file_to_matrix(filename: str) -> List[List[str]]:
    with open(filename, 'r') as infile:
        return multiline_string_to_matrix(infile.read())


if __name__ == '__main__':
    invader_one = Invader('Crab', file_to_matrix('space_invader_one.txt'))
    invader_two = Invader('Rocket', file_to_matrix('space_invader_two.txt'))
    radar_sample = file_to_matrix('radar_sample.txt')
    radar = Radar(radar_sample, 0.8, [invader_one, invader_two])
    print(list(str(invader_info) for invader_info in radar.find_invaders()))
