#!/usr/bin/env python3
#--------------------------------------------
# Advent of Code 2024
# Puzzle 2 12/2/24
# Shawn Kroeger
#--------------------------------------------
import sys

def parse_data():
    ''' Returns the contents of the input file in a list '''
    data = [[int(n) for n in line.split()] for line in open(sys.argv[1], "r").read().splitlines()]
    return data


def is_safe(row):
    ''' Returns True if the row of numbers meets the AoC Day 2 criteria, False if not.
        1) lists can increment or decrement, but not both
        2) no repeat numbers
        3) max distance between any two numbers is 3 '''
    inc = 0
    dec = 0
    dist = 0
    
    for i, val in enumerate(row[1:], start=1):
        prev = row[i-1]
        if (val == prev):  # duplicate values are not allowed
            return False
        
        elif (val < prev):
            if (inc == 1):  # Not allowed to both inc and dec
                return False
            dec = 1
                
        else: # val > prev
            if (dec == 1):  # Not allowed to both inc and dec
                return False
            inc = 1

        dist = abs(val-prev)
        if dist > 3:    # Max distance is 3
            return False
    else:   
        return True
    

def part1(inp):
    tot_safe = 0
    for row in inp:
        if is_safe(row):
            tot_safe += 1
    print ("Total safe values (part 1): {} ".format(tot_safe))
    

def part2(inp):
    ''' If removing any single number from a list makes it safe, declare the row safe '''
    tot_safe = 0
    for row in inp:
        if is_safe(row):
            tot_safe += 1
        
        else: # remove 1 element at a time and test again
            for i in range(len(row)):
                new_row = row.copy()
                new_row.pop(i)
                if is_safe(new_row):
                    tot_safe += 1
                    break
                
    print ("Total safe values (part 2): {} ".format(tot_safe))
    

if __name__ == "__main__":
    data = parse_data()
    part1(data)
    part2(data)
