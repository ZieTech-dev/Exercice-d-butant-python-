from Equipe import Equipe
from tinydb import TinyDB, Query
db = TinyDB('db.json') 
# ---- creation de quelque equipe avant le dénbogeur ----

# nation1 = Equipe("Cote d'Ivoire", 10,"B")
# nation1.joueurs.extend(["Serge Aurier", "Serge Aurier","Ousmane Diomandé","Franck Kessié","Simon Adingra"])

# nation2 = Equipe("Ghana", 8,"C")
# nation2.joueurs.extend(["Abedi Pelé","Jordan Ayew","Louis Mafouta ","Richard Ofori"])

# nation3 = Equipe("Senegale", 5 ,"B")
# nation3.joueurs.extend(["Sadio Mané","D. Lopy ","P. Gueye"])

# nation4 = Equipe("Egypte", 4 , "C")
# nation4.joueurs.extend(["Salah","Mohamed Gabal"])

while True:
    print("\n--- Menu ---")
    print("1. Créer une nouvelle équipe")
    print("2. Modifier une équipe existante")
    print("3. Supprimer une équipe")
    print("4. Lister les équipes")
    print("5. Quitter")
    choix = input("Choisissez une option: ")

    if choix == "1":
        while True:
            print("\n--- Menu Insertion joueur---")
            nom = input("Entrez le nom de la nouvelle équipe: ")
            point = int(input(f"Enterz le nombre de point de l'equipe '{nom}' :"))
            poule = input(f"Entrez la poule de l'équipe '{nom}' :")
            Equipe(nom=nom, point=point, poule=poule)
            print(f"L'équipe '{nom}' a été créée.")
            reponse = input("voulez vous ajouter une nouvelle equipe ?(1: oui ; 0 :non)\n choisissez une option: ")
            if reponse == "0":
                print("Fin d'implementation des equipes")
                break
            elif reponse != "0" and reponse !="1":
                print("Option invalide.")
                break
    
    elif choix == "2":
        print("\n--- Menu modification ---")
        print("\n--- liste ---")
        equipes = Equipe.lister_equipes()
        if equipes:
            print("Équipes actuelles:")
            i = 0
            for equipe in Equipe.instances:
                print(f"{i}: {equipe.nom}, nombre(s) de points est : {equipe.point} , la poule est : {equipe.poule}")
                i = i + 1
        else:
            print("Aucune équipe n'a été créée.")
        # ---utulisation du nom  pour selectionner l'élement---
        # nom = input("Entrez le nom de l'équipe à modifier: ")
        # equipe = Equipe.trouver_equipe(nom)
        index = int(input("\nEntrez l'index de l'équipe corespondant avec les chiffres :"))
        equipe = Equipe.trouver_equipe_by_index(index)
        
        if equipe:
            print(f"Équipe trouvée: {equipe.nom}")
            print("1. Ajouter un joueur")
            print("2. Supprimer un joueur")
            print("3. Modifier le nom de l'équipe")
            choix_modification = input("Choisissez une option: ")
            
            if choix_modification == "1":
                joueur = input("Entrez le nom du joueur à ajouter: ")
                equipe.ajouter_joueur(joueur)
                print(f"Le joueur '{joueur}' a été ajouté à l'équipe '{equipe.nom}'.")
            
            elif choix_modification == "2":
                joueur = input("Entrez le nom du joueur à supprimer: ")
                if joueur in equipe.joueurs:
                    equipe.supprimer_joueur(joueur)
                    print(f"Le joueur '{joueur}' a été supprimé de l'équipe '{equipe.nom}'.")
                else:
                    print(f"Le joueur '{joueur}' n'existe pas dans l'équipe '{equipe.nom}'.")
            
            elif choix_modification == "3":
                nouveau_nom = input("Entrez le nouveau nom de l'équipe: ")
                equipe.modifier_nom(nouveau_nom)
                print(f"Le nom de l'équipe a été modifié en '{nouveau_nom}'.")
            
            else:
                print("Option invalide.")
        else:
            print(f"L'équipe '{nom}' n'a pas été trouvée.")
    
    elif choix == "3":
        print("\n--- Menu Suppression joueur---")
        nom = input("Entrez le nom de l'équipe à supprimer: ")
        equipe = Equipe.trouver_equipe(nom)
        if equipe:
            equipe.supprimer()
            print(f"L'équipe '{nom}' a été supprimée.")
        else:
            print(f"L'équipe '{nom}' n'a pas été trouvée.")
    
    elif choix == "4":
        print("\n--- liste ---")
        equipes = Equipe.lister_equipes()
        for item in db.all():
            print(f"- {item['Nom']}, nombre de points est : {item['point']} , la poule est : {item['poule']}")
            print("  Liste des joueurs actuels:")
            for joueur in item['joueur']:
                print(f"  - {joueur['nom']}")
        if equipes:
            print("Équipes actuelles:")
            for equipe in Equipe.instances:
                print(f"- {equipe.nom}, nombre de points est : {equipe.point} , la poule est : {equipe.poule}")
                if equipe.joueurs:  
                    print("  Liste des joueurs actuels:")
                    for joueur in equipe.joueurs:
                        print(f"  - {joueur}")
                else:
                    print("  Aucun joueur dans cette équipe.")
        else:
            print("Aucune équipe n'a été créée.")
    
    elif choix == "5":
        
        print("Au revoir!")
        for equipe in Equipe.instances:
            db.insert({'nom': equipe.nom, 'point': equipe.point ,'poule':equipe.poule ,'joueur':[{'nom': joueur} for joueur in equipe.joueurs]})
            # ---- suppression totale du fichier -----
            # db.truncate()
        break
    
    else:
        print("Option invalide. Veuillez réessayer.")

print(db.all())

# --- afficharge de de la suppression du fichier --- 
# print(db.truncate())