#Utilisez la bibliothèque `pandas` pour lire un fichier CSV contenant des données de ventes et affichez les cinq premières lignes

import pandas as pd
df = pd.read_csv('fichier.csv')
df.head(5)

