from sugar4py import *


def encode(size, ng):
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
        for j in range(size - ng + 1):
            term = i[j:j + ng]
            add(GE, create(ADD, *term), 1)

    for i in zip(*x):
        for j in range(size - ng + 1):
            term = i[j:j + ng]
            add(GE, create(ADD, *term), 1)

    for i in range(size):
        for j in range(size):
            if min(size - i, size - j) < ng:
                continue
            a, b = i, j
            term = []
            for _ in range(ng):
                term.append(x[a][b])
                a += 1
                b += 1
            add(GE, create(ADD, *term), 1)

    for i in range(size):
        for j in range(size):
            if min(size - i, j + 1) < ng:
                continue
            a, b = i, j
            term = []
            for _ in range(ng):
                term.append(x[a][b])
                a += 1
                b -= 1
            add(GE, create(ADD, *term), 1)



def main():
    size, ng = map(int, input().split())
    encode(size, ng)



if __name__ == '__main__':
    main()
