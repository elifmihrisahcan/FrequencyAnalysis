"""
def analiz(girdi):
    liste=[]
    strink=""
    for car in girdi:
        if car in strink:
            for i in liste:
                if i[0]== car:
                    i[1] +=1

        else:
            strink += car
            liste.append([car,1])

    return liste

print(analiz("Bilmemneb"))
"""

def analiz(girdi):
    noktalama= "° x,±./? +\[]!%ˆˆ*()_;:˜`@#$-'&<>\"\' « » \n ^¦•'̂'„|~'̆'['̧', ['̇',"
    turkceOlmayanHarfler="xwq"
    sayilar ="1234567890"
    girdi=girdi.lower()
    #girdi= str(girdi.encode('UTF-8'))
    liste=[]
    strink=""
    for car in girdi:
        if car not in noktalama and car not in sayilar and car not in turkceOlmayanHarfler:
            if car in strink:
                for i in liste:
                    if i[0]== car:
                        i[1] +=1

            else:
                strink += car
                liste.append([car,1])

    return sorted(liste, key=lambda i: i[1], reverse=True)

with open("incememed.txt","r", encoding="UTF-8") as file:
    print(file)
    for i in analiz(file.read()):
        print(i)