# def typing_time(layout, word):
    # solution1 : loop 2 times; So this is O(n*m) ,space O(1); 
    # curr_pos = 0
    # total_time = 0

    # for letter in word:
    #     letter_pos = 0
    #     for key in layout:
    #         if key == letter:
    #             break
    #         letter_pos += 1 # letter postion found

    #     time = abs(letter_pos - curr_pos)
    #     total_time += time
    #     curr_pos = letter_pos
    
    # return total_time
    
    # solution2 : enumerate way，时间复杂度说、变成了o（n），空间复杂度o（n）
    # positions = {letter : pos for pos, letter in enumerate(layout)} #  a : 0, "b" : 1
    # # 快速建立dic的方法
    # location = 0
    # typed_time = 0

    # for letter in word:
    #     next_loc = positions[letter]
    #     time = abs(next_loc - location)
    #     typed_time += time
    #     location = next_loc
    
    # return typed_time
    

# tc - O(n + m) where n = len(word) still O(n)
# sc - O(m) where m = len(layout)



# skipping error handling
# empty keys? empty word? repeated letters in keys?

def typing_time(layout, word):
    curr_pos = 0
    total_time = 0

    for letter in word:
        letter_pos = 0
        for k in layout:
            if letter == k:
                break
            else:
                letter_pos += 1

        time = abs(letter_pos - curr_pos)
        total_time += time
        curr_pos = letter_pos

    return total_time

