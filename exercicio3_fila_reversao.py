from collections import deque

fila = deque()

fila.append(1)
fila.append(2)
fila.append(3)

fila.reverse()

for elemento in fila:
    print(elemento)