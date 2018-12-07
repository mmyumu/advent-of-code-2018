
frequency = 0

with open('step1.input') as input:
    content = input.readlines()
    for line in content:
        frequency_modificator = line.strip()
        sign = frequency_modificator[0]
        number = int(frequency_modificator[1:])
        if sign == '+':
            frequency += number
        elif sign == '-':
            frequency -= number
        else:
            raise Exception('Sign ' + sign + ' not recognized')

print("Result is {}".format(frequency))
