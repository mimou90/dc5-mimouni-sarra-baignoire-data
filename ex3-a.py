#Écrivez un script qui détermine si une campagne a été rentable en comparant le coût de la campagne au revenu généré.

try:
    cout_campagne = 5000
    revenu_genere = 12000

    if revenu_genere > cout_campagne:
        print("La campagne a été rentable.")
    elif revenu_genere == cout_campagne:
        print("La campagne a couvert ses coûts, mais n'a pas généré de bénéfice.")
    else:
        print("La campagne n'a pas été rentable.")

except TypeError:
    print("Erreur : Les valeurs de coût de la campagne ou de revenu généré ne sont pas numériques.")
