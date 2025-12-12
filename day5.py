
def verify_id_in_range(ranges_list, itemid_list):
    fresh_count = 0
    for id in itemid_list:
        for start, end in ranges_list:
            if start <= id <=end:
               fresh_count += 1 
               break 
    print("fresh_count: ",fresh_count)
            
def sum_of_ranges(range_tuple):
    sum = 0 
    sorted_list = []
    sorted_list = sorted(range_tuple, key=lambda x:x[0])
    # print("sorted_list: ",sorted_list)
    no_over_lapping = []
    i = 0 
    while i < len(sorted_list):
        # print("i: ",i)
        last = sorted_list[i][1]
        first = sorted_list[i][0]
        # print("new verify: ",first,last)
        for j in range(i,len(sorted_list) - 1):
            # print("current tuple: ",sorted_list[j])
            if last < sorted_list[j+1][0]:
                # print("last: ",last," bigger range: ",sorted_list[j+1][0])
                break
            else:
                i += 1
                if last < sorted_list[j+1][1]:
                    # print("new last: ",sorted_list[j+1][1] )
                    last = sorted_list[j+1][1]
                continue
        i += 1
        # print("first: ",first," last: ",last) 
        no_over_lapping.append((first,last))
    # print(no_over_lapping)

    sum = 0
    for k in range(len(no_over_lapping)):
        sum += no_over_lapping[k][1] - no_over_lapping[k][0] + 1
    print("sum: ",sum)

def main():
    with open("adventOfCodeDay5.txt") as file:
        lines = file.read().split("\n")
        # print(lines)
        ranges_list = []

        i = 0
        while lines[i] != '':
            i += 1
        ranges_list = lines[:i]
        range_tuple = []
        for ranges in ranges_list:
            temp_tuple = ranges.split("-")
            range_tuple.append((int(temp_tuple[0]),int(temp_tuple[1])))

        itemid_list= []
        for element in lines[i+1:]:
            itemid_list.append(int(element))

        # print(range_tuple)
        # print(itemid_list)
        # verify_id_in_range(range_tuple, itemid_list)
        sum_of_ranges(range_tuple)
            

if __name__ == "__main__":
    main()