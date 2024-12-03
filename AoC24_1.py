#!/usr/bin/env python3
#--------------------------------------------
# Advent of Code 2024
# Puzzle 1 12/1/24
# Shawn Kroeger
#--------------------------------------------
import sys

def parse_data():
    ''' Returns the contents of the input file in a list '''
    l_lst = []
    r_lst = []
    
    with open(sys.argv[1], "r") as f:
        str_list = f.read().strip().split("\n")
    
    # convert input into two lists of ints (left and right) 
    for i in str_list:
        lt, rt = i.split("   ")
        l_lst.append(int(lt))
        r_lst.append(int(rt))
    
    # Lists have to be sorted smallest to biggest to get right answer for part 1
    l_lst.sort()
    r_lst.sort()
    
    return l_lst, r_lst


def part1(left, right):
    total = 0
    
    for i in range(len(left)):
        total += abs(right[i] - left[i])  # sometimes r < l
    print ("Part 1 = ", total)
    
    
def part2(left, right):
    occurrences = {}
    tot2 = 0
    
    # Count the number of times n occurs in lst
    def count_inst(n, lst):
        cnt = 0
        for i in lst:
            if i == n:
                cnt += 1
        return cnt
    
    for y in left:
        y_str = str(y)
        if y_str not in occurrences:
            # save number of times "L" occurs in "R" multiplied by "L" to save future search/math computations
            cnt_y = y * count_inst(y, right)
            occurrences[y_str] = cnt_y
        tot2 += occurrences[y_str]
        
    print ("Part 2 = ", tot2)
    

if __name__ == "__main__":
    l, r = parse_data()
    part1(l, r)
    part2(l, r)
