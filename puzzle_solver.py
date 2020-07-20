from modules.state import State, Grid, empty_space, List


def h1(current_state: State):
    # h_score_1 = number of misplaced tiles
    h_score = 0
    for state_piece, goal_piece in zip(current_state.board, goal_state.board):
        if state_piece == empty_space:
            continue
        if state_piece != goal_piece:
            h_score += 1
    return h_score


def h2(current_state: State):
    # h_score_2 = Manhattan Distance between misplaced nodes
    h_score = 0
    curr_grid = Grid(current_state.board.copy())
    for goal_position in goal_grid.positions:
        curr_pos = curr_grid.get_pos(goal_position.value)
        h_score += (abs(curr_pos.x - goal_position.x) + abs(curr_pos.y - goal_position.y))
    return h_score


def reconstruct_path(end_state: State):
    path: List[State] = []
    curr_state = end_state
    while curr_state.parent_state is not None:
        path.append(curr_state.parent_state)
        curr_state = curr_state.parent_state
    path.reverse()
    path.append(goal_state)
    return path


def a_star(h):
    """
    A Star Algorithm implemented via pseudo-code found at:
    https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode

    :param h: Heuristic Function to use
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

        if current == goal_state:
            return reconstruct_path(current)

        for expanded_state in current.possible_moves():
            if expanded_state not in closed_list:
                closed_list.append(expanded_state)
                if g_score < expanded_state.g_score:
                    expanded_state.parent_state = current
                    expanded_state.g_score = g_score
                    expanded_state.h_score = h(expanded_state)
                    expanded_state.f = expanded_state.g_score + expanded_state.h_score
                    if expanded_state not in open_list:
                        open_list.append(expanded_state)
    print("no path found")
    return []


if __name__ == '__main__':
    goal_state = State([1, 4, 7, 2, 5, 8, 3, 6, empty_space])
    goal_grid = Grid(goal_state.board.copy())

    # Assignment input
    # start_state = State([7, 4, 5, 2, empty_space, 6, 8, 3, 1])
    # Test Input 1
    # start_state = State([1, 4, 7, 2, 5, 8, empty_space, 3, 6])
    # Test Input 2
    # start_state = State([4, empty_space, 7, 1, 5, 8, 2, 3, 6])
    # Test Input 3
    start_state = State([4, 7, 6, 1, empty_space, 5, 2, 8, 3])

    print("H1:")
    h1_path = a_star(h1)
    for state in h1_path:
        state.print_state()
        print('')

    print("H2:")
    h1_path = a_star(h2)
    for state in h1_path:
        state.print_state()
        print('')

    # states = start_state.possible_moves()
    # for state in states:
    #     state.f = h1(state)
    #     state.print_state()
    #     print("f =", state.f)
    #
    # print("\nsorted")
    # states.sort(key=lambda x: x.f, reverse=True)
    # for state in states:
    #     state.f = h1(state)
    #     state.print_state()
    #     print("f =", state.f)
    #
    # print("\npopped")
    # current = states.pop()
    # current.print_state()
