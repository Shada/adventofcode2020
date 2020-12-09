from aocd import get_data


def part_1 () :
    print("Part 1!")
    xPos = 0
    trees = 0
    slope = get_data(day=3, year=2020).split("\n")
    for row in slope:
        if row[xPos] == '#':
            trees += 1
        xPos += 3
        if xPos >= len(row):
            xPos -= len(row)
    print("Trees = ", trees)

def part_2():
    print("Part 2!")
    xPos = [0, 0, 0, 0, 0]
    xMove = [1, 3, 5, 7, 1]
    yPos = [0, 0, 0,0 , 0]
    yMove = [1, 1, 1, 1, 2]
    trees = [0, 0, 0, 0, 0]
    slope = get_data(day=3, year=2020).split("\n")
    for i in range(len(trees)):
        while yPos[i] < len(slope):
            if slope[yPos[i]][xPos[i]] == '#':
                trees[i] += 1
            xPos[i] += xMove[i]
            if xPos[i] >= len(slope[yPos[i]]):
                xPos[i] -= len(slope[yPos[i]])
            yPos[i] += yMove[i]
    
    product = 1
    for tree in trees:
        product *= tree
    print("Trees Product= ", product)
    

if __name__ == "__main__":
    print("Day 3 - Toboggan Trajectory!")
    part_1()
    part_2()
    print ("Day 3 - Done!")
