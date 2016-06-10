#!/user/bin/python

"""
num = 23

if num < 50:
    for letter in 'Python':
        if letter == 'h':
            pass
            print ('This is pass block')
        print ('Current Letter :', letter)
    print("Welcome to passing in Java")
else:
    print("it didnt work")
    for letter in 'kdomedomepython':
        if letter == 'd':
            pass
            print('not allowed')
        print('Current leter: '+letter)
    print("This is the end")


str = ["1", "2", "3"]
strs = 'wort'
n = [str, str]
print(len(n.pop(1)))

dic = [1, 2, 3, 4, 4, 5, 6]
dic[4] = 5
dic[5] = dic[6]
dic[6] = 7
strs = strs.replace('t', 'k')
print(dic)
print(strs)

# creating map

mapval = {"Alex": 32, "Mike": 34, "Johnson": 34}
mapval.update({"Zha": 34})
mapval.update({"Rose": 38})
mapval.update({"Reono": 38})

# boo = "zha" in mapval this way doesnt work
bole = "zha"

for i in mapval:
    if i.lower() == bole:
        print("true")

for i in mapval.keys():
    print("keys in mapval are: ", i)
    for a in mapval.values():
        print("The vales in mapval are: ", a)

# python sets
sett = set()
sett.add(2)
sett.add(3)
sett.add(7)
sett.add(6)
sett.add(5)
sett.add(9)
sett1 = {3, 7, 4, 23, 24, 2}
print(sett, sett1)

print(sett & sett1)  # without common values
print(sett | sett1)  # union
print(sett - sett1)  # without common values
"""
"""""
var = [1, 2, 3, 4]
st = ["Mak","hsj","jjk"]
print(*var) # this is unpacking everything
print(' '.join(st)) # works on string
print(','.join(map(str, var))) # cast int to string and use it.
"""""


def get_Greater(num, num1):
    numbr = 89
    num = numbr
    print(num)
    return num > num1


if get_Greater(-2, 82):
    global numbr
    print("True is  greater")
else:
    print("False is not greater")


def getList(list):
    return list[0], list[1], list[2]


a, b, c = getList(["work", "good moeny", "food", "travel"])

print(a, b,c)

