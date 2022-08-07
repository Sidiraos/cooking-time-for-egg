import time
import beepy

def show_options_to_user () :
    print("Veuillez choisir votre cuisson des oeufs")
    print("----------------------------------------")
    print("a) Oeufs à la coque (3mn)\nb) Oeufs mollets (6mn)\nc) Oeufs dur (9mn)")

    return

def get_option_chosen_by_user() :
    option = input("votre choix : ").lower()
    if not (option == "a" or option == "b" or option == "c" ):
        print("ERREUR : choisir entre a , b ou c")
        return get_option_chosen_by_user()
    return option

def show_cooking_duration(option) :
    time_cooking_sec=''
    if option == "a" :
        time_cooking_sec=180
    elif option == "b" :
        time_cooking_sec=360
    elif option == "c" :
        time_cooking_sec =540

    d = time_cooking_sec
    tour = time_cooking_sec//10 #temps de cuisson pour 10 pour faire combien d'affichage en 10s car on affiche tous les 10secondes le temps restant
                                #exemple en 180 on fait 18 tours de 10s

    print("Cuisson en cours" , end="" , flush=True)
    for i in range(tour) :
        for i in range(10) :
            time.sleep(1)
            print("." , end="" , flush=True)
            if i == 9 :
                d -= 10
                min = d//60     # division entière (pas de virgules)
                sec = d-min*60
                print(end="\n")
                print(f"durée restante : {min:02d} : {sec}", end = "" , flush=True)

    print("" , end="\n")

    return

def show_ending_of_cooking():
    print('Cuisson terminée' , end="" , flush=True) #pour que le son du beepy se synchronise en meme temps que le print cuisson car j'ai remarqué une difference de temps il y'avait un peu de retard
    beepy.beep(sound="ping")
    return


show_options_to_user()
option = get_option_chosen_by_user()
show_cooking_duration(option)
show_ending_of_cooking()


