fruits = {
    "pomme": "rouge",
    "banane": "jaune",
    "orange": "orange",
}
print("Dictionnaire de fruits : \n")
print(fruits)
print("Couleur de la pomme :", fruits["pomme"])
fruits["kiwi"] = "vert"
print("Ajout du kiwi au dictionnaire : \n", fruits)
fruits["pomme"] = "vert"
print("Changement de la couleur de la pomme : \n", fruits)
del fruits["banane"]
print("Suppression de la banane du dictionnaire : \n", fruits)
print("Vérification si 'kiwi' est dans le dictionnaire :", "kiwi" in fruits)
print("Clés du dictionnaire :", fruits.keys())
print("Valeurs du dictionnaire :", fruits.values())
print("Nombre d'éléments dans le dictionnaire :", len(fruits))

print("Le reste des elements du dictionnaire est :")
print(fruits.items())
