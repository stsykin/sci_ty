from unittest import TestCase
from play import Scene, Player


class SceneTestCase(TestCase):

    def test_check_winner_false(self):
        scene = Scene()
        player = Player('test', "R")

        for i in range(0, 3):
            scene.set_turn(0, player)
        self.assertEqual(False, scene.check_winner(player, 1, 1))

    def test_check_winner_true(self):
        scene = Scene()
        player = Player('test', "G")
        for i in [1, 1, 1, 1]:
            scene.set_turn(1, player)
        self.assertEqual(True, scene.check_winner(player, 1, 1))
