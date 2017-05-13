from collections import deque

d = deque(["task1","task2","task3"])
d.append("task4")
print("Handling", d.popleft())
print("Handling1", d.pop())
#深度优先算法
