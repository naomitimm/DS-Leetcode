from collections import deque
q = deque([1, 3, 5, 7, 2, 4])

max_val = float('-inf')
for _ in range(len(q)):
    val = q.popleft()
    if val > max_val:
        max_val = val
    q.append(val)

print(q, max_val)
