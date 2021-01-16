# write your code here

cells = input('Enter cells: ').replace('_', ' ')

first_row, second_row, third_row = cells[:3], cells[3: 6], cells[6: 9]

x = [first_row[0], first_row[1], first_row[2]]
y = [second_row[0], second_row[1], second_row[2]]
z = [third_row[0], third_row[1], third_row[2]]

print('---------')
print('|', x[0], x[1], x[2], '|')
print('|', y[0], y[1], y[2], '|')
print('|', z[0], z[1], z[2], '|')
print('---------')

nested_state = [x, y, z]

while True:
    coordinate = input('Enter the coordinates: ')
    try:
        coordinates = [int(i) for i in coordinate.split()]
    except ValueError:
        print('You should enter numbers!')
    else:
        a = coordinates[0]
        b = coordinates[1]
        if 1 <= a <= 3 and 1 <= b <= 3:

            if nested_state[a - 1][b - 1] in ('O', 'X'):
                print('This cell is occupied! Choose another one!')
            else:

                nested_state[a - 1][b - 1] = 'X'

                print('---------')
                print('|', nested_state[0][0], nested_state[0][1], nested_state[0][2], '|')
                print('|', nested_state[1][0], nested_state[1][1], nested_state[1][2], '|')
                print('|', nested_state[2][0], nested_state[2][1], nested_state[2][2], '|')
                print('---------')
                break
        else:
            print('Coordinates should be from 1 to 3!')


