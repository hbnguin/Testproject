from simpleai.search import SearchProblem, astar
import itertools

# Định nghĩa bài toán 8 quân hậu bằng cách kế thừa SearchProblem
class EightQueensProblem(SearchProblem):
    def actions(self, state):
        # Các hành động là thêm một quân hậu vào hàng tiếp theo
        if len(state) == 8:  # Nếu đã đặt đủ 8 quân hậu, không cần thêm
            return []
        else:
            # Trả về tất cả các cột có thể đặt cho hàng tiếp theo
            return [col for col in range(8) if col not in state]

    def result(self, state, action):
        # Trả về trạng thái mới khi đặt thêm một quân hậu vào hàng tiếp theo
        return state + (action,)

    def is_goal(self, state):
        # Đích là khi có 8 quân hậu và không có xung đột
        return len(state) == 8 and self._count_conflicts(state) == 0

    def _count_conflicts(self, state):
        """Đếm số cặp quân hậu có thể tấn công nhau."""
        conflicts = 0
        for (r1, c1), (r2, c2) in itertools.combinations(enumerate(state), 2):
            if abs(r1 - r2) == abs(c1 - c2):  # Trùng đường chéo
                conflicts += 1
        return conflicts

    def heuristic(self, state):
        # Heuristic là số lượng xung đột hiện tại
        return self._count_conflicts(state)


# Khởi tạo trạng thái ban đầu là bàn cờ trống
initial_state = ()

# Tạo bài toán 8 quân hậu
problem = EightQueensProblem(initial_state)

# Giải bài toán bằng A*
result = astar(problem)

# In kết quả
print("Vị trí của 8 quân hậu trên bàn cờ (theo hàng và cột):")
for row, col in enumerate(result.state):
    print(f"Hàng {row}, Cột {col}")
