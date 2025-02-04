import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script
os.system('cls')
import csv


# Tu as toujours rêvé de travailler un jour pour le CH
# Tu as vu une job en TI, 
#           Analyste, soutien technique réseau

# Le fichier Ex3 Competences.csv contient la liste des compétences qu'ils demandent, 
# #         avec le niveau et le fait que cette compétence est exigée ou plutôt un atout
# Bien que tu n'as pas encore fini tes études tu veux imprimer ici les compétences qui sont exigées 
# afin de bien développer ces compétences pour qu'éventuellement tu puisses entrer dans cette entreprise

#  Si vous êtes à l'aise en programmation allez-y
#  Des instructions détaillées sont données plus bas

ficher_a_lire = os.path.join("csvs", "Ex6 Competences.csv")

with open (ficher_a_lire, 'r', encoding = 'utf-8') as fichier :
    lecteur = csv.reader(fichier, delimiter = '/')
    for ligne in lecteur :
        if(ligne[2] == 'Exigé') :
            print(ligne)
    



# INSTRUCTIONS DÉTAILLÉES
#Ouvrez en lecture le fichier Ex6 Competences.csv
#avec l'encodage et le delimiter requis
#Imprimez la première ligne
#Faites une boucle pour passer à travers chacune des lignes du fichier
#Si l'exigence est  'Exigé' imprimez cette ligne
