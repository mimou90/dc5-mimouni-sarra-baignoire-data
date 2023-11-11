#Créez une liste des dépenses marketing mensuelles et calculez les dépenses totales de l'année

depenses_mensuelles = [1200, 1500, 800, 1100, 1300, 1000, 900, 1200, 950, 1100, 1300, 1000]

depenses_annuelles = 0
for depense in depenses_mensuelles:
    depenses_annuelles += depense

print(f"Les dépenses marketing mensuelles sont : {depenses_mensuelles}")
print(f"Les dépenses totales de l'année sont : {depenses_annuelles}")
