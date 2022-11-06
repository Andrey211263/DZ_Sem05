# Напишите программу, удаляющую из текста все слова,
# в которых присутствуют все буквы "абв"
import re
# str =input('Введите текст ')
# ---------- 1-ый вариант
lst = ['фырмф', 'лдцг', 'бцвуцауы', 'опа',
       'ы', 'ка', 'ааукуа', 'аппрбв', 'ывроавб']
# str = []
# for i in range(0, len(lst), 1):
#     a = lst[i].lower()
#     if 'б' in a and 'а' in a and 'в'  in a:
#         print(i, 'абв - есть')
#     else:
#         str.append(lst[i])
# print(str)
# print(lst)

# exit()

# --------- 2-ой вариант
lst = []
with open('file.txt', 'r', encoding='utf-8') as data:
    for line in data:
        lst = re.split(r"[,]", line)

print(*lst)
# print(lst(type))
count = len(lst)
i = 0
while count > 0:
    a = lst[i].lower()
    # print(f'{lst[i]} i, count -> {i}, {count}')
    if 'б' in a and 'а' in a and 'в'  in a:
        del lst[i]
    else:
        i += 1
    count -= 1
with open('result.txt', 'w', encoding='utf-8') as file:
    for i in range(len(lst)):
        file.write(str(lst[i]))
        # file.write(str(lst[i]+'\n'))
print(*lst)
