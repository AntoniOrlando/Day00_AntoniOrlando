def tri_croissant(tab):
    n = len(tab)
    # Parcourir tous les éléments du tableau
    for i in range(n):
        # Trouver le minimum non trié dans le reste du tableau
        min_index = i
        for j in range(i+1, n):
            if tab[j] < tab[min_index]:
                min_index = j
        # Échanger l'élément minimum avec le premier élément non trié
        tab[i], tab[min_index] = tab[min_index], tab[i]
    return tab

# Exemple d'utilisation
import random

# Génération d'un tableau aléatoire de plus de 15 indices
tableau = [random.randint(1, 100) for _ in range(20)]

print("Tableau avant le tri :", tableau)
tableau_trie = tri_croissant(tableau)
print("Tableau après le tri :", tableau_trie)