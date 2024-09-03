def ListaParilliset(list):
    returnList = []
    for i in list:
        if(i % 2) == 0:
            returnList.append(i)
    return returnList

testList = [52,635,8474,243,74,5,96,24,735,634,23,2345,64,32,58,9032]
print(f"Alkuperäinen lista: {testList[:len(testList)+1]}")
print(f"Parillinen lista: {ListaParilliset(testList)[:len(ListaParilliset(testList))+1]}")

