#!/usr/bin/env python3

"""
8-Puzzle Problem Solver written as part of Assignment 1
Uses A* and two separate heuristic functions to find the goal state

Author: Ansh Shukla [V00816280]
Class: ECE 470
Date: July 20, 2020
"""

from modules.state import State, Grid, empty_space, List


def h1(current_state: State) -> int:
    """
    This admissible heuristic function calculates the
    number of misplaces tiles in the current state
    :param current_state: The state to compare against the goal state
    :return: h_score
    """
    # h_score_1 = number of misplaced tiles
    h_score = 0
    for state_piece, goal_piece in zip(current_state.board, goal_state.board):
        if state_piece == empty_space:
            continue
        if state_piece != goal_piece:
            h_score += 1
    return h_score


def h2(current_state: State) -> int:
    """
    This admissible heuristic function calculates the
    total Manhattan distance between misplaced tiles
    :param current_state: The state to compare against the goal state
    :return: h_score
    """
    # h_score_2 = Manhattan Distance between misplaced nodes
    h_score = 0
    curr_grid: Grid = current_state.generate_grid()
    for goal_position in goal_grid.positions:
        curr_pos = curr_grid.get_pos(goal_position.value)
        h_score += (abs(curr_pos.x - goal_position.x) + abs(curr_pos.y - goal_position.y))
    return h_score


def reconstruct_path(end_state: State) -> List[State]:
    """
    Reconstructs the path taken from the start state to the goal state
    by going back and recording state's parents until the start state
    :param end_state: The state to start reconstructing from
    :return: The list of states progressed in order
    """
    path: List[State] = []
    curr_state = end_state
    while curr_state.parent_state is not None:
        path.append(curr_state.parent_state)
        curr_state = curr_state.parent_state
    path.reverse()
    path.append(goal_state)
    return path


def print_initial_states():
    """
    Convenience function to print out goal and start states
    """
    print("Goal State:")
    goal_state.print_state()
    print("\nStart State:")
    start_state.print_state()
    print()


def a_star(h) -> List[State]:
    """
    A Star Algorithm implemented via pseudo-code found at:
    https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode

    as well as email hints from Professor Deepali Arora (UVic)

    :param h: Heuristic Function to use to calculate h_score
    :return: A path list to goal state
    """
    g_score = 0
    open_list: List[State] = [start_state]
    closed_list: List[State] = []
    while len(open_list) > 0:
        g_score += 1
        # Sort open list by f() value of state
        open_list.sort(key=lambda x: x.f, reverse=True)
        current = open_list.pop()

        print("Current State:")
        current.print_state()
        print()

        if current == goal_state:
            return reconstruct_path(current)
        print("Expanded States:")
        for expanded_state in current.possible_moves():
            if expanded_state not in closed_list:
                # Add explored state to closed list to reduce analyzing again
                closed_list.append(expanded_state)
                # If g_score to path better than its current recorded g_score
                if g_score < expanded_state.g_score:
                    # Record g_score
                    expanded_state.parent_state = current
                    expanded_state.g_score = g_score
                    expanded_state.h_score = h(expanded_state)
                    # Calculated f = g + h
                    expanded_state.f = expanded_state.g_score + expanded_state.h_score
                    expanded_state.print_state()
                    print(f'g={expanded_state.g_score} h={expanded_state.h_score} f={expanded_state.f}\n')

                    if expanded_state not in open_list:
                        open_list.append(expanded_state)
    print("no path found")
    return []


if __name__ == '__main__':
    goal_state = State([1, 4, 7, 2, 5, 8, 3, 6, empty_space])
    goal_grid: Grid = goal_state.generate_grid()

    # Assignment input
    # start_state = State([7, 4, 5, 2, empty_space, 6, 8, 3, 1])
    # Test Input 1
    # start_state = State([1, 4, 7, 2, 5, 8, empty_space, 3, 6])
    # Test Input 2
    start_state = State([4, empty_space, 7, 1, 5, 8, 2, 3, 6])
    # Test Input 3
    # start_state = State([4, 7, 6, 1, empty_space, 5, 2, 8, 3])

    print("Finding solution using h() = number of misplaced tiles")
    print_initial_states()
    h1_path = a_star(h1)
    print("Solution:")
    for state in h1_path:
        state.print_state()
        print('')

    print("Finding solution using h() = Manhattan Distance between misplaced tiles")
    print_initial_states()
    h1_path = a_star(h2)
    print("Solution:")
    for state in h1_path:
        state.print_state()
        print('')
