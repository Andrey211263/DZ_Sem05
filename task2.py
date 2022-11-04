# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход 
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно 
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему 
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все 
# конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def rnd():
    res = []
    for i in range(0, 28, 1):
        res.append(randint(1, 29))
    return res

def dialog(str, uf):
    print('Количестов конфет ', uf)
    pl = int(input(str))
    while pl > 28:
        print('Извените, но можно взять только 1 - 28! Попробуйте еще раз')
        pl = int(input(str))
    uf -= pl
    print(uf)
    return uf

num = int(input('Выберите с кем хотите играть: 1 - человек, 2 - компьютер, 3 - ИИ '))
match num:
    case 1:
        pl1 = int(input("1-ый игрок -> Введите число: "))
        pl2 = int(input("2-ой игрок -> Введите число: "))
        c1 =rnd()
        c2 =rnd()
        print(f' Выкинул 1-ый игрок {c1[pl1]},\n Выкинул 2-ой игрок {c2[pl2]}')
        buf = 121
        sign = 0
        if c1[pl1] > c2[pl2]:
            buf = dialog('Ход первого игрока! Сколько конфет вы заберете?: ', buf)
            sign = 1
        else:
            buf = dialog('Ход вторго игрока! Сколько конфет вы заберете?: ', buf)
            sign = 2    
        while buf > 0:
            if sign == 1:
                buf = dialog('Ход второго игрока! Сколько конфет вы заберете?: ', buf)
                sign = 2
            else:
                buf = dialog('Ход первого игрока! Сколько конфет вы заберете?: ', buf)
                sign = 1
        if sign == 1:
            print('Победа 1-ый игрок')
        else:
            print('Победа 2-ой игрок')
        
    case 2:
        pl1 = int(input("1-ый игрок -> Введите число: "))
        c1 = rnd()
        c2 = randint(1, 29)
        print(f' Выкинул 1-ый игрок {c1[pl1]},\n Выкинул компьютер {c2}')
        buf = 121
        sign = 0
        if c1[pl1] >= c2:
            buf = dialog('Ход первого игрока! Сколько конфет вы заберете?: ', buf)
            print('test')
            sign = 1
        else:
            buf = buf - randint(1, 29)
            print(f'ход компьютера, забрал: {c2}, остаток {buf}')
            sign = 2
        while buf > 0:
            if sign == 1:
                c2 = randint(1, 29)
                if c2 > buf:
                    c2 = buf
                    buf = buf - c2
                    print(f'Ход комьютера! забрал: {c2} остаток {buf}')
                    sign = 2
                else:
                    buf = buf - c2
                    print(f'Ход комьютера! забрал: {c2} остаток {buf}')
                    sign = 2
            else:
                buf = dialog('Ход первого игрока! Сколько конфет вы заберете?: ', buf)
                print('test')
                sign = 1
        if sign == 1:
            print('Победа 1-ый игрок')
        else:
            print('Победа компьютера')
        
 
    case 3:
        pl1 = int(input("1-ый игрок -> Введите число: "))
        c1 = rnd()
        c2 = randint(1, 29)
        print(f' Выкинул 1-ый игрок {c1[pl1]},\n Выкинул компьютер {c2}')
        buf = 2021
        sign = 0
        if c1[pl1] >= c2:
            buf = dialog('Ход первого игрока! Сколько конфет вы заберете?: ', buf)
            sign = 1
        else:
            c2 = buf % 29
            buf = buf - c2
            print(f'ход компьютера, забрал: {buf % 29}, остаток {buf}')
            sign = 2
        while buf > 0:
            if sign == 1:
                c2 = buf % 29
                print(c2)
                if c2 > buf:
                    c2 = buf
                    buf = buf - c2
                    print(f'Ход комьютера! забрал: {c2} остаток {buf}')
                    sign = 2
                else:
                    buf = buf - c2
                    print(f'Ход комьютера! забрал: {c2} остаток {buf}')
                    sign = 2
            else:
                buf = dialog('Ход первого игрока! Сколько конфет вы заберете?: ', buf)
                print('test')
                sign = 1
        if sign == 1:
            print('Победа 1-ый игрок')
        else:
            print('Победа компьютера')
    
    case _:
        print('Отдохни!')
