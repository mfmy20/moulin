#from IA import *
from tkinter import *

debug_IA = "true"




class Arbre(object):

    def __init__(self, profondeur, joueur, jeton, valeur=0):
        self.profondeur = profondeur
        self.joueur = joueur
        self.jeton = jeton
        self.valeur = valeur
        self.IA = []
        self.IAJoue()

    def IAJoue(self):
        global jeton_simulé
        max_val = -1000000
        for J in jeton:
            if jeton[J] == "":
                jeton[J] = "black"
                jeton_simulé = J
                val = Min( jeton_simulé, self.profondeur-1)
                if val > max_val:
                    max_val = val
                    MeilleurCoup = J
                jeton[J] = ""
        print(MeilleurCoup)

def realval(jeton_simulé):
    val = 0
    list_ColoneIA(jeton_simulé)
    for l in listdeslist:
        valeur_noir = listdeslist[l].count("black")
        valeur_blanc = listdeslist[l].count("white")
        if valeur_noir == 0:
            if valeur_blanc == 3:
                val = val-100
            elif valeur_blanc == 2:
                val = val-50
            elif valeur_blanc == 1:
                val = val - 10
        if valeur_noir == 1:
            if valeur_blanc == 2:
                val = val+25
            elif valeur_blanc == 0:
                val = val+10
        if valeur_noir == 2:
            if valeur_blanc == 1:
                val = val-25
            else:
                val = val+50
        if valeur_noir == 3:
            val = val+100
    listdeslist[colone_supprimer].pop()
    listdeslist[ligne_supprimer].pop()
    if nbr_noir > nbr_blanc:
        val = val+25
    elif nbr_blanc > nbr_noir:
        val = val+25
    return val

def list_ColoneIA(jeton_simulé):
    global colone_supprimer,ligne_supprimer
    for l in listdeslist:
        if jeton_simulé[2] == l:
            listdeslist[l].append(jeton[jeton_simulé])
            colone_supprimer = l
        elif jeton_simulé[3] == l:
            listdeslist[l].append(jeton[jeton_simulé])
            ligne_supprimer = l
        
def Min( jeton_simulé, profondeur):
    if profondeur == 0:
        return realval(jeton_simulé)
    else:
        min_val = 1000000
        for J in jeton:
            if jeton[J] == "":
                jeton[J] = "white"
                jeton_simulé = J
                val = Max( jeton_simulé, profondeur-1)
                if val < min_val:
                    min_val = val
                jeton[J] = ""
        return min_val

def Max( jeton_simulé, profondeur):
    if profondeur == 0:
        return realval( jeton_simulé)
    else:
        max_val = -1000000
        for J in jeton:
            if jeton[J] == "":
                jeton[J] = "black"
                jeton_simulé = J
                val = Min( jeton_simulé, profondeur-1)
                if val > max_val:
                    max_val = val
                jeton[J] = ""
        return max_val


def test(jeton):
    global joueur,arbre
    joueur = -1
    profondeur = 2
    arbre = Arbre(profondeur, joueur, jeton)































debug = "false"

couleur = "white"

que_moulin = "true"

jeton_saisie = []

nbr_jeton = 0

nbr_noir = 0

nbr_blanc = 0

joueur = 1

fenetre = Tk()

jeton = {(200, 50, 'A', 'a', 1, 1): "", (600, 50, 'D', 'a', 1, 2): "", (200, 450, 'A', 'd', 2, 1): "",
         (1000, 50, 'G', 'a', 1, 3): "", (200, 850, 'A', 'g', 3, 1): "",
         (600, 850, 'H', 'g', 3, 2): "", (1000, 450, 'G', 'h', 2, 3): "", (1000, 850, 'G', 'g', 3, 3): "",
         (325, 175, 'B', 'b', 1, 1): "", (600, 175, 'D', 'b', 2, 2): "",
         (325, 450, 'B', 'd', 2, 2): "", (875, 175, 'F', 'b', 1, 3): "", (325, 725, 'B', 'f', 3, 1): "",
         (875, 450, 'F', 'h', 2, 2): "", (600, 725, 'H', 'f', 2, 2): "",
         (875, 725, 'F', 'f', 3, 3): "", (450, 300, 'C', 'c', 1, 1): "", (600, 300, 'D', 'c', 3, 2): "",
         (450, 450, 'C', 'd', 2, 3): "", (750, 300, 'E', 'c', 1, 3): "",
         (450, 600, 'C', 'e', 3, 1): "", (750, 450, 'E', 'h', 2, 1): "", (600, 600, 'H', 'e', 1, 2): "",
         (750, 600, 'E', 'e', 3, 3): ""}

A = []
a = []
B = []
b = []
C = []
c = []
D = []
d = []
E = []
e = []
F = []
f = []
G = []
g = []
H = []
h = []
white = ["white", "white", "white"]
black = ["black", "black", "black"]

jeton_blanc = {(50, 25): "white", (50, 150): "white", (50, 275): "white", (50, 400): "white",
               (50, 525): "white", (50, 650): "white", (50, 775): "white", (50, 900): "white"}

jeton_noir = {(1150, 25): "black", (1150, 150): "black", (1150, 275): "black", (1150, 400): "black",
              (1150, 525): "black", (1150, 650): "black", (1150, 775): "black", (1150, 900): "black"}

listdeslist = {'A': A, 'a': a, 'B': B, 'b': b, 'C': C, 'c': c, 'D': D, 'd': d, 'E': E, 'e': e, 'F': F, 'f': f, 'G': G,
               'g': g, 'H': H, 'h': h}

def exit_game(event):
    fenetre.destroy()
    exit()


def fin_du_jeu():
    if perdant == "white":
        text_gagnant = "Les noirs ont gagné"
        text_perdant = "Les blancs ont perdu"
    else:
        text_gagnant = "Les blancs ont gagné"
        text_perdant = "Les noirs ont perdu"
    fin = Toplevel()
    fin.title("Fin")
    msg = Message(fin, text=text_gagnant)
    msg_2 = Message(fin, text=text_perdant)
    msg.pack()
    msg_2.pack()


def changer_joueur():
    global couleur
    if couleur != "white":
        couleur = "white"
    else:
        couleur = "black"


def fin_tour():
    global joueur, jeton
    changer_joueur()
    plateau.create_rectangle(630, 5, 670, 45, fill=couleur)
    if joueur == 1:
        test(jeton)
    else:
        joueur = 1
        plateau.bind("<Button-1>", poser)


def jeton_par_position(x, y):
    global jeton
    for c in jeton:
        if c[0] <= x <= c[0] + 100 and c[1] <= y <= c[1] + 100:
            return c
    return None


def verification_moulin():
    global moulin
    moulin = "false"
    if debug == "true":
        print("vérification ", listdeslist[l])
    if listdeslist[l] == white:
        moulin = "true"
        if debug == "true":
            print(moulin, "blanc")
    elif listdeslist[l] == black:
        moulin = "true"
        if debug == "true":
            print(moulin, "noir")
    else:
        if debug == "true":
            print("pas de moulin")


def uniquement_moulin():
    global que_moulin
    changer_joueur()
    nbr_moulin = 0
    que_moulin = "true"
    for c in jeton:
        if jeton[c] == couleur and jeton[c] != "":
            for l in listdeslist:
                if c[2] == l:
                    if listdeslist[l] == white:
                        nbr_moulin = nbr_moulin + 1
                    elif listdeslist[l] == black:
                        nbr_moulin = nbr_moulin + 1
                    else:
                        nbr_moulin = nbr_moulin - 1
                elif c[3] == l:
                    if listdeslist[l] == white:
                        nbr_moulin = nbr_moulin + 1
                    elif listdeslist[l] == black:
                        nbr_moulin = nbr_moulin + 1
                    else:
                        nbr_moulin = nbr_moulin - 1
            if nbr_moulin < 0:
                que_moulin = "false"
            if debug == "true":
                print(que_moulin, nbr_moulin)
            nbr_moulin = 0
    changer_joueur()


def reconstitution_list():
    for l in listdeslist:
        listdeslist[l].clear()
    for c in jeton:
        for l in listdeslist:
            if c[2] == l and jeton[c] != "":
                listdeslist[l].append(jeton[c])
            elif c[3] == l and jeton[c] != "":
                listdeslist[l].append(jeton[c])
    if debug == "true":
        print(listdeslist)


def incrementation_jeton():
    global nbr_noir, nbr_blanc
    deja_fait = 0
    if couleur == "white":
        nbr_blanc = nbr_blanc + 1
        for c in jeton_blanc:
            if jeton_blanc[c] == "white" and deja_fait == 0:
                jeton_blanc[c] = ""
                plateau.create_oval(c[0], c[1], c[0] + 100, c[1] + 100, fill="red")
                deja_fait = 1
    else:
        nbr_noir = nbr_noir + 1
        for c in jeton_noir:
            if jeton_noir[c] == "black" and deja_fait == 0:
                jeton_noir[c] = ""
                plateau.create_oval(c[0], c[1], c[0] + 100, c[1] + 100, fill="red")
                deja_fait = 1


def reduction_jeton():
    global nbr_noir, nbr_blanc
    deja_fait = 0
    if couleur == "black":
        nbr_blanc = nbr_blanc - 1
        for c in jeton_noir:
            if jeton_noir[c] == "" and deja_fait == 0:
                jeton_noir[c] = "white"
                plateau.create_oval(c[0], c[1], c[0] + 100, c[1] + 100, fill="white")
                deja_fait = 1
    else:
        nbr_noir = nbr_noir - 1
        for c in jeton_blanc:
            if jeton_blanc[c] == "" and deja_fait == 0:
                jeton_blanc[c] = "black"
                plateau.create_oval(c[0], c[1], c[0] + 100, c[1] + 100, fill="black")
                deja_fait = 1


def verification_case():
    global coup_possible
    coup_possible = "false"
    for c in jeton:
        if jeton[c] == couleur:
            for k in jeton:
                if c[2] == k[2] and abs(k[4] - c[4]) == 1 and jeton[k] == "":
                    coup_possible = "true"
                if c[3] == k[3] and abs(k[5] - c[5]) == 1 and jeton[k] == "":
                    coup_possible = "true"


def poser(event):
    X = event.x
    Y = event.y
    global J, moulin, jeton, nbr_jeton, perdant
    J = jeton_par_position(X, Y)
    moulin = "false"
    if debug == "true":
        print("jeton posé", nbr_jeton)
    if nbr_jeton >= 16:
        if nbr_noir < 3:
            perdant = "black"
            fin_du_jeu()
            plateau.bind("<Button-1>", exit_game)
        elif nbr_blanc < 3:
            perdant = "white"
            fin_du_jeu()
            plateau.bind("<Button-1>", exit_game)
        else:
            plateau.bind("<Button-1>", saisir)
    elif J and jeton[J] == "" and nbr_jeton < 16:
        incrementation_jeton()
        nbr_jeton = nbr_jeton + 1
        if debug == "true":
            print("poser ", couleur, J, "noir", nbr_noir, "blanc", nbr_blanc)
        jeton[J] = couleur
        plateau.create_oval(J[0], J[1], J[0] + 100, J[1] + 100, fill=couleur)
        colone_ligne()
        if debug == "true":
            print("en poser ", moulin)
        if moulin == "true":
            plateau.bind("<Button-1>", faire_moulin)
        else:
            fin_tour()


def colone_ligne():
    global l
    if debug == "true":
        print("colone ", couleur)
    for l in listdeslist:
        if J[2] == l:
            listdeslist[l].append(jeton[J])
            verification_moulin()
        elif J[3] == l:
            listdeslist[l].append(jeton[J])
            verification_moulin()


def colone_ligne_moulin():
    global l
    if debug == "true":
        print("colone ", couleur)
    for l in listdeslist:
        if J[2] == l:
            verification_moulin()
        elif J[3] == l:
            verification_moulin()


def faire_moulin(event):
    X = event.x
    Y = event.y
    global moulin, J
    moulin = "false"
    J = jeton_par_position(X, Y)
    if debug == "true":
        print("moulin ", moulin)
    if J and jeton[J] != couleur and jeton[J] != "":
        colone_ligne_moulin()
        uniquement_moulin()
        if moulin == "false":
            if debug == "true":
                print("yes")
            jeton[J] = ""
            plateau.create_oval(J[0], J[1], J[0] + 100, J[1] + 100, fill="red")
            reconstitution_list()
            reduction_jeton()
            fin_tour()
        elif que_moulin == "true":
            if debug == "true":
                print("nop")
            fin_tour()


def saisir(event):
    X = event.x
    Y = event.y
    global J, jeton_saisie, detruire, perdant
    J = jeton_par_position(X, Y)
    if debug == "true":
        print("deplacer ", couleur, J)
    if J and jeton[J] == couleur:
        detruire = plateau.create_oval(J[0], J[1], J[0] + 100, J[1] + 100, width=5, outline="orange", fill=jeton[J])
        jeton_saisie = J
        verification_case()
        if coup_possible == "false":
            perdant = couleur
            fin_du_jeu()
            plateau.bind("<Button-1>", exit_game)
        else:
            plateau.bind("<Button-1>", deplacer)


def deplacer(event):
    X = event.x
    Y = event.y
    global J, moulin, jeton, jeton_saisie
    J = jeton_par_position(X, Y)
    plateau.bind("<Button-3>", annuler_selection)
    if debug == "true":
        print("en ", J)
    moulin = "false"
    if J and jeton[J] == "":
        if debug == "true":
            print("déplacer", J, detruire)
        if (nbr_blanc == 3 and couleur == "white") or (nbr_noir == 3 and couleur == "black"):
            jeton[jeton_saisie] = ""
            plateau.delete(detruire)
            plateau.create_oval(jeton_saisie[0], jeton_saisie[1], jeton_saisie[0] + 100, jeton_saisie[1] + 100,
                                fill="red")
            reconstitution_list()
            jeton[J] = couleur
            plateau.create_oval(J[0], J[1], J[0] + 100, J[1] + 100, fill=couleur)
            colone_ligne()
            if moulin == "true":
                plateau.bind("<Button-1>", faire_moulin)
            else:
                fin_tour()
        else:
            if (J[2] == jeton_saisie[2] and abs(J[4] - jeton_saisie[4]) == 1) or (
                    J[3] == jeton_saisie[3] and abs(J[5] - jeton_saisie[5]) == 1):
                plateau.delete(detruire)
                jeton[jeton_saisie] = ""
                plateau.create_oval(jeton_saisie[0], jeton_saisie[1], jeton_saisie[0] + 100, jeton_saisie[1] + 100,
                                    fill="red")
                reconstitution_list()
                jeton[J] = couleur
                plateau.create_oval(J[0], J[1], J[0] + 100, J[1] + 100, fill=couleur)
                colone_ligne()
                if moulin == "true":
                    plateau.bind("<Button-1>", faire_moulin)
                else:
                    fin_tour()
            else:
                if debug == "true":
                    print(coup_possible)
                if coup_possible == "true":
                    plateau.delete(detruire)
                    plateau.bind("<Button-1>", saisir)


def annuler_selection(event):
    if debug == "true":
        print("YEP")
    plateau.delete(detruire)
    plateau.bind("<Button-1>", saisir)


plateau = Canvas(fenetre, width=1300, height=1025, bg='red')

plateau.create_text(575, 25, text="Au tour de")

plateau.create_rectangle(630, 5, 670, 45, fill="white")

for c in jeton:
    plateau.create_oval(c[0], c[1], c[0] + 100, c[1] + 100)

ligne = [(150, 100, 450, 100, 400, 800), (275, 225, 450, 225, 275, 550), (400, 350, 450, 350, 150, 300),
         (500, 150, 500, 175, 0, 550), (825, 500, 850, 500, -550, 0)]
for l in ligne:
    plateau.create_line(l[0] + 150, l[1], l[2] + 150, l[3])
    plateau.create_line(l[0] + l[4] + 150, l[1], l[2] + l[4] + 150, l[3])
    plateau.create_line(l[0] + 150, l[1] + l[5], l[2] + 150, l[3] + l[5])
    plateau.create_line(l[1] + 150, l[0], l[3] + 150, l[2])
    plateau.create_line(l[1] + l[5] + 150, l[0], l[3] + l[5] + 150, l[2])
    plateau.create_line(l[1] + 150, l[0] + l[4], l[3] + 150, l[2] + l[4])
    plateau.create_line(l[0] + l[4] + 150, l[1] + l[5], l[2] + l[4] + 150, l[3] + l[5])
    plateau.create_line(l[1] + l[5] + 150, l[0] + l[4], l[3] + l[5] + 150, l[2] + l[4])

for c in jeton_blanc:
    plateau.create_oval(c[0], c[1], c[0] + 100, c[1] + 100, fill="white")

for c in jeton_noir:
    plateau.create_oval(c[0], c[1], c[0] + 100, c[1] + 100, fill="black")

plateau.bind("<Button-1>", poser)

plateau.pack()

fenetre.mainloop()
