def tri_decroissant(tab):
    n = len(tab)
    # Parcourir tous les éléments du tableau
    for i in range(n):
        # Trouver le maximum non trié dans le reste du tableau
        max_index = i
        for j in range(i+1, n):
            if tab[j] > tab[max_index]:
                max_index = j
        # Échanger l'élément maximum avec le premier élément non trié
        tab[i], tab[max_index] = tab[max_index], tab[i]
    return tab

# Exemple d'utilisation
import random

# Génération d'un tableau aléatoire de plus de 15 indices
tableau = [random.randint(1, 100) for _ in range(20)]

print("Tableau avant le tri :", tableau)
tableau_trie = tri_decroissant(tableau)
print("Tableau après le tri :", tableau_trie)