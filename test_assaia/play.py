

HEIGHT = 7
WIDTH = 7
NUMBERS_IN_LINE = 4
EMPTY_MARK = 0

DIGITS = {"R": 1, "B": 2, "G": 3}
MARKS = {EMPTY_MARK: "-", 1: "R", 2: "B", 3: "G"}
players_samples = [("Rich", "R"), ("Big", "B"), ("Great", "G")]


class SceneError(Exception):
    """
    This is the base class for all kinds of SceneErrors
    """
    pass


class Player(object):

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.digit = DIGITS.get(mark)

    def __str__(self):
        return self.name


class Scene(object):

    def __init__(self, **kw):
        self.height = kw.get("height") or HEIGHT
        self.width = kw.get("width") or WIDTH
        self.number_in_line = kw.get("nline") or NUMBERS_IN_LINE
        self._players = [Player(*players_sample) for players_sample in players_samples]
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

    def match_nearest(self, digit, cell, next_p):
        d = self.marks
        template = str(digit) * self.number_in_line
        vertical = ''.join(str(mark) for mark in d[cell])
        match = template in vertical
        if not match:
            horizontal = ''.join(str(d[i][next_p]) for i in range(0, self.width))
            match = template in horizontal
        if not match:
            # TODO: here should be smart counter for all these digits from the self.marks
            diagonal = ""
        return match

    def check_winner(self, name, cell, next_p):
        """
        horizontal, vertical or diagonal checking for NUMBERS_IN_LINE similar marks in line
        :return: result
        """
        digit = name.digit
        return self.match_nearest(digit, cell, next_p)

    def set_turn(self, turn, player):
        """
        setting the player turn
        :return: result
        """
        # gravitation's stroong
        current_length = sum([1 for cell in self.marks[turn] if cell != EMPTY_MARK])
        next_position = self.height - current_length - 1
        if next_position < 0:
            raise SceneError('Cannot add the turn')
        next_p = self.width - current_length - 1
        self.marks[turn][next_p] = player.digit
        return next_p

    def show_scene(self):
        """
        Show current state of the scene
        """
        for i in range(len(self.marks)):
            for j in range(len(self.marks[0])):
                print(MARKS.get(self.marks[j][i]), end=',')
            print('\n')


class GameOver(Exception):
    pass


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
                    cell = scene.set_turn(turn, name)
                    win = scene.check_winner(name, turn, cell)
                except SceneError:
                    print('Please, try again (wrong turn)')
                    continue
                if win:
                    scene.show_scene()
                    print(f'Player {name} won')
                    raise GameOver("Thank you and Good Luck")
                else:
                    break
            scene.show_scene()
