from aocd import get_data

dataDict = {}

def part_1 () :
    print("Part 1!")
    expenses = [int(string) for string in get_data(day=1, year=2020).split("\n")]
    for i in expenses:
        dataDict[i] = 1
        if (2020 - i) in dataDict:
            print("answer = ", i * (2020 - i))
            break

def part_2():
    print("Part 2!")
    expenses = [int(string) for string in get_data(day=1, year=2020).split("\n")]
    i = 0
    j = 0
    while i < len(expenses):
        j = i+1
        while j < len(expenses):
            third = (2020 - expenses[i] - expenses[j])
            if third > 0 and third in dataDict:
                print("answer = ", expenses[i] * expenses[j] * third)
                return
            j+=1
        i+=1

if __name__ == "__main__":
    print("Day 1 - Report Repair!")
    part_1()
    part_2()
    print ("Day 1 - Done!")
