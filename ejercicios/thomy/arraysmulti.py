elArray = [[1,2,3],[4,5,6],[7,8,9]]
print(elArray)

""" print(elArray[2]) """

elArray[0].insert(0,"primeros números")
elArray[1].insert(0,"Segundo arreglo")
elArray[2].insert(0,"Tercer arreglo")

""" print(elArray) """

for x in range(len(elArray)):
    for i in range(len(elArray[x])):
        print(elArray[x][i])

print("---------------------------")
print(elArray[0].count(2))
print(elArray[1].count(4))
print(elArray[2].count(8))


print("---------------------------")

print(elArray[0].index(2))
print(elArray[1].index(5))
print(f"El indice ",{elArray[2].index(7)})

print("---------------------------")

print(elArray[0].insert(4,"4"))
print(elArray[1].insert(4,"7"))
print(elArray[2].insert(4,"10"))

print(elArray)

elArray.reverse()
print(elArray)




