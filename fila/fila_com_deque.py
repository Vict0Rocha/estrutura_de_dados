from collections import deque

queue = deque()
queue.append('A')
queue.append('B')
queue.append('C')
print('Removendo: ', queue.popleft())
print('Removendo: ', queue.popleft())
# print('Removendo: ', queue.popleft())


# for item in queue:
#     print(item)
