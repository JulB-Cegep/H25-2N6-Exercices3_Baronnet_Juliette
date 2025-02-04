# importez os
# # allez dans le dossier Ex3 Videos
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier


import os
os.system('cls')

os.chdir("Ex3 Videos")
for file in os.listdir() :
    nom, extension = os.path.splitext(file)
    titre, cours, numéro = nom.split("_")
    t = titre.strip()
    c = cours.strip()
    n = numéro.strip()
    n2 = n[1:]
    n3 = n2.zfill(2)
    os.rename(file, f"{t}_{c}_#{n3}.{extension}")

