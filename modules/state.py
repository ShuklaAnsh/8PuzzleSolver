from typing import List

empty_space = ' '
top_i = [0, 1, 2]
left_i = [0, 3, 6]
bottom_i = [6, 7, 8]
right_i = [2, 5, 8]


class Position:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value


class Grid:

    def __init__(self, pieces: list):
        self.positions: List[Position] = []
        self.positions.append(Position(0, 0, pieces[0]))
        self.positions.append(Position(1, 0, pieces[1]))
        self.positions.append(Position(2, 0, pieces[2]))
        self.positions.append(Position(0, 1, pieces[3]))
        self.positions.append(Position(1, 1, pieces[4]))
        self.positions.append(Position(2, 1, pieces[5]))
        self.positions.append(Position(0, 2, pieces[6]))
        self.positions.append(Position(1, 2, pieces[7]))
        self.positions.append(Position(2, 2, pieces[8]))

    def get_pos(self, value):
        for position in self.positions:
            if position.value == value:
                return position


class State:
    #  pieces = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    #  board =
    #   [0][1][2]
    #   [3][4][5]
    #   [6][7][8]
    def __init__(self, pieces: list):
        assert len(pieces) == 9
        inf = float('inf')
        self.parent_state: State = None
        self.board = pieces
        self.h_score = inf
        # g = the number of nodes traversed from the start state to the current state
        self.g_score = inf
        self.f = inf

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError(f"Object is of type {type(other)}. Expected type {type(self)}")
        return self.board == other.board

    def empty_piece_idx(self):
        for i, piece in enumerate(self.board):
            if piece == empty_space:
                return i

    def stringify(self):
        state = ''
        for i, piece in enumerate(self.board):
            if i > 0 and i % 3 == 0:
                state += '\n'
            state += f'[{piece}]'
        return state

    def print_state(self):
        print(self.stringify())

    def swap_pieces(self, x, y):
        temp = self.board[x]
        self.board[x] = self.board[y]
        self.board[y] = temp

    def possible_moves(self):
        states: List[State] = []
        empty_i = self.empty_piece_idx()
        # Move blank_piece left
        if empty_i not in left_i:
            left_state = State(self.board.copy())
            left_state.swap_pieces(empty_i, empty_i - 1)
            states.append(left_state)
        # Move blank_piece up
        if empty_i not in top_i:
            up_state = State(self.board.copy())
            up_state.swap_pieces(empty_i, empty_i - 3)
            states.append(up_state)
        # Move blank_piece right
        if empty_i not in right_i:
            right_state = State(self.board.copy())
            right_state.swap_pieces(empty_i, empty_i + 1)
            states.append(right_state)
        # Move blank_piece down
        if empty_i not in bottom_i:
            down_state = State(self.board.copy())
            down_state.swap_pieces(empty_i, empty_i + 3)
            states.append(down_state)

        return states
