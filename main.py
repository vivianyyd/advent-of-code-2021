import numpy as np

with open('input.txt', 'r') as f:
    # more efficient: map number to board, row, col
    draws = [int(n) for n in f.readline().split(',')]
    nums = {}
    board = -1  # boards numbered 0-
    row = 0
    bn = []
    for line in f:
        line = line.strip()
        r = []
        if len(line) == 0:
            board += 1
            row = 0
            col = 0
            b = []
            if not len(b):
                bn.append(b)
            continue
        for col, num in enumerate(line.split()):
            n = int(num)
            r.append(n)
            if n in nums:
                nums[n].append((board, row, col))
            else:
                nums[n] = [(board, row, col)]
        b.append(r)
        row += 1
    boards = [np.array([[False for i in range(5)] for j in range(5)]) for k in range(board + 1)]


def check():
    """
    Returns index of board if it has won
    """
    for ind, board in enumerate(boards):
        if np.any(np.all(board, axis=0)) or np.any(np.all(board, axis=1)):
            return ind
    return None


wins = set()


def new():
    """
    Returns -1 if multiple boards have newly won.
    Returns the index of a board if it alone has newly won.
    Otherwise, returns None.
    """
    new = []
    for ind, board in enumerate(boards):
        if np.any(np.all(board, axis=0)) or np.any(np.all(board, axis=1)):
            if ind not in wins:
                wins.add(ind)
                new.append(ind)
    if len(new) == 1:
        return new[0]
    elif len(new) > 1:
        return -1
    else:
        return None


def p1():
    for draw in draws:
        try:
            for (b, r, c) in nums[draw]:
                boards[b][r][c] = True
        except KeyError:
            pass  # no boards contain draw
        win = check()
        if win:
            sm = 0
            for r, row in enumerate(bn[win]):
                for c, num in enumerate(row):
                    if not boards[win][r][c]:
                        sm += num
            print(sm * draw)
            break


def p2():
    lastscore = 0
    for draw in draws:
        try:
            for (b, r, c) in nums[draw]:
                boards[b][r][c] = True
        except KeyError:
            pass  # no boards contain draw
        win = new()
        if win is not None and win != -1:
            last = win
            sm = 0
            for r, row in enumerate(bn[last]):
                for c, num in enumerate(row):
                    if not boards[last][r][c]:
                        sm += num
            lastscore = sm * draw
    print(lastscore)


if __name__ == '__main__':
    p1()
    p2()
