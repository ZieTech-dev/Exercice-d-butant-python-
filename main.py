from Equipe import Equipe

nation1 = Equipe("Cote d'Ivoire")
nation1.joueurs.extend(["Serge Aurier", "Serge Aurier","Ousmane Diomandé","Franck Kessié","Simon Adingra"])

nation2 = Equipe("Ghana")
nation2.joueurs.extend(["Abedi Pelé","Jordan Ayew","Louis Mafouta ","Richard Ofori"])

nation3 = Equipe("Senegale")
nation3.joueurs.extend(["Sadio Mané","D. Lopy ","P. Gueye"])

nation4 = Equipe("Egypte")
nation4.joueurs.extend(["Salah","Mohamed Gabal"])

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
            nom = input("Entrez le nom de la nouvelle équipe: ")
            Equipe.creer_equipe(nom)
            print(f"L'équipe '{nom}' a été créée.")
            reponse = input("voulez vous ajouter une nouvelle equipe ?(1: oui ; 0 :non)\n choisissez une option: ")
            if reponse == "0":
                print("Fin d'implementation des equipes")
                break
            elif reponse != "0" and reponse !="1":
                print("Option invalide.")
                break
    
    elif choix == "2":
        nom = input("Entrez le nom de l'équipe à modifier: ")
        equipe = Equipe.trouver_equipe(nom)
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
        nom = input("Entrez le nom de l'équipe à supprimer: ")
        equipe = Equipe.trouver_equipe(nom)
        if equipe:
            equipe.supprimer()
            print(f"L'équipe '{nom}' a été supprimée.")
        else:
            print(f"L'équipe '{nom}' n'a pas été trouvée.")
    
    elif choix == "4":
        equipes = Equipe.lister_equipes()
        if equipes:
            print("Équipes actuelles:")
            for equipe in Equipe.instances:
                print(f"- {equipe.nom}")
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
        break
    
    else:
        print("Option invalide. Veuillez réessayer.")
