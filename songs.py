import csv
from datetime import*
with open('songs.csv',encoding='utf8') as csvfile:
    reader = csv.reader(csvfile,delimiter =';',quotechar='"')
    answer =list(reader)[1:]
    for j in answer:
        a = j[-1].split('.')
        b = int(a[-1])
        if b<2002:
            print(j[-2],'-',j[-3],'-',j[0])

with open('songs.csv',encoding='utf8') as csvfile:
    reader = csv.reader(csvfile,delimiter =';',quotechar='"')
    answer =list(reader)[1:]
    for j in answer:
        a = j[-1].split('.')
        f_date = date(2023,5,12)
        s_date = date(int(a[-1]),int(a[-2]),int(a[-3]))
        raz = int((f_date-s_date).days)
        if j[0] == '0':
            j[0] = abs(raz/(len(j[1])+len(j[2])))*10000
        print(j)
              

with open('songs_new.csv','w', newline='',encoding='utf8') as file:
    w = csv.writer(file)
    w.writerow(['streams','artist_name','track_name','date'])
    w.writerows(answer)
