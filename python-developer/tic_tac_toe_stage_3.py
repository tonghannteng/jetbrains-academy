# write your code here
cells = input('Enter cells:')
count_x = cells.count('X')
count_o = cells.count('O')

first_row, second_row, third_row = cells[:3], cells[3: 6], cells[6: 9]

print('---------')
print('|', first_row[0], first_row[1], first_row[2], '|')
print('|', second_row[0], second_row[1], second_row[2], '|')
print('|', third_row[0], third_row[1], third_row[2], '|')
print('---------')

x = [first_row[0], first_row[1], first_row[2]]
y = [second_row[0], second_row[1], second_row[2]]
z = [third_row[0], third_row[1], third_row[2]]

list_test = []


def solve():
    # checking cross
    if x[0] == y[1] == z[2] or x[2] == y[1] == z[0]:
        return str(x[0]) + ' wins'

    # checking impossible condition
    if abs(count_o - count_x) > 1:
        return 'Impossible'

    # checking rows
    if x[0] == x[1] == x[2]:
        list_test.append(str(x[0]) + ' wins')

    if y[0] == y[1] == y[2]:
        list_test.append(str(y[0]) + ' wins')

    if z[0] == z[1] == z[2]:
        list_test.append(str(z[0]) + ' wins')

    if x[0] == y[0] == z[0]:
        list_test.append(str(x[0]) + ' wins')

    if x[1] == y[1] == z[1]:
        list_test.append(str(x[1]) + ' wins')

    if x[2] == y[2] == z[2]:
        list_test.append(str(x[2]) + ' wins')

    if len(list_test) > 1:
        return 'Impossible'
    elif len(list_test) == 1:
        return list_test[0]

    if count_x + count_o == 9:
        return 'Draw'


obj = solve()

if obj is None:
    print('Game not finished')
else:
    print(obj)
