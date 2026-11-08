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
    for i in range(len(list)):
        if list[i]>najvecje:
            najvecje=list[i]
    return najvecje
print(najvecje(list))

def najmanjse(list):
    najmanjse=list[0]
    for i in range(len(list)):
        if list[i]<najmanjse:
            najmanjse=list[i]
    return najmanjse
print(najmanjse(list))

def sodi(list):
    st_sodih=0
    for i in range(len(list)):
        if list[i]%2==0:
            st_sodih+=1
    return st_sodih
print(sodi(list))

def lihi(list):
    st_lihih = 0
    for i in range(len(list)):
        if list[i] % 2 != 0:
            st_lihih += 1
    return st_lihih

print(lihi(list))  

def vecje_od_10(list):
    for i in range(len(list)):
        if list[i] > 10:
            print(list[i])

def uredi(list):
    list.sort()
    print(list)
        