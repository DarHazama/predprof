import csv
from datetime import*
def quicksort(arr,low,high,key):
    if low < high:
        pi = partatition(arr,low,high,key)
        quicksort(arr,low,pi-1,key)
        quicksort(arr,pi+1,high,key)
def partatition(arr,low,high,key):
    pivot = float(arr[high][key] if arr[high][key] != 'None' else 0)
    i = low - 1
    for j in range(low,high):
        if float(arr[high][key] if arr[high][key] != 'None' else 0) >= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i + 1

#with open('songs.csv',encoding='utf8') as csvfile:
#   reader = csv.reader(csvfile,delimiter =';',quotechar='"')
#    answer =list(reader)[1:]
#    for j in answer:
#        a = j[-1].split('.')
#        f_date = date(2023,5,12)
#        s_date = date(int(a[-1]),int(a[-2]),int(a[-3]))
#        raz = int((f_date-s_date).days)
#        if j[0] == '0':
#            j[0] = abs(raz/(len(j[1])+len(j[2])))*10000
with open('songs.csv',encoding='utf8') as csvfile:
    reader = list(csv.DictReader(csvfile,delimiter=';',quotechar='"'))
    quicksort(reader,0,len(reader)-1,key='date')
    print(reader)
