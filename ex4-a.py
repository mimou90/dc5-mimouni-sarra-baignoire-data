# Définissez une fonction pour convertir le CTR (Click-Through Rate) en pourcentage. Testez la fonction avec plusieurs entrées


def calculer_taux_clics_pourcentage(clics, impressions):
    if impressions == 0:
        return "Indéfini - Les impressions ne peuvent pas être zéro."

    taux_clics = (clics / impressions) * 100
    return taux_clics

# Tests

print(f"Taux de clics : {calculer_taux_clics_pourcentage(150, 1000):.2f}%")
print(f"Taux de clics : {calculer_taux_clics_pourcentage(300, 10000):.2f}%")
print(f"Taux de clics : {calculer_taux_clics_pourcentage(75, 500):.2f}%")
