# write your code here
x = [' ', ' ', ' ']
y = [' ', ' ', ' ']
z = [' ', ' ', ' ']

print('---------')
print('|', x[0], x[1], x[2], '|')
print('|', y[0], y[1], y[2], '|')
print('|', z[0], z[1], z[2], '|')
print('---------')

count_x_o, count_x, count_o = 0, 0, 0


def solve_tic(coordinate, count_x_o, m, count_x, count_o):
    try:
        coordinates = [int(i) for i in coordinate.split()]
    except ValueError:
        return 'not_number'
    else:
        a = coordinates[0]
        b = coordinates[1]
        if 1 <= a <= 3 and 1 <= b <= 3:

            if m[a - 1][b - 1] in ('O', 'X'):
                return 'occupied'
            else:
                if count_x_o % 2 == 0:
                    m[a - 1][b - 1] = 'X'
                    count_x += 1
                else:
                    m[a - 1][b - 1] = 'O'
                    count_o += 1

                count_x_o += 1  # count X and O

                print('---------')
                print('|', m[0][0], m[0][1], m[0][2], '|')
                print('|', m[1][0], m[1][1], m[1][2], '|')
                print('|', m[2][0], m[2][1], m[2][2], '|')
                print('---------')

                # checking cross
                if m[0][0] == m[1][1] == m[2][2] or m[0][2] == m[1][1] == m[2][0]:
                    return f'{m[1][1]} wins'

                # checking rows
                for i in range(3):
                    if m[i][0] == m[i][1] == m[i][2]:
                        return f'{m[i][0]} wins'

                for j in range(3):
                    if m[0][j] == m[1][j] == m[2][j]:
                        return f'{m[0][j]} wins'

                if count_x + count_o == 9:
                    return 'Draw'

        else:
            return 'coordinates'


while True:
    m = [x, y, z]
    coordinate = input('Enter the coordinates: ')
    count_x = x.count('X') + y.count('X') + z.count('X')
    count_o = x.count('O') + y.count('O') + z.count('O')
    sol = solve_tic(coordinate, count_x_o, m, count_x, count_o)

    if sol == 'not_number':
        print('You should enter numbers!')
    elif sol == 'occupied':
        print('This cell is occupied! Choose another one!')
    elif sol == 'coordinates':
        print('Coordinates should be from 1 to 3!')
    elif sol == '  wins' or sol is None:
        count_x_o += 1
        continue
    else:
        print(sol)
        break
