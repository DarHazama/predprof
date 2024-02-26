import csv
from datetime import*

def linar_search(arr,target):
    for i in range(len(arr)):
        if arr[i][1] == target:
            return i
    return -1


with open('songs.csv',encoding='utf8') as csvfile:
    reader = csv.reader(csvfile,delimiter =';',quotechar='"')
    answer =list(reader)[1:]
    a = input()
    while a != '0':
        if linar_search(answer,a) != -1:
            print('У',answer[linar_search(answer,a)][1],'найдена песня:',answer[linar_search(answer,a)][2])
        else:
            print('К сожалению, ничего не удалось найти')
        a = input()
    
