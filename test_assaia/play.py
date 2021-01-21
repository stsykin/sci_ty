

HEIGHT = 7
WIDTH = 7
NUMBERS_IN_LINE = 4
EMPTY_MARK = 0


class SceneError(Exception):
    """
    This is the base class for all kinds of SceneErrors
    """
    pass


class Scene(object):

    def __init__(self, **kw):
        self.height = kw.get("height") or HEIGHT
        self.width = kw.get("width") or WIDTH
        self.number_in_line = kw.get("nline") or NUMBERS_IN_LINE
        self._players = {'Yellow': "Y", "Green": "G"}
        self.marks = self.create_scene()

    @property
    def players(self):
        """
        Returns current users' with marks
        :return: dict with players
        """
        return self._players

    def create_scene(self):
        """
        Returns empty scene
        :return:
        """
        marks = []
        for i in range(0, self.width):
            marks.append([EMPTY_MARK for j in range(0, self.height)])
        return marks

    def check_winner(self, cell, name):
        """
        horizontal, vertical or diagonal checking for NUMBERS_IN_LINE similar marks in line
        :return: result
        """
        result = True if len([name for mark in self.marks[cell] if name == mark]) > self.number_in_line else False
        # TODO: check also vertical and diagonal matches
        if not result:
            pass
        return result

    def set_turn(self, turn, mark):
        """
        setting the player turn
        :return: result
        """
        current_length = sum([1 for cell in self.marks[turn] if cell != EMPTY_MARK])
        next_position = self.width - current_length - 1
        if next_position < 0:
            raise SceneError('Cannot add the turn')
        self.marks[turn][self.height - current_length - 1] = mark

    def show_scene(self):
        """
        Show current state of the scene
        """
        for i in range(len(self.marks[0])):
            for j in range(len(self.marks)):
                print(self.marks[i][j], end=',')
            print('\n')


if __name__ == '__main__':

    print(f"Let\'s play, my dear players {Scene.players}")
    num = input(f'Number of your scene? (number 4 to {HEIGHT}): ')
    num = int(num)
    scene = Scene(**{"height": num, "width": num})
    players = scene.players
    scene.show_scene()

    while True:
        for name in players:
            while True:
                ch = 0xFF
                if ch == 27:
                    break
                turn = input(f'Player {name}, your turn? (number 0 to {scene.width}, for every column): ')
                if not turn.isnumeric() or int(turn) > scene.width:
                    print('Try again (invalid position)')
                    continue
                try:
                    turn = int(turn)
                    mark = name[0]
                    ceil = scene.set_turn(turn, mark)
                    win = scene.check_winner(turn, mark)
                except SceneError:
                    print('Please, try again (wrong turn)')
                    continue
                if win:
                    print(f'Player {name} won')
                else:
                    break
            scene.show_scene()
