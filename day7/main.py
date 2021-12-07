with open('input.txt', 'r') as f:
    crabs = [int(x) for x in f.readline().split(',')]


def p1():
    fuel_const = 0
    crabs.sort()
    position = crabs[round(len(crabs) / 2)]
    for crab in crabs:
        fuel_const += abs(position - crab)
    print(fuel_const)


def p2():
    fuel = 0
    position = round(sum(crabs) / len(crabs))  # for the example, rounded up. for actual, rounded down. not sure why
    for crab in crabs:
        fl = 0
        for dist in range(abs(position - crab)):
            fuel += dist + 1
        fuel += fl
    print(fuel)


if __name__ == '__main__':
    p1()
    p2()
