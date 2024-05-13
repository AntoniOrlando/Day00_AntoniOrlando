def est_nombre_armstrong(num):
    # Convertir le nombre en chaîne de caractères pour pouvoir accéder à chaque chiffre
    num_str = str(num)
    # Initialiser la somme
    somme = 0
    # Calculer la somme des cubes des chiffres
    for chiffre in num_str:
        somme += int(chiffre) ** len(num_str)
    # Vérifier si la somme est égale au nombre lui-même
    if somme == num:
        return True
    else:
        return False

# Demander à l'utilisateur d'entrer un numéro
numero = int(input("Entrez un numéro : "))

# Vérifier si le numéro est un nombre d'Armstrong
if est_nombre_armstrong(numero):
    print(numero, "est un nombre Armstrong")
else:
    print(numero, "n'est pas un nombre Armstrong")