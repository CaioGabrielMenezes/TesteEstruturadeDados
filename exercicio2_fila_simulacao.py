from collections import deque

fila = deque()

fila.append(1)
fila.append(2)

if fila:
    print(fila.popleft())