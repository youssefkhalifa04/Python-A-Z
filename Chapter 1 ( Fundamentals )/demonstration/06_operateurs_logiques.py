"""Les opérateurs logiques en Python.

Ce fichier présente and, or et not avec des exemples simples.
"""

print("--- Opérateurs logiques ---")

est_majeur = True
possede_billet = False

print("est_majeur and possede_billet =", est_majeur and possede_billet)
print("est_majeur or possede_billet =", est_majeur or possede_billet)
print("not est_majeur =", not est_majeur)

peut_entrer = est_majeur and not possede_billet
print("peut_entrer =", peut_entrer)
