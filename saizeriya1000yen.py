import re
import sqlite3
from sugar4py import*


def encode(data, limit):

    culsum = 0

    # 変数の宣言
    for name, _, calorie in data:
        add(INT, name, 0, 1)
        culsum += int(calorie)

    y = '総カロリー数'
    add(INT, y, 0, culsum)
    add(OBJECTIVE, MAXIMIZE, y)

    # 制約
    term = [create(MUL, calorie, name) for name, _, calorie in data]
    add(EQ, y, create(ADD, *term))

    term = [create(MUL, price, name) for name, price, _ in data]
    add(LE, create(ADD, *term), limit)



def main():
    # データベースは(https://github.com/marushosummers/Saizeriya_1000yen/blob/master/sensai/saizeriya.db)から
    c = sqlite3.connect('saizeriya.db').cursor()
    data = c.execute('SELECT name, price, calorie FROM menu')
    # メニュー名をそのまま変数名にしたいけど括弧があるとまずいのでごり押して消す
    data = [(re.sub('\((.*?)\)|（(.*?)）','_\\1\\2',d[0]) + '_\\%s_\\%skcal'%(d[1], d[2]), d[1], d[2]) for d in data]
    
    # 全部のメニューでやろうとしたらSATに変換すると膨大なbyte数になって無理って怒られた
    # メニュー数30個でやってみたら4時間45分かかった
    # data = data[:30]

    # 上限1000円
    limit = 1000
    encode(data, limit)

    #print(*data,sep='\n')


if __name__ == '__main__':
    main()
