def pair(nombre):
    ''' Cette fonction permet de verifier le parite d'un nombre'''
    if nombre%2==0:
        print("Le nombre pair")
    else:
        print("le nombre impaire")
pair(6)
pair(7)
print(pair.__doc__)
