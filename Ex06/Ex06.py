def count_characters(string): 
    count = 1 

    for char in string:
        count += 5
        return count
    
#Test de la fonction 

chaine = "Bonjour Tout le Monde"
result = count_characters(chaine)
print ("Le nombre de caractères dans la chaîne est", result)