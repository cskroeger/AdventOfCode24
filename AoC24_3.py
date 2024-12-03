#!/usr/bin/env python3
#--------------------------------------------
# Advent of Code 2024
# Puzzle 3 12/3/24
# Shawn Kroeger
#--------------------------------------------
import sys
import re

def parse_data():
    with open(sys.argv[1], "r") as f:
        return f.read()
    
def part1(data):
    total = 0
    happy = [(int(m.group(1)), int(m.group(2))) for m in re.finditer('mul\(([0-9]+),([0-9]+)\)', data)]
    for i in happy:
        total += i[0]*i[1]
    print ("Part 1:", total)

def part2(data):
    dos = data.split("do()")  # beginning of every string is valid until a "don't()" is hit
    total = 0
    for i in dos:
        donts = i.split("don't()")  # split on "don't()", then only use the first element of the list
        happy = [(int(m.group(1)), int(m.group(2))) for m in re.finditer('mul\(([0-9]+),([0-9]+)\)', donts[0])]
        for j in happy:
            total += j[0]*j[1]
    print ("Part 2:", total)

if __name__ == "__main__":
    data = parse_data()
    part1(data)
    part2(data)
