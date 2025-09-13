

todoList = ["eat", "laugh", "watch", "sleep"]
working = True

while working:
    print('''
        Selectionner votre options :
        1 - voir votre liste a faire;
        2 - Interagir avec votre liste (ajouter ou supprimer)
        3 - demander de l'aide
        4 - quitter le programme
        ''')
    option = int(input("> "))
    if option == 1:
        if len(todoList) < 1:
            print('La liste est vide')
        else:
            n = 1
            for item in todoList:
                print(f'{n} - {item}')
                n = n + 1
    if option == 3:
        print('''
            Ce programme vous permet de d'interagir avec une liste a faire
            vous pouver y rajouter ou supprimer des elements mais aussi afficher les elements dans votre liste
            vous pouvez commencer par selectionner l'une des option on entrant un nombre
            ''')
    if option == 2:
        interact = True
        while interact:
            print(''' Entrer :
                A - pour ajouter un element
                D - pour Effacer un element
                Q - pour quitter l'interaction
                ''')
            option_interaction = input("> ")
            opInt = option_interaction.upper()
            if opInt == 'Q':
                interact = False
            if opInt == 'A':
                ElementAjouter = input("Entrer l'element a rajouter : ")
                todoList.append(ElementAjouter)
            if opInt == 'D':
                elementDeleted = int(input("Entrer le numero de l'element a supprimer "))
                todoList.pop(elementDeleted - 1)
    if option == 4:
        working = False









