
number_of_duplicates = 0
number_of_triplets = 0
with open('step1.input') as input:
    content = input.readlines()
    for line in content:
        box_id = line.strip()

        duplicate_found = False
        triplet_found = False
        for char in box_id:
            char_count = box_id.count(char)
            if char_count == 2:
                if not duplicate_found:
                    number_of_duplicates += 1
                duplicate_found = True
            elif char_count == 3:
                if not triplet_found:
                    number_of_triplets += 1
                triplet_found = True

result = number_of_duplicates * number_of_triplets
print("Result is {} x {} = {}".format(number_of_duplicates, number_of_triplets, result))