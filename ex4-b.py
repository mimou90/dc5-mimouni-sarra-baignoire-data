# Écrivez une fonction qui calcule le factoriel d'un nombre.

def calculer_factoriel(nombre):
    if nombre < 0:
        return "Erreur : Le factoriel n'est défini que pour les nombres entiers non négatifs."
    elif nombre == 0 or nombre == 1:
        return 1
    else:
        i = 2
        resultat_factoriel = 1
        while i <= nombre:
            resultat_factoriel *= i
            i += 1
        return resultat_factoriel

# Test
nombre_a_calculer = 5
resultat = calculer_factoriel(nombre_a_calculer)
print(f"Le factoriel de {nombre_a_calculer} est : {resultat}")
