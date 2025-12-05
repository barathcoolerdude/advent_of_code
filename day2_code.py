import math
# def remove_zero(string):
#     if not string.startswith("0"):
#         return 
#     s=s[1:]
    
# with open("adventOfCodeDay2.txt") as file:
#     for line in file:
#         arr = line.strip().split(",")
#         print(arr)
#         sum = 0
# # arr=['11-22',"95-115","998-1012","1188511880-1188511890","222220-222224","1698522-1698528","446443-446449","38593856-38593862"]
#         for ranges in arr:
#             splite = ranges.split("-")
#             remove_zero(splite[0]) # 95
#             remove_zero(splite[1]) # 110
#             position = int(splite[0])
#             while position <= int(splite[1]) :
#                 if(str(position)[:len(str(position))//2] == str(position)[len(str(position))//2:]):
#                     sum += position
#                     print(sum)

#                 position += 1
# print("sum: ",sum)
                    
def series_check(digit, series, length):
    # print("digit: ",digit,"series: ",series,"i: ",length)
    check = 1
    for i in range(math.ceil(len(digit)/length)-1):
        # print("sequence: ",i," ",digit[i*length:(i+1)*length])
        # print("sequence: ",i," ",digit[(i+1)*length:(i+2)*length])
        if(digit[i*length:(i+1)*length] != digit[(i+1)*length:(i+2)*length]):
            check = 0
            break
    return check

 
def find_repeat(position):
    digit = str(position)
    half_len = math.floor(len(digit)/2)
    # print("half_len: ",half_len)
    check = 0
    for i in range(1,half_len+1):
        # print("first half: ",digit[:i])
        # print("second half: ",digit[i:i+i])
        if(digit[:i]==digit[i:i+i]):
            result = series_check(digit,digit[:i], i)
            if result == 1:
                print("sucess position:",position)
                check = 1
                break 
    return check

with open("adventOfCodeDay2.txt") as file:
    for line in file:
        arr = line.strip().split(",")
sum = 0 
# arr = ["11-22","95-115","998-1012","1188511880-1188511890","222220-222224","1698522-1698528","446443-446449","38593856-38593862","565653-565659","824824821-824824827","2121212118-2121212124"]
# arr1 = ["12-21"]
for ranges in arr:
            # print("new range")
            split_range = ranges.split("-")
            print(split_range[0], split_range[1])
            position = int(split_range[0])
            while position <= int(split_range[1]):
                # print("position: ",position)
                find_check = find_repeat(position)
                if find_check == 1:
                    sum += position
                position += 1
                
print("sum: ",sum)
