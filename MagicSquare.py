import sys
from sugar4py import*

def encode(size):
    summ = (size * size) * (size * size + 1) // 2 // size
    
    # 変数の宣言
    x = [['x_{}_{}'.format(str(i).zfill(2), str(j).zfill(2)) for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            add(INT, x[i][j], create(1), create(size * size))

    # 制約の生成
    terms = [j for i in x for j in i]
    add(ALLDIFFERENT, *terms)

    # 横
    for i in x:
        terms = i
        add(EQ, create(ADD, *terms), create(summ))
    
    # 縦
    for i in zip(*x):
        terms = i
        add(EQ, create(ADD, *terms), create(summ))

    # 斜め1
    terms = [y[i] for i,y in enumerate(x)]
    add(EQ, create(ADD, *terms), create(summ))

    # 斜め2
    terms = [y[size - 1 - i] for i,y in enumerate(x)]
    add(EQ, create(ADD, *terms), create(summ))
    

def main():
    args = sys.argv
    size = int(args[1])
    encode(size)


if __name__ == '__main__':
    main()
