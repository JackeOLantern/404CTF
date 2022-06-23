#!/usr/bin/python3.10
import random as rd

s = [16, 3, 12, 9, 1, 60, 1, 3, 14, 39, 13, 16, 16, 1, 9, 13, 3, 39, 60,
    16, 16, 1, 60, 7, 39, 13, 3, 13, 18, 3, 13, 25, 14, 3, 1, 14, 60,
    13, 32, 13, 3, 39, 16, 18, 18, 3, 43, 16, 18, 3, 1, 43, 18, 16,
    13, 16, 1, 3, 1, 16, 13, 18, 60, 16, 3, 3, 14, 18, 13, 14, 16, 18,
    7, 3, 7, 25, 7, 7, 13, 13, 13, 3, 60, 1, 3, 13, 1, 25, 18, 16, 32,
    16, 60, 1, 7, 44, 18, 39, 39, 39, 60, 3, 1, 60, 3, 16, 13, 13, 14,
    1, 3, 39, 39, 31, 32, 39, 32, 18, 39, 3, 13, 32, 60, 7, 7, 39, 14,
    3, 18, 14, 60, 39, 18, 7, 1, 32, 13, 3, 14, 39, 39, 7, 1, 1, 13,
    29, 60, 13, 39, 14, 14, 16, 60, 1, 3, 44, 14, 3, 1, 1, 1, 39, 13,
    14, 39, 18, 3, 7, 13, 39, 32, 1, 43, 1, 16, 1, 3, 18, 14, 25, 32,
    7, 13, 39, 7, 1, 3, 60, 13, 13, 7, 18, 1, 3, 18, 1, 60, 7, 1, 39,
    14, 3, 39, 7, 31, 1, 7, 18, 7, 32, 3, 3, 14, 32, 14, 1, 32, 12,
    18, 31, 39, 1, 13, 13, 43, 44, 32, 3, 32, 60, 14, 60, 60, 7, 3, 1,
    3, 3, 14, 1, 60, 16, 44, 3, 1, 32, 13, 5, 16, 39, 3, 60, 7, 14, 3,
    13, 7, 31, 13, 39, 9, 3, 44, 13, 16, 14, 18, 18, 3, 7, 3, 3, 3, 7,
    3, 3, 16, 39, 3, 3, 13, 32, 13, 3, 18, 7, 10, 3, 18, 1, 7, 7, 18,
    13, 43, 18, 3, 32, 39, 32, 13, 1, 18, 10, 1, 32, 1, 16, 32, 3, 44,
    3, 18, 1, 1, 1, 16, 18, 25, 60, 1, 39, 1, 18, 60, 16, 1, 7, 3, 13,
    16, 18, 39, 14, 7, 14, 3, 14, 13, 7, 16, 10, 18, 13, 3, 16, 13, 3,
    32, 43, 13, 14, 1, 13, 1, 14, 18, 60, 7, 3, 7, 31, 1, 18, 26, 7,
    3, 3, 32, 1, 7, 18, 7, 1, 16, 18, 39, 14, 7, 3
]

##
def a(c, r=True):
    n = ord(c)
    if r: rd.seed(n)
    match n:
        case 0:
            return dict.fromkeys(range(10), 0)
        case _:
            return (d:=a(chr(n - 1), False)) | {(m:=rd.randint(0, 9)): d[m] + rd.randint(0,2)}

##

def b(p, n):
    match list(p):
        case []:
            return []
        case [f, *rest]:
            l = list(a(f).values()) + b(''.join(rest), n*2)
 #           if n == 1:
 #               print("b1=", l)
            rd.seed(n)
            rd.shuffle(l)
            return l

##
def c(p, n=0):
    match p:
        case []:
            return n!=0
        case [f, *rest]:
            rd.seed(s[n])
            return rd.randint(0,30) == f and c(rest, n + 1)


def unshuffle(l, seed):
    order = list()
    for i in range (0, len(l)):
        order.append(i)
    rd.seed(seed)
    #print("INDEXES BEFORE: ", order)
    rd.shuffle(order)
    #print("INDEXES       : ", order)
    resu = list()
    for i in range (0, len(l)):
        idx = order.index(i)
        resu.append(l[idx])
    return resu

#print(len(s))
N=len(s)
resuC = list()
for n in range(0, N):
    rd.seed(s[n])
    f = rd.randint(0,30)
    #print(f)
    resuC.append(f)

# print(c(resu))
print("RESU C:\n", resuC)

# pour a c 'est complexe mais deterministe, on va se faire un dictionnaire
aDic = dict()
aDicReverse = dict()
for i in range (0, 256):
    c = chr(i)
    v = str(list(a(c).values()))
    aDic[v] = c
    aDicReverse[c] = v
# print(aDic)

# try to get FIRST letter : split by packets of 10 resuB1
resuB1 = unshuffle(resuC, 1) # la fonction appelle avec un n=1
print("RESU B1:\n", resuB1)
resuB1_1 = resuB1[0:10]
print("B1_1=")
print(str(resuB1_1))
print("Letter 1: ", aDic[str(resuB1_1)])
print("----------------------------------")
# try to get NEXT letter : take the REST
resuB1_REST = resuB1[10:]
print("B1_REST=")
print(str(resuB1_REST))
resuB2 = unshuffle(resuB1_REST, 2) # la fonction appelle avec un n=2
print("RESU B2:\n", resuB2)
resuB2_1 = resuB2[0:10]
print("B2_1=")
print(str(resuB2_1))
print(aDic[str(resuB2_1)])
print("----------- GO FOR REAL ------------------")
print("RESU C:\n", resuC)
#GO FOR GENERIC not one by one
REST = resuC
n = 1
flag = ''
while len(REST) >= 10:
    resuB1 = unshuffle(REST, n) # la fonction appelle avec un n
    print("RESU B1:\n", resuB1)
    resuB1_1 = resuB1[0:10]
    print("B1_1=")
    print(str(resuB1_1))
    l = aDic[str(resuB1_1)]
    print("Letter : ", l)
    flag = flag  + l
    print("----------------------------------")
    REST = resuB1[10:]
    n = n * 2

print("Here we are :\n", flag)
#c1 = '0'
#print("reverse", c1, " = ", aDicReverse[c1])

#b(input("password:"), 1)

''' test unshuffle b ok
n = 13
rd.seed(n)
rd.shuffle(resu)
print("shuffle : ", str(n), "\n", resu)
resu = unshuffle(resu, n)
print("unshuffle : ", str(n), "\n", resu)
'''

##
#if c(b(input("password:"), 1)):
#    print("Utilise ce mot de passe pour valider le challenge!")
#else:
#    print("Essaye Encore!")
