from sugar4py import *


def encode():
    size = 9
    
    x = [['x_%02d_%02d'%(i, j) for j in range(size)] for i in range(size)]
    for i in x:
        for j in i:
            add(INT, j, 0, 1)

    y = 'y'
    add(INT, y, 0, size * size)
    
    add(OBJECTIVE, MINIMIZE, y)
    term = [j for i in x for j in i]
    add(EQ, y, create(ADD, *term))
    
    for i in x:
        for j in range(size - 7 + 1):
            term = i[j:j + 7]
            add(GT, create(ADD, *term), 0)

    for i in zip(*x):
        for j in range(size - 7 + 1):
            term = i[j:j + 7]
            add(GT, create(ADD, *term), 0)

    for i, j in ((2, 0), (1, 0), (0, 0), (0, 1), (0, 2)):
        for k in range(min(size - i, size - j) - 7 + 1):
            a, b = i + k, j + k
            term = []
            for _ in range(7):
                term.append(x[a][b])
                a += 1
                b += 1
            add(GT, create(ADD, *term), 0)

    for i, j in ((0, 6), (0, 7), (0, 8), (1, 8), (2, 8)):
        for k in range(min(size - i, j + 1) - 7 + 1):
            a, b = i + k, j - k
            term = []
            for _ in range(7):
                term.append(x[a][b])
                a += 1
                b -= 1
            add(GT, create(ADD, *term), 0)


def main():
    encode()


if __name__ == '__main__':
    main()
