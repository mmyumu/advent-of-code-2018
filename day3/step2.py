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

with open('step2.input') as input:
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
        m = re.search("^#(?P<id>\d+)\s@\s(?P<left>\d+),(?P<top>\d+):\s(?P<width>\d+)x(?P<height>\d+)$", line)
        claim_id = m.group('id')
        left = int(m.group('left'))
        top = int(m.group('top'))
        width = int(m.group('width'))
        height = int(m.group('height'))

        not_overlaping_claim = True
        for i in range(width):
            for j in range(height):
                square_inches[top + j][left + i] += 1

    for line in content:
        m = re.search("^#(?P<id>\d+)\s@\s(?P<left>\d+),(?P<top>\d+):\s(?P<width>\d+)x(?P<height>\d+)$", line)
        claim_id = m.group('id')
        left = int(m.group('left'))
        top = int(m.group('top'))
        width = int(m.group('width'))
        height = int(m.group('height'))

        not_overlaping_claim = True
        for i in range(width):
            for j in range(height):
                if square_inches[top + j][left + i] > 1:
                    not_overlaping_claim = False

        if not_overlaping_claim:
            print("Not overlaping claim ID={}".format(claim_id))