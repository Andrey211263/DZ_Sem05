# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
import re
lst = []
with open('rle.txt', 'r',encoding='utf-8') as data:
    for line in data:
        lst.append(line)

print(lst)
res = []
res = str(lst).strip("[']")
# print(res, ':len -> ', len(res))

# шифратор:  1-ый символ признак: 0- не повторяющаяся/1- повторяющаяся  последовательность.
# 2-ой длина для неповт. последовательности и количество символов для повторяющейся  

def shifr(txt):
    count = 1   # счетчик дублей
    res = '' 
    cnt = 0     # кол-во не совпадающих
    tmp = ''    # буфер для несовпадающих элементов
    for i in range(len(txt) - 1):
        if txt[i] != txt[i+1]:
            if count != 1:
                res = res + '1' + str(count) + txt[i]
                count = 1
                i += 1
            else:
                tmp += txt[i]
                cnt += 1
        else:
            if cnt != 0:
                res = res + '0' + str(cnt) + tmp
                cnt = 0
                tmp = ''
            count += 1
    # обработка последнего элемента     
    if txt[-2] != txt[-1]:
        if count != 1:      #провекрка количества повторяющихся элементов
            res = res + '1' + str(count) + txt[i]
        else:
            if cnt == 0:    #проверка длины неповторяющейся последовательности
                cnt += 1
                res = res + '0' + str(cnt) + txt[-1]
            else:
                cnt += 1
                tmp += txt[-1]
                res = res + '0' + str(cnt) + tmp
    else:
        if count != 1:
            res = res + '1' + str(count) + txt[i]
    # print(f'{res}, i -> {i}, tmp -> "{tmp}", cnt -> {cnt}, count -> {count}')
    return res
# дешифруем
def deshifr(txt):
    rs = ''
    count = len(txt)
    # print(count)
    i = 0
    while count > 0:
        pr = int(txt[i])
        number = int(txt[i+1])
        # print('pr - ',pr, 'number - ', number, 'count -', count)
        if pr == 1:
            rs = rs + txt[i + 2] * number
            count -= 3
            i += 3
        else:
            j = i
            count -= number + 2
            i += number + 2
            while number > 0:
                rs = rs + txt[j + 2]
                number -= 1
                # print(rs, 'i->', j, number)
                j += 1
        # print(rs, 'i->', i, 'count -', count)
    return rs

result = shifr(res)
print(result)
print(deshifr(result))
# with open('rle.txt', 'a', encoding='utf-8') as file:
#     file.write('\shifr\n')
#     for i in range(len(result)):
#         file.write(result[i])
with open('shifr.txt', 'w',encoding='utf-8') as file:
    for i in range(len(result)):
        file.write(result[i])
finish = deshifr(result)
# res_str = finish.replace("'", "", 1)
# res_str = finish.replace("'", "", -1)

# with open('rle.txt', 'a', encoding='utf-8') as file:
#     file.write('\ndeshifr\n')
#     for i in range(len(result)):
#         file.write(result[i])       
with open('deshifr.txt', 'w',encoding='utf-8') as file:
    for i in range(len(finish)):
        file.write(finish[i])

# При использовании во входном файле символа '\', после прогона strip он задваивается, 
# я не разобрался почему