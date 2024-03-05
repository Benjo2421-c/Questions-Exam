# Q6
# Ce script sert à corriger des listes de noms ayant des espaces superflus.
# On répète les mêmes lignes de code pour chaque groupe.
# Écrivez une fonction qui permettra d'enlever la duplication de code.
# La structure de la fonction est déjà amorcée.
# L'exécution de votre script devra donner le même résultat que l'exécution du script original
#       c'est-à-dire 3 nouvelles listes de groupes contenant les mêmes noms mais sans espaces superflus.


liste_noms_groupe1 = [" Anna Jacobs","Bertand Dupier ", "Catherine Deschamps", "   William Dupont", "     Loise Vilmar  ", " Toca Lombe"]
liste_noms_groupe2 = [" Mienne Lambert", " Justin Tremblay", " Pok Holmes", "Gertrude Dupé", "Harry Potter   ", "   Garry Smother"]
liste_noms_groupe3 = ["Gard Longe ", " Untel Aknom ", "William Dupont III ", " Steven Stevenson  "]

def correction_espaces_supp(liste_nom:list[str]):
    list_nom_strip = []
    for nom in liste_nom:
        nom_corriger = nom.strip()
        list_nom_strip.append(nom_corriger)
    return list_nom_strip


print(correction_espaces_supp(liste_noms_groupe1))
print(correction_espaces_supp(liste_noms_groupe2))
print(correction_espaces_supp(liste_noms_groupe2))