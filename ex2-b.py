# Créez une liste de 10 nombres, trouvez le maximum, le minimum, et calculez la moyenne.

liste_nombres = [42, 17, 8, 94, 56, 23, 70, 12, 35, 50]

if not liste_nombres:
    print("Erreur : La liste est vide.")
else:
    maximum = minimum = liste_nombres[0]
    somme = 0
    nombre_elements = 0

    for nombre in liste_nombres:
        if nombre > maximum:
            maximum = nombre
        if nombre < minimum:
            minimum = nombre
        somme += nombre
        nombre_elements += 1

    moyenne = somme
    if nombre_elements > 0:
        moyenne = moyenne // nombre_elements

    print(f"Maximum : {maximum}")
    print(f"Minimum : {minimum}")
    print(f"Moyenne : {moyenne}")
