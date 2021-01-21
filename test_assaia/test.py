from unittest import TestCase
from play import Scene


class SceneTestCase(TestCase):
    def test_check_winner_false(self):
        scene = Scene()
        for i in range(0, 3):
            scene.set_turn(0, "G")
        self.assertEqual(False, scene.check_winner(0, "Y"))

    def test_check_winner_true(self):
        scene = Scene()
        for i in range(0, 4):
            scene.set_turn(i, "Y")
        self.assertEqual(True, scene.check_winner(1, "Y"))
