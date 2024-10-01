# # home_work 7
""" Игра-лабиринт."""

maze = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', 'E', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '#', '#', '#'],
        ['#', ' ', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '#', '#', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '0', '#', '#', '#']
]
def print_maze(maze):
    for row in maze:
        print(' '.join(row))
      
def win_condition(maze):
    if "0" not in maze:
        return True
      
def find_exit(maze, x, y):
    i = 0
    player = "E"
    print_maze(maze)
    print(f'\nВы сейчас находитесь в лабиринте, Ваше местонахождение помечено символом "E". Сделайте следующий ход!\nВарианты ходов:')
    print('"A" - влево 1 шаг\n"D" - вправо 1 шаг\n"W" - вверх 1 шаг\n"S" - вниз 1 шаг')
    action = input('Ваш ход: ')
    if action != "A" and action != "D" and action != "W" and action != "S":
        print('mistake! Try again! Только заглавные буквы!!!')
        return find_exit(maze, x, y)
    if action == "A":
        if maze[x][y-1] == " ":
            maze[x][y-1] = player
            maze[x][y] = "-"
            y = y-1
            player = maze[x][y]
            find_exit(maze, x, y)
        elif maze[x][y-1] == "0":
            maze[x][y-1] = player
            maze[x][y] = "-"
        else:
            print('Это СТЕНА! Выберите другой ход!')
            find_exit(maze, x, y)
        i += 1
    if action == "D":
        if maze[x][y+1] == " ":
            maze[x][y+1] = player
            maze[x][y] = "-"
            y = y + 1
            player = maze[x][y]
            find_exit(maze, x, y)
        elif maze[x][y+1] == "0":
            maze[x][y+1] = player
            maze[x][y] = "-"
        else:
            print('Это СТЕНА! Выберите другой ход!')
            find_exit(maze, x, y)
        i += 1
    if action == "W":
        if maze[x-1][y] == " ":
            maze[x-1][y] = player
            maze[x][y] = "-"
            x = x - 1
            player = maze[x][y]
            find_exit(maze, x, y)
        elif maze[x-1][y] == "0":
            maze[x-1][y] = player
            maze[x][y] = "-"
        else:
            print('Это СТЕНА! Выберите другой ход!')
            find_exit(maze, x, y)
        i += 1
    if action == "S":
        if maze[x+1][y] == " ":
            maze[x+1][y] = player
            maze[x][y] = "-"
            x = x + 1
            player = maze[x][y]
            find_exit(maze, x, y)
        elif maze[x+1][y] == "0":
            maze[x+1][y] = player
            maze[x][y] = "-"
        else:
            print('Это СТЕНА! Выберите другой ход!')
            find_exit(maze, x, y)
        i += 1
    if win_condition(maze):
        print(f'Ура, вы победили!!! Количество шагов: {i}')
    else:
        print('Вы не смогли выйти из лабиринта!')
find_exit(maze, x=1, y=2)
