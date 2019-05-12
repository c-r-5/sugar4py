import subprocess
import argparse
from sugar4py import*

file = ''

def write(*s):
    s = create(*s)
    file.write(s + '\n')

def encode(size):
    summ = (size * size) * (size * size + 1) // 2 // size
    
    # 変数の宣言
    x = [['x_%02d_%02d'%(i, j) for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            write(INT, x[i][j], create(1), create(size * size))

    # 制約の生成
    terms = [j for i in x for j in i]
    write(ALLDIFFERENT, *terms)

    # 横
    for i in x:
        terms = i
        write(EQ, create(ADD, *terms), create(summ))
    
    # 縦
    for i in zip(*x):
        terms = i
        write(EQ, create(ADD, *terms), create(summ))

    # 斜め1
    terms = [y[i] for i,y in enumerate(x)]
    write(EQ, create(ADD, *terms), create(summ))

    # 斜め2
    terms = [y[size - 1 - i] for i,y in enumerate(x)]
    write(EQ, create(ADD, *terms), create(summ))

def result(size, vv, f):
    if vv:
        run = subprocess.Popen(['sugar', '-vv', f], stdout = subprocess.PIPE)
    else:
        run = subprocess.Popen(['sugar', f], stdout = subprocess.PIPE)

    res = run.communicate()[0].decode()
    print(res)

    if 'SATISFIABLE' in res:
        res = res[res.rfind('SATISFIABLE'):]
        ans = [[None]*size for _ in range(size)]
        
        for t in res.split('\n')[1:size * size + 1]:
            x, v = t.split()[1:]
            i, j = map(int, x.split('_')[1:])
            ans[i][j] = int(v)

        for a in ans:
            print(*['%2d'%t for t in a])

def main():
    global file
    parser = argparse.ArgumentParser()
    parser.add_argument('size', type = int)
    parser.add_argument('-vv', action = 'store_true')
    parser.add_argument('-f', default = 'hoge.csp')
    args = parser.parse_args()
    size = args.size
    f = args.f
    file = open(f, 'w')

    encode(size)
    file.close()

    result(size, args.vv, f)

if __name__ == '__main__':
    main()
