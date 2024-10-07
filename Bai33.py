from simpleai.search import SearchProblem, breadth_first

ACTIONS = {
    'up': (-1, 0),   # Di chuyển lên trên (giảm 1 hàng)
    'down': (1, 0),  # Di chuyển xuống dưới (tăng 1 hàng)
    'left': (0, -1), # Di chuyển sang trái (giảm 1 cột)
    'right': (0, 1)  # Di chuyển sang phải (tăng 1 cột)
}

def ShowTuple(my_tuple):
    my_string = ''
    for tuple in my_tuple:
        my_string += '( '
        for item in tuple:
            if item == -1:
                my_string += '  '
            else:
                my_string += str(item) + ' '
        my_string += ')\n'
    return my_string

init_matrix_2d = ((8, 1, 2),
                  (4, 6, -1),
                  (7, 5, 3))

matrix_GOAL = ((-1, 2, 3),
               (8, 1, 4),
               (7, 6, 5))

class TryToSolve(SearchProblem):
    def __init__(self, initial_state):
        super().__init__(initial_state)
        self.visited = []

    def actions(self, state):
        empty_row, empty_col = [(r, c) for r in range(3) for c in range(3) if state[r][c] == -1][0]
        possible_actions = []
        for action, (dy, dx) in ACTIONS.items():
            new_y = empty_row + dy
            new_x = empty_col + dx
            if 0 <= new_y < 3 and 0 <= new_x < 3:
                possible_actions.append(action)  
        return possible_actions
    
    def result(self, state, action):
        empty_row, empty_col = [(r, c) for r in range(3) for c in range(3) if state[r][c] == -1][0]
        copy_state = [list(row) for row in state]
        dy, dx = ACTIONS[action]
        new_y, new_x = empty_row + dy, empty_col + dx
        copy_state[empty_row][empty_col], copy_state[new_y][new_x] = copy_state[new_y][new_x], copy_state[empty_row][empty_col]
        return tuple(tuple(row) for row in copy_state)
    
    def is_goal(self, state):
        return state == matrix_GOAL
    
    def cost(self, state, action, state2):
        return 1

solver = TryToSolve(initial_state=init_matrix_2d)
solution = breadth_first(solver)

if solution:
    print("Path to solution:")
    for action, state in solution.path():
        ThisState = ShowTuple(state)
        print(f"Action: {action}, Resulting State:\n{ThisState}")

    print("Final State:", solution)
else:
    print("No solution")
