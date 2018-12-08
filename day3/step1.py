import re

def print_array(array):
    for i in range(len(array)):
        line = ''
        for j in range(len(array[i])):
            line += str(array[i][j])
            #if array[i][j] ==:
                #line += '.'
                #print('.')
            #else:
                #line += '#'
                #print('#')
        print("i={:>4} => {}".format(i, line))

with open('step1.input') as input:
    content = input.readlines()

    square_inches = []

    x_dim = 0
    y_dim = 0
    for line in content:
        m = re.search("^(#\d+)\s@\s(?P<left>\d+),(?P<top>\d+):\s(?P<width>\d+)x(?P<height>\d+)$", line)
        left = int(m.group('left'))
        top = int(m.group('top'))
        width = int(m.group('width'))
        height = int(m.group('height'))

        if left + width > x_dim:
            x_dim = left + width

        if top + height > y_dim:
            y_dim = top + height

    square_inches = [[0 for x in range(x_dim)] for y in range(y_dim)]

    overlap = 0
    for line in content:
        m = re.search("^(#\d+)\s@\s(?P<left>\d+),(?P<top>\d+):\s(?P<width>\d+)x(?P<height>\d+)$", line)
        left = int(m.group('left'))
        top = int(m.group('top'))
        width = int(m.group('width'))
        height = int(m.group('height'))
        #print("{} => left={}, top={}, width={}, height={}".format(m.group(0), left, top, width, height))

        for i in range(width):
            for j in range(height):
                #print("left + i=", left + i)
                #print("top + j=", top + j)
                square_inches[top + j][left + i] += 1
    #print_array(square_inches)

    for x in range(len(square_inches)):
        for y in range(len(square_inches[x])):
            if square_inches[x][y] > 1:
                overlap += 1            

    print("Result is {}".format(overlap))