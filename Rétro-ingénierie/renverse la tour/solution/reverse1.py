def tour1(password):
    string = str("".join( "".join(password[::-1])[::-1])[::-1])
    return [ord(c) for c in string]

def DEBUGtour1(password):
    #a = password[::-1] # ecrire password a  l 'envers
    #print("a=", a)
    #b = "".join(a)[::-1] # ecrire password a  l 'envers
    #print("b=", b)
    string = str(password[::-1])
    print("string=", string)
    return [ord(c) for c in string] # code ascii de password

def Rtour1(s):
    a = [chr(c) for c in s] # code ascii de password
#    print(a)

    b = "".join(a)[::-1]
#    print(b)
    return b

def tour2(password):
    new = []
    i = 0
    while password != []:
        new.append(password[password.index(password[i])])
        new.append(password[password.index(password[i])] + password[password.index(password[ i + 1 %len(password)])])
        password.pop(password.index(password[i]))
        i += int('qkdj', base=27) - int('QKDJ', base=31) + 267500
    return new

def DEBUGtour2(password):
    new = []
 #   print("off1", str(int('qkdj', base=27)), " - ", str(int('QKDJ', base=31)), str(int('qkdj', base=27)+ 267500))
    while password != []:
        '''valI = password[i] #val a position i
        posI = password.index(valI)# position de val : i?
        valI2 = password[posI] #val a position posI = valI ?
        print(str(i), " - valI:", str(valI))
        print(str(i), " - posI:", str(posI))
        print(str(i), " - valI2:", str(valI2))'''
        new.append(password[0])

        new.append(password[0] + password[1 % len(password)])
        
        password.pop(0)
    return new

def Rtour2(password):
    new = []
 #   print("off1", str(int('qkdj', base=27)), " - ", str(int('QKDJ', base=31)), str(int('qkdj', base=27)+ 267500))
    i = 0
    while i < len(password):
        new.append(password[i]) # on ne garde que les pairs
        i = i + 2
    return new


def tour3(password):
    mdp =['l', 'x', 'i', 'b', 'i', 'i', 'q', 'u', 'd', 'v', 'a', 'v', 'b', 'n', 'l', 'v', 'v', 'l', 'g', 'z', 'q', 'g', 'i', 'u', 'd', 'u', 'd', 'j', 'o', 'r', 'y', 'r', 'u', 'a']
    for i in range(len(password)):
        mdp[i], mdp[len(password) - i -1 ] = chr(password[len(password) - i -1 ] + i % 4),  chr(password[i] + i % 4)
    return "".join(mdp)

def DEBUGTour3(password):
    L = 34 # 17 du pass * 2 
    mdp =['1', '1', '1', '1', '1', 'i', 'q', 'u', 'd', 'v', 'a', 'v', 'b', 'n', 'l', 'v', 'v', 'l', 'g', 'z', 'q', 'g', 'i', 'u', 'd', 'u', 'd', 'j', 'o', 'r', 'y', 'r', 'u', 'a']
    for i in range(17, L):
        mdp[i] =  chr(password[33 - i] + i % 4) #remplir la 2eme moitie  autre et ecrasee
    for i in range(0, 17):
        mdp[i] = chr(password[33 - i] + (1 - i) % 4) #remplir la 1ere moitie
    
    
    return "".join(mdp)

def RTour3(mdp):
    s = [ord(c) for c in mdp] # code ascii de password
    print("s=", s)
    L = 34 # 17 du pass * 2
    password =['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    for i in range(0, 17):
        password[33 - i] = s[i] -  (1 - i) % 4 #remplir la 1ere moitie
    for i in range(17, L):
        password[33 - i] =  s[i] - i % 4 #remplir la 2eme moitie  autre et ecrasee
    
    return password


s = "abcdefGHIjKlMnOpr" # si pass fait plus de 17 : ko

print(s)
resu1 = tour1(s)  # un tableau avec les code ascii des char du password
print(resu1)
# print(Rtour1(resu1))
resu2 = tour2(resu1)  # un tableau avec les code ascii des char du password
print(resu2)
#resu1 = tour1(s)  # rearmela valeur
#print(DEBUGtour2(resu1))
#print(Rtour2(resu2))
#print(Rtour1(Rtour2(resu2)))

#R3 et go !
resu3 = tour3(resu2)
print(resu3)
print(DEBUGTour3(resu2))
print(RTour3(resu3))

print(Rtour1(Rtour2(RTour3(resu3))))

# FLAG 

print(Rtour1(Rtour2(RTour3("¡P6¨sÉU1T0d¸VÊvçu©6RÈx¨4xFw5"))))





mdp = input("Mot de passe : ")

if tour3(tour2(tour1(mdp))) == "¡P6¨sÉU1T0d¸VÊvçu©6RÈx¨4xFw5":
    print("Bravo ! Le flag est 404CTF{" + mdp + "}")
else :
    print("Désolé, le mot-de-passe n'est pas correct")




