list = [12,5,8,21,3,16,9,14]

def sestevek(list):
    vsota = 0
    for i in range(0,len(list)):
        vsota +=list[i]
    return vsota
print(sestevek(list))

def povprecje(list):
    vsota = 0
    for i in range(0,len(list)):
        vsota+=list[i]
    return vsota/len(list)
print(povprecje(list))

def najvecje(list):
    najvecje=0
    for i in range(len(list)-1):
        if list[i]>najvecje:
            najvecje=list[i]
    return najvecje
print(najvecje(list))