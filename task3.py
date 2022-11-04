#Создайте программу для игры в ""Крестики-нолики"".
maps = [1,2,3,
        4,5,6,
        7,8,9]
 

shablon = [[0,1,2],
           [3,4,5],
           [6,7,8],
           [0,3,6],
           [1,4,7],
           [2,5,8],
           [0,4,8],
           [2,4,6]]
 

def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
 
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
 
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])    
 
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol
 
def get_result():
    win = ""
 
    for i in shablon:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"   
             
    return win

player1 = 1
count = 9
while count > 0:
    print_maps()
    if player1 == 1:
        symbol = "X"
        step = int(input("Х, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("О, ваш ход: "))
 
    step_maps(step,symbol) # делаем ход в указанную ячейку
    win = get_result() # определим победителя
    count -= 1
    if win != "":
        break
    player1 = not(player1)        

print_maps()
if win =="":
    print("ничья")
else:
    print("Победил", win)

