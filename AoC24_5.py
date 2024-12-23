#!/usr/bin/env python3
#--------------------------------------------
# Advent of Code 2024
# Puzzle 5 12/5/24
# Shawn Kroeger
#--------------------------------------------
import sys
from collections import deque

RULES = {}  # Each key's value is a list of numbers that must occur after the key itself in a given input
UPDATES = []
GOOD_UPDATES = []
FAILED_UPDATES = []

def parse_data():
    ''' Returns the contents of the input file in a list '''
    with open(sys.argv[1], "r") as f:
        sect1,sect2 = f.read().strip().split("\n\n")
    
    # Now divide section 1 & 2 into lists, separate by newlines
    rules = sect1.split("\n")
    update = sect2.split("\n")
    
    # Store Rules in a dictionary where the key is the first number, and values are
    #  a list of INTs that can later be compared.  This set of numbers should not be
    #  seen upon comparison, lest they indicate out-of-order rule violation
    for i in rules:
        key,val = i.split("|")
        if key in RULES:
            RULES[key].append(int(val))
        else:
            RULES[key] = [int(val)]
    #print("Rules:", RULES)    
    
    # Put the Input (2nd half section) into lists of INTs
    for u in update:
        UPDATES.append(list(map(int, u.split(","))))
    #print("UPDATES:", UPDATES)


# Returns the sum of all of the middle numbers in the input list of lists
def count_mids(list_of_lists):
    count = 0
    for i in list_of_lists:
        midIdx = (len(i)-1)/2  # -1 bc the 1st element is index 0
        count += i[int(midIdx)]
    return count


# Check that each number that comes after is in the right order, i.e. doesn't appear in the 
# dictionary entry whose key is that number
# Returns: True if update passed, else
#          False, failed comparison, index where comparison failed
def check_updates(in_list):
    for i, item in enumerate(in_list):
        for cmp in in_list[i+1:]:
            if (str(cmp) in RULES) and (item in RULES[str(cmp)]):  # failed rule check
                return False, cmp, i
    return True, 0, 0


# Re-order a given input list according to the rules in RULES
#  where a dictionary's key must come before each of the values in its list
def reorder_row(in_list):
    new_list = []
    q = deque()
    q.append(in_list)
    while len(q) > 0:
        new_list = q.pop()
        upd_passed, cmp, idx = check_updates(new_list)
        if upd_passed == False:
            new_list.remove(cmp)    # remove the failed compare from its current location
            new_list.insert(idx, cmp) # ... and insert before the thing it failed against
            q.append(new_list)      # Then re-run
            
    return new_list


def check_data():
    global GOOD_UPDATES, FAILED_UPDATES
    for row in UPDATES:
        upd_passed, x, i = check_updates(row)
        if (upd_passed == True):
            GOOD_UPDATES.append(row)
        else:
            new_row = reorder_row(row)
            FAILED_UPDATES.append(new_row)
    print("Part 1 Count:", count_mids(GOOD_UPDATES))
    print("Part 2 Count:", count_mids(FAILED_UPDATES))


if __name__ == "__main__":
    parse_data()
    check_data()
