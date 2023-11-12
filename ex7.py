#Écrire une fonction qui calcule le montant total dépensé par tous les clients.

clients = [
    {"nom": "Alice Dupont", "email": "alice.dupont@example.com", "montant_depense": 1000},
    {"nom": "Bob Martin", "email": "bob.martin@example.com", "montant_depense": 1500},
    {"nom": "Claire Lambert", "email": "claire.lambert@example.com", "montant_depense": 80},
    {"nom": "David Lefevre", "email": "david.lefevre@example.com", "montant_depense": 120},
    {"nom": "Emma Moreau", "email": "emma.moreau@example.com", "montant_depense": 90},
    {"nom": "Franck Rocher", "email": "franck.rocher@example.com", "montant_depense": 110},
    {"nom": "Gabrielle Girard", "email": "gabrielle.girard@example.com", "montant_depense": 130},
    {"nom": "Hugo Dufresne", "email": "hugo.dufresne@example.com", "montant_depense": 95},
    {"nom": "Inès Gauthier", "email": "ines.gauthier@example.com", "montant_depense": 85},
    {"nom": "Julien Mercier", "email": "julien.mercier@example.com", "montant_depense": 120},
    {"nom": "Kelly Bertrand", "email": "kelly.bertrand@example.com", "montant_depense": 100},
    {"nom": "Lucie Boucher", "email": "lucie.boucher@example.com", "montant_depense": 90},
    {"nom": "Maxime Giroux", "email": "maxime.giroux@example.com", "montant_depense": 110},
    {"nom": "Nina Chevalier", "email": "nina.chevalier@example.com", "montant_depense": 130},
    {"nom": "Olivier Tremblay", "email": "olivier.tremblay@example.com", "montant_depense": 85},
    {"nom": "Pauline Lemoine", "email": "pauline.lemoine@example.com", "montant_depense": 95},
    {"nom": "Quentin Deschamps", "email": "quentin.deschamps@example.com", "montant_depense": 120},
    {"nom": "Rose Perrin", "email": "rose.perrin@example.com", "montant_depense": 90},
    {"nom": "Sylvain Caron", "email": "sylvain.caron@example.com", "montant_depense": 110},
    {"nom": "Tessa Roy", "email": "tessa.roy@example.com", "montant_depense": 130},
    {"nom": "Ulysse Lefevre", "email": "ulysse.lefevre@example.com", "montant_depense": 100},
    {"nom": "Victoria Dubois", "email": "victoria.dubois@example.com", "montant_depense": 80},
    {"nom": "William Henry", "email": "william.henry@example.com", "montant_depense": 95},
    {"nom": "Xavier Bertrand", "email": "xavier.bertrand@example.com", "montant_depense": 120},
    {"nom": "Yasmine Legrand", "email": "yasmine.legrand@example.com", "montant_depense": 90},
    {"nom": "Zoé Renard", "email": "zoe.renard@example.com", "montant_depense": 110},
    {"nom": "Adam Moreau", "email": "adam.moreau@example.com", "montant_depense": 130},
    {"nom": "Béatrice Leclerc", "email": "beatrice.leclerc@example.com", "montant_depense": 85},
    {"nom": "Charles Royer", "email": "charles.royer@example.com", "montant_depense": 95},
    {"nom": "Diane Lefevre", "email": "diane.lefevre@example.com", "montant_depense": 120},
    {"nom": "Éric Bergeron", "email": "eric.bergeron@example.com", "montant_depense": 90},
    {"nom": "Fiona Mercier", "email": "fiona.mercier@example.com", "montant_depense": 110},
    {"nom": "Gilles Leroux", "email": "gilles.leroux@example.com", "montant_depense": 130},
    {"nom": "Hélène Deschamps", "email": "helene.deschamps@example.com", "montant_depense": 100},
    {"nom": "Ivan Gagnon", "email": "ivan.gagnon@example.com", "montant_depense": 80},
    {"nom": "Jessica Bouchard", "email": "jessica.bouchard@example.com", "montant_depense": 95},
    {"nom": "Karl Martel", "email": "karl.martel@example.com", "montant_depense": 120},
    {"nom": "Léa Lavoie", "email": "lea.lavoie@example.com", "montant_depense": 90},
    {"nom": "Marc Girard", "email": "marc.girard@example.com", "montant_depense": 110},
    {"nom": "Nadia Richard", "email": "nadia.richard@example.com", "montant_depense": 130},
    {"nom": "Olivier Fournier", "email": "olivier.fournier@example.com", "montant_depense": 85},
    {"nom": "Pauline Gosselin", "email": "pauline.gosselin@example.com", "montant_depense": 95},
    {"nom": "Quentin Lemieux", "email": "quentin.lemieux@example.com", "montant_depense": 120},
    {"nom": "Roxane Leclair", "email": "roxane.leclair@example.com", "montant_depense": 90},
    {"nom": "Samuel Lambert", "email": "samuel.lambert@example.com", "montant_depense": 110},
    {"nom": "Tania Lavoie", "email": "tania.lavoie@example.com", "montant_depense": 130},
    {"nom": "Ulysse Boucher", "email": "ulysse.boucher@example.com", "montant_depense": 100},
    {"nom": "Victoria Robert", "email": "victoria.robert@example.com", "montant_depense": 80},
    {"nom": "William Gagnon", "email": "william.gagnon@example.com", "montant_depense": 95},
    {"nom": "Xavier Lefevre", "email": "xavier.lefevre@example.com", "montant_depense": 120},
    {"nom": "Yasmine Martin", "email": "yasmine.martin@example.com", "montant_depense": 90},
    {"nom": "Zoé Morin", "email": "zoe.morin@example.com", "montant_depense": 110},
]

def montant_total_depense(clients):
    montant_total = 0
    for client in clients:
        montant_total += client["montant_depense"]
    return montant_total

total_depenses = montant_total_depense(clients)
print(f"Le montant total dépensé par tous les clients est de : {total_depenses}€")

       
