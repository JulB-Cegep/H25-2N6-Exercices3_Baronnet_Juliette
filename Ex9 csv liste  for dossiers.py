import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script
os.system('cls')
# Importez csv
import csv

 

# Vous utiliserez encore le fichier "Ex7 Lan Party.csv"
# 
#         Vous voulez créer un dossier par Lan Party
#         Et pour chaque Lan Party, créez des sous-dossier pour chaque jeu
#                   (On y mettra éventuellement la liste des participants du Lan qui veulent jouer à ce jeu)
#         ATTENTION: Pour le nom de chaque jeu: changez le ':' pour un '_' et gardez juste les 20 premiers caractères

#         Si besoin, des instructions détaillées sont données plus bas

ficher_a_lire = os.path.join("csvs", 'Ex7 Lan Party.csv')
            
liste = []

with open(ficher_a_lire, 'r', encoding='utf-8') as fichier :
    lecteur = csv.reader(fichier, delimiter = ';' )
    next(fichier)
    for ligne in lecteur :
       for i in [1,2,3] :
        nom = (ligne[i].replace(":", "_"))
        chara = nom[:20] 
        os.makedirs(f"{ligne[0]}/{chara}")










# INSTRUCTIONS DÉTAILLÉES
#      Commencez par créer une liste des différents jeux vide
#      Ouvrez le fichier 'Ex4 Lan Party.csv' en lecture
#      utilisez csv.reader pour lire le fichier avec le bon delimiter
#      Sautez la première ligne de l'entête
#      Faites une boucle pour passer à travers chacune des lignes 
#      Créez un dossier pour le nom du Lan Party
#      Déplacez vous dans ce dossier
#      Utilisez le slicing pour garder uniquement les 3 jeux
#      Faites une boucle pour passer à travers chacun des jeux
#      Pour le nom de chaque jeu: changez le ':' pour un '_' et gardez juste les 20 premiers caractères
#      Créez un dossier pour le jeu avec le nouveau nom de jeu
#      Revenez au dossier parent

