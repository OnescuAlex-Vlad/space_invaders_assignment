import unittest

from invaders_detector import multiline_string_to_matrix
from radar import Radar
from invader import Invader


class TestFindInvaders(unittest.TestCase):
    def setUp(self):
        invader_matrix = multiline_string_to_matrix('''
            --o-----o--
            ---o---o---
            --ooooooo--
            -oo-ooo-oo-
            ooooooooooo
            o-ooooooo-o
            o-o-----o-o
            ---oo-oo---''')
        self.invader = Invader('test_invader', invader_matrix)

    def test_best_case_scenario(self):
        radar_matrix = multiline_string_to_matrix('''
            --o-----o--
            ---o---o---
            --ooooooo--
            -oo-ooo-oo-
            ooooooooooo
            o-ooooooo-o
            o-o-----o-o
            ---oo-oo---''')
        radar = Radar(radar_matrix, 1, [self.invader])

        result = list(radar.find_invaders())

        self.assertEqual(result[0].coordinates, (0, 0))
        self.assertEqual(result[0].accuracy, 1)

    def test_noise(self):
        radar_matrix = multiline_string_to_matrix('''
            NOISE---o--
            ---o---o---
            --ooooooo--
            -oo-ooo-oo-
            ooooooooooo
            o-ooooooo-o
            o-o-----o-o
            ---oo-oo---''')
        radar = Radar(radar_matrix, 0.8, [self.invader])

        result = list(radar.find_invaders())

        self.assertEqual(result[0].coordinates, (0, 0))

    def test_with_no_invaders(self):
        radar_matrix = multiline_string_to_matrix('''
            -----------
            -----------
            -----------
            -----------
            -----------
            -----------
            -----------
            -----------''')
        radar = Radar(radar_matrix, 0.8, [self.invader])

        result = list(radar.find_invaders())

        self.assertEqual(result, [])

    def test_matrix_creation(self):
        multiline_string = '''
        --oo----o---o-o
        -------o-------
        o--oooooo-----o
        -oo--oo--o-----
        oo-oooooooo---o
        o-ooooooo-o----
        oo-o----o-oo-o-
        --ooo-oo--o---o'''
        matrix = [
            ['-', '-', 'o', 'o', '-', '-', '-', '-', 'o', '-', '-', '-', 'o', '-', 'o'],
            ['-', '-', '-', '-', '-', '-', '-', 'o', '-', '-', '-', '-', '-', '-', '-'],
            ['o', '-', '-', 'o', 'o', 'o', 'o', 'o', 'o', '-', '-', '-', '-', '-', 'o'],
            ['-', 'o', 'o', '-', '-', 'o', 'o', '-', '-', 'o', '-', '-', '-', '-', '-'],
            ['o', 'o', '-', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '-', '-', '-', 'o'],
            ['o', '-', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '-', 'o', '-', '-', '-', '-'],
            ['o', 'o', '-', 'o', '-', '-', '-', '-', 'o', '-', 'o', 'o', '-', 'o', '-'],
            ['-', '-', 'o', 'o', 'o', '-', 'o', 'o', '-', '-', 'o', '-', '-', '-', 'o']
        ]

        result = multiline_string_to_matrix(multiline_string)

        self.assertEqual(result, matrix)
