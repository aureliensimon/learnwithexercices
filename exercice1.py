# Correction exercice 1.

# Elle doit renvoyer la somme de 2 list
def somme(l1, l2):
    if len(l1) != len(l2):
        return
    
    return [a+b for a, b in zip(l1, l2)]

# Elle doit renvoyer la soustraction de 2 list
def soustraction(l1, l2):
    if len(l1) != len(l2):
        return
    
    return [a-b for a, b in zip(l1, l2)]

# Elle doit renvoyer la multiplication de 2 list
def multiplication(l1, l2):
    if len(l1) != len(l2):
        return
    
    return [a*b for a, b in zip(l1, l2)]

# Elle doit renvoyer la division de 2 list
def division(l1, l2):
    if len(l1) != len(l2):
        return
    
    return [a/b for a, b in zip(l1, l2)]


if __name__ == "__main__":

    print("Exercice 1: ")
    l1 = [1, 2, 3, 4, 5]
    l2 = [1, 1, 1, 1, 1]

    print(somme(l1, l2))
    print(soustraction(l1, l2))
    print(multiplication(l1, l2))
    print(division(l1, l2))
