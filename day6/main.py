def add(dic, k, v):
    """ Sets dic[k] to dic[k] + v, or v if k is not in dic. """
    if k in dic:
        dic[k] += v
    else:
        dic[k] = v


def sim(iters):
    """ Runs the simulation for [iters] iterations. Prints the total number of fish at the end of the simulation. """
    days = {}  # {days until spawn: number of fish}
    with open('day6/input.txt', 'r') as f:
        for d in f.readline().strip().split(','):
            add(days, int(d), 1)
    for i in range(iters):
        nxt = {}
        for d, n in days.items():
            if d == 0:
                add(nxt, 8, n)
                add(nxt, 6, n)
            else:
                add(nxt, d - 1, n)
        days = nxt
    print(sum(days.values()))


if __name__ == '__main__':
    sim(80)  # part 1
    sim(256)  # part 2
