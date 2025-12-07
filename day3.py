import math 

def find_largest_12_digit_base10_num_in_list(lines):
    total_output_joltage = 0
    for line in lines:
        print("line: ",line)
        MAX_REQUIRED_DIGITS = 12
        digit_string = ""
        current_pos = 0

        # For each of the 12 digit positions we need to fill
        for digit_position in range(MAX_REQUIRED_DIGITS):
            print("digit_position: ",digit_position)
            # Calculate how many more digits we need after this one
            remaining_digits_needed = MAX_REQUIRED_DIGITS - digit_position - 1
            print("remaining digit needed: ",remaining_digits_needed)

            # search up to a position that leaves enough digits remaining
            search_end = len(line) - remaining_digits_needed
            print("search_end: ",search_end)

            # Find the maximum digit in the valid range
            max_digit = line[current_pos]
            print("max_digit: ",max_digit)
            index_of_max_digit = current_pos
            print("index_of_max: ",index_of_max_digit)

            for index in range(current_pos, search_end):
                print("index: ",index)
                if line[index] > max_digit:
                    max_digit = line[index]
                    index_of_max_digit = index
            print("index_of_max_digit",index_of_max_digit)
            # Add the max digit to our result
            digit_string += max_digit
            # Move past the position we just used
            current_pos = index_of_max_digit + 1

        total_output_joltage += int(digit_string)
    print(total_output_joltage)
    

list_max = []
sum = 0
with open("adventOfCodeDay3.txt") as file:
    lines = file.read().split("\n")
    # print(lines)
# lines = ["987654321111121"] 
    find_largest_12_digit_base10_num_in_list(lines)
        
        
        
        # print("block: ",line)

        # line = list(map(int,line))
        # tens_digit = -1
        # tens_index = -1
        # max_num = -1
        # for index, digit in enumerate(line[:len(line) - 1]):
        #     if digit > tens_digit:
        #         tens_digit = digit
        #         tens_index = index
        # for digit in line[tens_index+1:]:
        #     max_num = max(max_num, digit + (tens_digit * 10))
        # sum += max_num

        # print("tens_digit: ",tens_digit,"max: ",max_num)
        # print("sum: ",sum)