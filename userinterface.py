__author__ = "7422328, Cevik"
 


def game_rules():
    """
    It's the starting screen which the user will see.
    """
    print("----------------------------------------------------------")
    print("                      Spielregeln:                        ")
    print("----------------------------------------------------------")
    print("""Jeder Spieler hat eine unbegrenzte Anzahl an versuchen das
Ziel ist hierbei so nah wie möglich an die Zahl '16' heran 
zu kommen, der Spieler der am ende am nahsten ist, hat 
gewonnen.
    """)

game_rules()



def user_main_menue():
    """
    It's the starting screen which the user will see.
    """
    print("|          Herzlich Willkommen bei '16-ist-tot'         |")
    print("|                         ^-^                           |")
    print("|-------------------------------------------------------|")
    print("|                         Menü                          |")
    print("|-------------------------------------------------------|")
    print("|             Wählen Sie bitte etwas aus:               |")
    print("|                                                       |")
    print("|       1 = Singleplayer (Spieler vs Computer)          |")
    print("|       2 = Multiplayer (Spieler vs Spieler)            |")
    print("|       r = Regeln                                      |")
    print("|                                                       |")
    print("|       e = Exit / Beenden des Spiels                   |")
    print("|-------------------------------------------------------|")
    
      
user_main_menue() 



def winning_screen():
    print(" ")
    print("")
    print(" ~~~~~~~~~~~~Glückwunsch Sie haben gewonnen!!!~~~~~~~~~~~")
    print("")
    print(" ")



winning_screen()


def loosing_screen():
    print(":-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(")
    print("")
    print("~~~~~~~~~~~~~Sie haben leider verloren~~~~~~~~~~~~~~~~~~~")
    print("")
    print(":-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-(")

loosing_screen()