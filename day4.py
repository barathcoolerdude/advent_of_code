# with open("adventOfCodeDay4.txt") as file:
#     lines = file.read().split("\n")
#     for line in lines:
#         print("line: ",line)


# def find_accessable_rolls(lines):
#     sum = 0
#     for i in range(len(lines)):
#         for j in range(len(lines[i])):
#             if(lines[i][j] == "x" or lines[i][j] == "@"):
#                 count = 0
#                 for k in range(-1,2):
#                     for l in range(-1,2):
#                         if(k+i <= -1 or k+i >= len(lines) or l+j <= -1 or l+j >= len(lines[i])):
#                             continue
#                         if(k == 0 and l == 0):
#                             continue
#                         if(lines[i+k][j+l] == "@" or lines[i+k][j+l] == "x"):
#                             # print("\n success: i: ",i," j: ",j)
#                             count += 1
#                         # print()
#                 if(count < 4):
#                     sum += 1
#                 # print("count: ",count)
#     print("sum: ",sum)                       

global_sum = 0
def find_accessable_rolls_rec(lines):
    global global_sum
    position = []
    seperated_list = []
    for i in range(len(lines)):
        # print("lines[i]: ",lines[i])
        for j in range(len(lines[i])):
            if(lines[i][j] == "x" or lines[i][j] == "@"):
                count = 0
                for k in range(-1,2):
                    for l in range(-1,2):
                        if(k+i <= -1 or k+i >= len(lines) or l+j <= -1 or l+j >= len(lines[i])):
                            continue
                        if(k == 0 and l == 0):
                            continue
                        if(lines[i+k][j+l] == "@" or lines[i+k][j+l] == "x"):
                            # print("target: ",i,j)
                            # print("roll present slot: ","lines[i+k][j+l]: ",i+k,j+l)
                            count += 1
                # print("count: ",count)
                if(count < 4):
                    position.append((i,j))
                    global_sum += 1
    print("sum: ",global_sum)                      

    if not position:
        return
    for line in lines:
        seperated_list.append(list(line))
    # print(seperated_list)
    for index, slot in position:
        seperated_list[index] [slot] = "."
    # print(seperated_list)
    seperated_list = ["".join(row) for row in seperated_list]
    return find_accessable_rolls_rec(seperated_list)


def main():
    with open("adventOfCodeDay4.txt") as file:
        lines = file.read().split("\n")
        # find_accessable_rolls(lines)
        find_accessable_rolls_rec(lines)

if __name__ == "__main__" :
    main()
    
    

   