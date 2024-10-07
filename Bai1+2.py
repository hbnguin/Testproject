graph = {
    1: [2, 3, 5],
    2: [1, 4],
    3: [1, 4, 5],
    4: [2, 3, 5],
    5: [1, 3, 4]
}
#Function Ho Tro
def IsFind(check):
    if (check) :
        return "Found"
    else:
        return "Not Found"
    
def ShowValues(my_list):
    print('{', end=' ')
    for item in my_list:
        print(f'{item}',end=' ')
    
    print('}')
# Bai 1
#1
def BFS (goal):
    queue = []
    queue.append(1) # Thêm đỉnh 1, xet cac dinh xung quanh dinh 1
    closed = [1]; #Nhung dinh da duyet qua
    while(len(queue)):
        ShowValues(queue)
        value = queue.pop(0)#1
        if(value == goal): return True
        for item in graph[value]: #graph[1]
            if(item not in closed):
                closed.append(item)
                queue.append(item)
    return False
#2
def UCS (goal):
    queue = []
    queue.append(1) # Thêm đỉnh 1
    closed = [1];
    while(len(queue)):
        queue.sort()
        ShowValues(queue)
        value = queue.pop(0)
        if(value == goal): return True
        for item in graph[value]:
            if(item not in closed):
                closed.append(item)
                queue.append(item)
    return False
#3 DFS
def DFS(goal):
    stack = []
    stack.append(1)
    closed = [1]
    while(len(stack)):
        ShowValues(stack)
        value = stack.pop()
        if(value == goal): return True
        for item in graph[value]:
            if(item not in closed):
                closed.append(item)
                stack.append(item)
    return False
#4 IDS
def DFS_Limited(goal, max_depth):
    stack = []
    stack.append((1, 0))
    closed = []
    while(len(stack)):
        ShowValues(stack)
        value, depth = stack.pop()
        if(value == goal): return True
        if(depth < max_depth):
            for item in graph[value]:
                if(item not in closed):
                    closed.append((item, depth + 1))
                    stack.append((item, depth + 1))
    return False
    
def IDS(goal): #Khong gioi han Depth
    for depth in range(10): #Tim kiem het
        print(f"Depth: {depth}")
        if(DFS_Limited(goal, depth)):
            return True
        
    return False
#5 DLS
def DLS(goal, max_depth): #Gioi Han Depth
    for depth in range(max_depth + 1):
        print(f"Depth: {depth}")
        if DFS_Limited(goal, depth): 
            print(f"Goal {goal} found at depth {depth}")
            return True        
    
    print(f"Goal {goal} not found within depth {max_depth}")
    return False

# 2 7 8
# 3 -1 4
# 5 6 1


goal = 4
max_depth = 3
print(f'goal:{goal} | max_depth:{max_depth}')
print('This is BFS: ')
print(IsFind(BFS(goal)))
print('This is UCS: ')
print(IsFind(UCS(goal)))
print('This is DFS: ')
print(IsFind(DFS(goal)))
print('This is IDS: ')
print(IsFind(IDS(goal)))
print('This is DLS')
print(IsFind(DLS(goal, max_depth)))
#Bai 2
from collections import deque
from simpleai.search import SearchProblem, breadth_first, depth_first, astar
GOAL = 'HELLO WORLD'

class HelloProblem(SearchProblem):
    def actions(self, state):                                                                                             
        if state is None or len(state) >= len(GOAL):
            return []
        return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    def result(self, state, action):
        new_state = state + action
        if GOAL.startswith(new_state):
            return new_state
        else:
            return None
    
    def is_goal(self, state):
        return state == GOAL

    def cost(self, state, action, state2):
        return 1
    
# Tạo đối tượng vấn đề
my_problem = HelloProblem(initial_state='')

# Thực hiện tìm kiếm bằng giải thuật breadth-first
result = breadth_first(my_problem)

# Kiểm tra xem có tìm được giải pháp hay không
if result:
    # In ra đường đi dẫn đến mục tiêu
    print("Path to solution:")
    for action, state in result.path():
        print(f"Action: {action}, Resulting State: {state}")

    # In ra trạng thái cuối cùng
    print("Final State:", result.state)
else:
    print("No solution found!")

#Bai 3
