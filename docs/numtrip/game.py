board = [
    [2, 4, 1, 8, 8],
    [4, 2, 8, 2, 1],
    [4, 4, 8, 4, 2],
    [2, 8, 1, 4, 1],
    [2, 4, 4, 4, 4]
]

for zeile in board: #board wurde in den letzten Zeilen definiert
    for zelle in zeile:#Zellen und zeilen sind teile des Spielfelds
        print(' -', end='')#diese Zeile soll enden, wenn es keine zellen mehr in der Zeile darunter hat; für jede Zelle einen Strich
    print(' ')
    for zelle in zeile:
        print(f'|{zelle}', end='')# print neue zeile? auf jedenfall kommt vor jede zelle ein |
    print('|')#Am Schluss von jeder Zeile kommt noch ein |

for zelle in board[0]:
    print(' -', end='')# dieser teil ist noch der abschluss; die letzte Zeile wird seperat beschrieben
print(' ')