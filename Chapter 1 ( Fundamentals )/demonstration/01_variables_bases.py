"""Les variables en Python : instructions de base.

Ce fichier montre comment créer, modifier et réutiliser des variables.
"""

print("--- Instructions de base sur les variables ---")

prenom = "Amina"
age = 20
ville = "Tunis"

print("Prénom :", prenom)
print("Âge :", age)
print("Ville :", ville)

# Une variable peut changer de valeur.
age = age + 1
print("Âge après un anniversaire :", age)

# On peut aussi affecter une valeur à partir d'une autre variable.
message = prenom + " habite à " + ville
print("Message :", message)
