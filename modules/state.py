"""
Object Classes written as part of Assignment 1
State, Grid, and Position used for representing the
8-Puzzle Problem

Objects in this file are imported and used by
puzzle_solver.py

Author: Ansh Shukla [V00816280]
Class: ECE 470
Date: July 20, 2020
"""


from typing import List

empty_space = ' '
top_indices = [0, 1, 2]
left_indices = [0, 3, 6]
bottom_indices = [6, 7, 8]
right_indices = [2, 5, 8]


class Position:
    """
    Position defines a piece's co-ordinates in the 8-Puzzle Problem
    This is used for calculating the Manhattan Distance Heuristic
    """
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value


class Grid:
    """
    Grid representation of a state. Initializes all the pieces as positions in a grid
    Used for calculating the Manhattan Distance between tiles
    """
    def __init__(self, pieces: list):
        assert len(pieces) == 9
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

    def get_pos(self, value) -> Position:
        """
        Returns the position of a piece that contains the value specified
        :param value: The value of the piece whose position is being retrieved
        :return: Position
        """
        for position in self.positions:
            if position.value == value:
                return position


class State:
    """
    Object representing a state of the 8-Piece Problem
    """
    def __init__(self, pieces: list):
        """
        Takes in an array of pieces and initializes the state

        If the pieces passed in are [0, 1, 2, 3, 4, 5, 6, 7, 8]
        They are represented as:
        [0][1][2]
        [3][4][5]
        [6][7][8]

        :param pieces: Pieces in order of configuration
        """
        assert len(pieces) == 9
        inf = float('inf')
        self.parent_state: State = None
        self.board = pieces
        self.h_score = inf
        # g = the number of nodes traversed from the start state to the current state
        self.g_score = inf
        self.f = inf

    def __eq__(self, other) -> bool:
        """
        Tells python how to properly compare two instances of a State
        :param other: The object being compared to this instance
        :return: True if the objects are equivalent, false otherwise
        """
        if not isinstance(other, type(self)):
            raise ValueError(f"Object is of type {type(other)}. Expected type {type(self)}")
        return self.board == other.board

    def generate_grid(self) -> Grid:
        """
        Generates a Grid instance of this State instance
        :return: The generated Grid
        """
        return Grid(self.board.copy())

    def empty_piece_idx(self) -> int:
        """
        Finds the index of the empty space in the board
        Used to determine possible moves for the empty space
        :return: The index of the empty space
        """
        for i, piece in enumerate(self.board):
            if piece == empty_space:
                return i

    def stringify(self) -> str:
        """
        Creates a human readable representation of the State instance
        :return: The string representation of the State instance
        """
        state = ''
        for i, piece in enumerate(self.board):
            if i > 0 and i % 3 == 0:
                state += '\n'
            state += f'[{piece}]'
        return state

    def print_state(self):
        """
        Prints the state in a human readable representation
        """
        print(self.stringify())

    def swap_pieces(self, x_idx, y_idx):
        """
        Swaps pieces in the board
        Used for moving around a piece (The empty piece)
        :param x_idx: The index of piece x
        :param y_idx: The index of piece y
        """
        temp = self.board[x_idx]
        self.board[x_idx] = self.board[y_idx]
        self.board[y_idx] = temp

    def possible_moves(self):
        """
        Determines the possible moves for the empty space
        :return: A list of possible states
        """
        states: List[State] = []
        empty_idx = self.empty_piece_idx()
        # Move blank_piece left
        if empty_idx not in left_indices:
            left_state = State(self.board.copy())
            left_state.swap_pieces(empty_idx, empty_idx - 1)
            states.append(left_state)
        # Move blank_piece up
        if empty_idx not in top_indices:
            up_state = State(self.board.copy())
            up_state.swap_pieces(empty_idx, empty_idx - 3)
            states.append(up_state)
        # Move blank_piece right
        if empty_idx not in right_indices:
            right_state = State(self.board.copy())
            right_state.swap_pieces(empty_idx, empty_idx + 1)
            states.append(right_state)
        # Move blank_piece down
        if empty_idx not in bottom_indices:
            down_state = State(self.board.copy())
            down_state.swap_pieces(empty_idx, empty_idx + 3)
            states.append(down_state)

        return states
