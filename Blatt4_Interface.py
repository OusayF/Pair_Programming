''' User Interface of the game
'''

__author__ = "5984035, Laßmann, XXXXXX, XXXXXX"




# gültige Eingaben
print("Drücken Sie einfach die Enter Taste um erneut zu würfeln. \n\
Wenn Sie das Spiel beenden möchten geben Sie 'Ende' ein. \n\
Wenn Sie ein neues Spiel starten möchten dann geben Sie 'neu' ein.")
#print(players, "ist an der Reihe.")
def game_menu(input_player):
    '''
    '''
    input_player = input_player.strip().lower()
    if input_player == "\n" :
        #sixteen_is_dead(players)
        return True
    elif input_player == "n":
        #players += 1 # noch nicht richtig
        #sixteen_is_dead(players)
        return True
    elif input_player == "ende":
        print("Das Spiel wird beendet.")
        quit()
        return True
    elif input_player == "neu":
        print("Neues Spiel wird gestartet.")
        #sixteen_is_dead(players)
        return True
    else:
        return False
    while input_player != "n":
        print("Ihre Eingabe ist leider ungültig, versuchen Sie es erneut.")
        game_menu(input_player)
        
