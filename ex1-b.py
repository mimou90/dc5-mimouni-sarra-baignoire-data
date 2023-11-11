#Manipulation de chaînes : Demandez à l'utilisateur de saisir une phrase, puis affichez la phrase en majuscules, en minuscules et le nombre de mots


def Majuscules(chaine):
    chaine_majuscules = []
    for caractere in chaine:
        valeur_ascii = ord(caractere)
        if 97 <= valeur_ascii <= 122:
            caractere_majuscule = chr(valeur_ascii - 32)
        else:
            caractere_majuscule = caractere
        chaine_majuscules.append(caractere_majuscule)
    return chaine_majuscules

def Minuscules(chaine):
    chaine_minuscules = []
    for caractere in chaine:
        valeur_ascii = ord(caractere)
        if 65 <= valeur_ascii <= 90:
            caractere_minuscule = chr(valeur_ascii + 32)
        else:
            caractere_minuscule = caractere
        chaine_minuscules.append(caractere_minuscule)
    return chaine_minuscules

phrase_utilisateur = input("Veuillez saisir une phrase : ")

# Gestion de l'erreur si la phrase est vide
if not phrase_utilisateur:
    print("Erreur : La phrase est vide.")
else:
    phrase_en_majuscules = Majuscules(phrase_utilisateur)
    phrase_en_minuscules = Minuscules(phrase_utilisateur)

    nombre_mots = 0
    precedent_alphanum = False
    precedent_ponctuation = False

    for caractere in phrase_utilisateur:
        if ('a' <= caractere <= 'z') or ('A' <= caractere <= 'Z') or ('0' <= caractere <= '9') or caractere in "àâäéèêëïîôöùûüç":
            if not precedent_alphanum:
                nombre_mots += 1
            precedent_alphanum = True
            precedent_ponctuation = False 
        else:
            if caractere in "'-!.?,":
                if not precedent_ponctuation:
                    nombre_mots += 1
                precedent_ponctuation = True
            else:
                precedent_ponctuation = False
            precedent_alphanum = False

    print("Phrase en majuscules :", ''.join(phrase_en_majuscules))
    print("Phrase en minuscules :", ''.join(phrase_en_minuscules))
    print("Nombre de mots dans la phrase :", nombre_mots)



