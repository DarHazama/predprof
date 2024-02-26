import csv
from datetime import*

def linar_search(arr,target):
    for i in range(len(arr)):
        if arr[i][1] == target:
            return i
    return -1

alp_r = 'АБВГДЕЁЖЗКЛМНОПРСТУФХЧШЩЭЮЯабвгдеёжзиклмнопрстуфхчщёэюя'
alp_e = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
alp_n = '0123456789'
rus = set()
eng = set()
num = set()

with open('songs.csv' ,encoding='utf8') as csvfile:
    reader = csv.reader(csvfile,delimiter =';',quotechar='"')
    answer =list(reader)[1:]
    for i in answer:
        if i[1][0] in alp_r:
            rus.add(i[1])
        if i[1][0] in alp_e:
            eng.add(i[1])
        if i[1][0] in alp_n:
            num.add(i[1])
f = open('russian_artists.txt','w')
f.write('\n'.join(rus))
f.close()
q = open('foreign_artists.txt','w',encoding='utf8')
q.write('\n'.join(eng))
q.write('\n')
q.write('\n'.join(num))
q.close()

        
        
   
        
    
