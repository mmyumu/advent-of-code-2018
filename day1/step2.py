
frequency = 0
frequencies = set()
with open('step2.input') as input:
    content = input.readlines()

    while True:
        for line in content:
            frequencies.add(frequency)
            print("Add {} to frequencies".format(frequency))
            frequency_modificator = line.strip()
            sign = frequency_modificator[0]
            number = int(frequency_modificator[1:])
            if sign == '+':
                frequency += number
            elif sign == '-':
                frequency -= number
            else:
                raise Exception('Sign ' + sign + ' not recognized')

            print(frequency)
            #print(frequencies)
            if frequency in frequencies:
                print("Result is {}".format(frequency))
                exit(0)
