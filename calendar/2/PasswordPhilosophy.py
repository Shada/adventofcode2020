from aocd import get_data


def part_1 () :
    print("Part 1!")
    valid = 0
    passwordsAndPolicies = get_data(day=2, year=2020).split("\n")
    for line in passwordsAndPolicies:
        policy, password = line.split(": ")
        bounds, letter = policy.split(" ")
        lowerBound, upperBound = bounds.split("-")
        count = password.count(letter)
        if count >= int(lowerBound) and count <= int(upperBound):
            valid += 1
    print ("Valid Passwords  = ", valid)

def part_2():
    print("Part 2!")
    valid = 0
    passwordsAndPolicies = get_data(day=2, year=2020).split("\n")
    for line in passwordsAndPolicies:
        policy, password = line.split(": ")
        positions, letter = policy.split(" ")
        lowerPos, upperPos = positions.split("-")
        posLetters = password[int(lowerPos) - 1] + password[int(upperPos) - 1]
        if(posLetters.count(letter) == 1):
            valid += 1
    print ("Valid Passwords  = ", valid)

if __name__ == "__main__":
    print("Day 2 - Password Philosophy!")
    part_1()
    part_2()
    print ("Day 2 - Done!")
