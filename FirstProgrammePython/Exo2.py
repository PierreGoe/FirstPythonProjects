"""EXERCICE PYTHON #3
> Créer un programme simulant un combat qui respecte les contraintes suivantes :
    - Deux joueurs, auxquels on demandera de choisir un pseudo
    - Les deux combattants démarrent avec 250 points de vie chacun
    - Le combat se déroule en 4 attaques (Joueur1, Joueur2, Joueur1 et enfin Joueur2)
    - Chaque attaque est une tentative (si elle réussit, le joueur infligera un nombre de dégâts entre 0 et 100 - 
                                        si elle échoue, l'attaque est ratée, et c'est au tour de l'autre joueur)
    - À la fin du combat (les 4 attaques), on déclare le gagnant (celui à qui il reste le plus de points de vie)

> Indications :
    - Le déroulement du combat doit être logique et annoncé à l'utilisateur (affichez du texte, décrivez ce qu'il se passe)
    - Coder dans un premier temps uniquement avec des affichages/saisies, variables, opérations, conditions.
    - Pour les plus avancés, vous pourrez optimiser ce code ensuite en l'adaptant avec vos connaissances (boucles, fonctions, classe, etc.)
"""

import random

random_attack = True 
random_attack = 0
compteur = 1


Joueur1 = "Inconue 1"
Joueur2 = "inconue 2"
Joueur1 = input("Nom du joueur 1")
Joueur2 = input("Non du joueur 2")
pointDeVieJoueur1=250
pointDeVieJoueur2=250
random_damage = 0

print("Début du Combat !")

while compteur < 4 :

    print("ROUND {}".format(compteur))
    print(f"Le joueur {Joueur1} attaque.")

    random_attack = random.randint(0, 1) #Je fait mon tirage au sort pour connaitre le jet pile ou face
    random_attack= bool(random_attack) #Le "cast" en boléen pour eviter les érreure 

    
    if random_attack == True:
        random_damage = random.randint(0, 100)
        pointDeVieJoueur2 = pointDeVieJoueur2 - random_damage
        print("L'attaque a réusis le joueur {} vient de perdre {} il posséde donc {} points de vie".format(Joueur2,random_damage,pointDeVieJoueur2))
        compteur += 1 
    
    else:
        print("Ton attaque à échouer au tour de ton adversaire !")
        compteur += 1 




    print("ROUND {}".format(compteur))
    print("Le joueur {} attaque.".format(Joueur2))

    random_attack = random.randint(0, 1) #Je fait mon tirage au sort pour connaitre le jet pile ou face
    random_attack= bool(random_attack) #Le "cast" en boléen pour eviter les érreure 


    if random_attack == True:
        random_damage = random.randint(0, 100)
        pointDeVieJoueur1 = pointDeVieJoueur1 - random_damage
        print("L'attaque a réusis le joueur {} vient de perdre {} il posséde donc {} points de vie".format(Joueur1,random_damage,pointDeVieJoueur1))
        compteur += 1 
    else:
        print("Ton attaque à échouer au tour de ton adversaire !")    
        compteur += 1  
        

if pointDeVieJoueur1 > pointDeVieJoueur2:
    print("Le joueur {} gagne !".format(Joueur1))
else: 
    print("Le joueur {} gagne !".format(Joueur2))


