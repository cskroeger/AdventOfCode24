#!/usr/bin/env python3
#--------------------------------------------
# Advent of Code 2024
# Puzzle 4 12/4/24
# Shawn Kroeger
#--------------------------------------------
import sys

DATA = [] # a list where each row of the input file is an entry
NUM_ROW = 0
NUM_COL = 0
SOLUTIONS = []

def parse_data():
    global DATA, NUM_ROW, NUM_COL
    with open(sys.argv[1], "r") as f:
        DATA = f.read().strip().split("\n")
    NUM_ROW = len(DATA)
    NUM_COL = len(DATA[0])


def get_next_letter(inp):
    match inp:
        case "X": next_letter = "M"
        case "M": next_letter = "A"
        case "A": next_letter = "S"
        case "S": next_letter = ""
    return next_letter


# Rotate Clockwise around an origin point
# Return a list of coordinates around that point that have the input letter 'cmp'
def get_next_coords(coord, cmp):
    global DATA, NUM_ROW, NUM_COL
    rtn = []
    #      0      1     2
    # 0) -1,-1  0,-1  1,-1
    # 1) -1, 0  orig  1, 0
    # 2) -1, 1  0, 1  1, 1
    loc = [(-1,0), (-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)] # (x,y) relative locations
    for i in loc:
        x = coord[0] + i[0]
        y = coord[1] + i[1]
        if ((x >= 0) and (x < NUM_COL) and (y >= 0) and (y < NUM_ROW)):
            if (DATA[y][x] == cmp):
                rtn.append((x,y))
    #print (rtn)
    return rtn


# Fix the solutions.  I.e. limit the correct answers to ones where the answers are in 
#   a straight line.
def chk_soln(inp):
    dir_x = inp[1][0] - inp[0][0]
    dir_y = inp[1][1] - inp[0][1]
    if ((inp[2][0] - inp[1][0] == dir_x) and
        (inp[3][0] - inp[2][0] == dir_x) and
        (inp[2][1] - inp[1][1] == dir_y) and
        (inp[3][1] - inp[2][1] == dir_y)):
        return True
    else:
        return False


# Recursively find XMAS patterns, adding each solution to SOLUTIONS
# This solution allows "XMAS" to be found in ways that are not strictly a straight line.
# i.e. M can be moving in the x direction, then A in the y, then S in a diagonal from there
# That's not what the problem asked for, the the answer needs to be post-processed-fixed.
def search_xmas(coords):
    global DATA, SOLUTIONS
    curr_letter = DATA[coords[-1][1]] [coords[-1][0]]
    
    if curr_letter == "S":
        if (chk_soln(coords)):
            SOLUTIONS.append(coords)  # Found a solution!
    else:
        nl = get_next_letter(curr_letter)
        next_coords = get_next_coords(coords[-1],nl)
        if next_coords != []:  # i.e. not a dead end
            for nc in next_coords:
                search_list = coords.copy()
                search_list.append(nc)
                search_xmas(search_list)  # recurse!


def part1():
    global DATA
    solutions = 0
    x_list = []
    for y, row in enumerate(DATA):
        for x, col in enumerate(row):
            # Find each X; use as a starting point for a search
            if col == "X":
                x_list.append((x,y))
    
    # count number of items in list        
    for Xs in x_list:
        search_xmas([Xs])
    print ("Total XMAS solutions (part 1): {} ".format(len(SOLUTIONS)))

    
# Returns True if MAS found in an X pattern around a central A
# Else returns False
# 1 2    -> Positions 1 & 2
#  A
# 3 4    -> Positions 3 & 4
def check_x(i): 
    x,y = i   # i is an (x,y) coordinate
    
    pos1 = DATA[y-1][x-1] # DATA is accessed "DATA[y][x]"
    pos2 = DATA[y-1][x+1]
    pos3 = DATA[y+1][x-1]
    pos4 = DATA[y+1][x+1]
    
    if (((pos1 == "M" and pos4 == "S") or (pos1 == "S" and pos4 == "M")) and
        ((pos2 == "M" and pos3 == "S") or (pos2 == "S" and pos3 == "M"))):
        return True
    else:
        return False


def part2():
    global DATA, NUM_ROW, NUM_COL
    solutions = 0
    a_list = []
    for y, row in enumerate(DATA):
        if y == 0 or y == NUM_ROW-1:  # Looking for an "A" with room above and below for the "X"
            continue
        for x, col in enumerate(row):
            if x == 0 or x == NUM_COL-1:
                continue
            # Find each A; use as a starting point for a search
            if col == "A":
                a_list.append((x,y))
    
    for As in a_list:
        if check_x(As):
            solutions += 1
    print ("Total XMAS solutions (part 2): {} ".format(solutions))


if __name__ == "__main__":
    data = parse_data()
    part1()
    part2()
