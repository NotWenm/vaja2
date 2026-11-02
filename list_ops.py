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

def najmanjse(list):
    najmanjse=list[0]
    for i in range(len(list)-1):
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
        
        