
with open('step2.input') as input:
    content = input.readlines()
    for line in content:
        box_id = line.strip()

        for other_line in content:
            if line == other_line:
                break
            other_box_id = other_line.strip()

            number_of_different_chars = 0
            
            index = 0
            for char1, char2 in zip(box_id, other_box_id):         
                if char1 != char2:
                    number_of_different_chars += 1
                    index_bad_char = index
                index += 1

            if number_of_different_chars == 1:
                print("Box IDS are {} and {}. Bad character index is {}".format(box_id, other_box_id, index_bad_char))
                result = box_id[:index_bad_char] + box_id[index_bad_char+1:]
                confirmation = other_box_id[:index_bad_char] + other_box_id[index_bad_char+1:]
                print("The result is {} (confirmation={})".format(result, confirmation))