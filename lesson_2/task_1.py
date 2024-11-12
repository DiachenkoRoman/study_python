#---------------------------VARIABLES--------------------------------
intVar = 12
weight = 140.5
strVar = "baboon"
listVar = [1, 2, 3, 4, 5]
tupleVar = (1, 2, 3, 4, 5)
dictVar = {"name": "Bob", "age": 23, "profession": "baboon"}
cpDict = dict(dictVar)
bool_1 = True
bool_0 = False


#---------------------------ARITHMETICS-------------------------------
summ = intVar + weight
print(summ)
print(intVar + weight, weight - intVar, weight * intVar, weight / intVar, intVar ** 2)


#--------------------------COMPARISON---------------------------------

result = intVar == weight
print(result)
print(strVar and intVar, bool_1 and bool_0, bool_1 or bool_0)

print(bool_1 and weight or strVar and intVar)

print(dictVar == cpDict)

print(type(dictVar) == type(tupleVar))


