strl="salut tout le monde"
print(strl[3])
print(strl[0])
print(strl[-1])
print(strl[-2])
print(len(strl))
print(strl[len(strl)-1])
# decouper de chaine de caracters
print(strl[0:5])
print(strl[6:10])
print(strl[0:])
print(strl[6:])
# saute avec :: dans le chaine de caracter
strl1="sabacada"
print(strl1[1::2])
print(strl[1::3])
print(strl[:7])#retourne 6 primiers caracters
print(strl[::-1])# renverse de chaine
str="Nadia"
str1="Savasteeva"
str2=str+" "+str1
print(str2)# print(str+" "+str1)
print(str,str1)

strl=strl+strl
print(strl)
# for (int i=0;i>3;i++)
for i in strl:
    print(i)
for i in enumerate(strl):
    print(i)






