from fltk.fltk import fltk

fltk.cree_fenetre(500, 500, redimension=True)
# fltk.plein_ecran()

# root: fltk.tk.Tk = fltk.__canevas.root # tk.Tk()

# screen_width = fltk.__canevas.root.winfo_screenwidth()
# screen_height = fltk.__canevas.root.winfo_screenheight()

# print(screen_height, screen_width)

# Set the window size to the screen width and height
# fltk.__canevas.root.attributes("-fullscreen", True)


class MaterialButton():
    pass

# Design with classes in tkinter https://www.youtube.com/watch?v=eaxPK9VIkFM

fltk.rectangle(0, 0, fltk.largeur_fenetre()/2, fltk.hauteur_fenetre(), remplissage="#0096FF")
while True:
    fltk.attend_clic_gauche()
    fltk.redimensionne_fenetre(800, 800)
    print("fenetetrée", fltk.largeur_fenetre(), fltk.hauteur_fenetre())
    fltk.attend_clic_gauche()
    fltk.plein_ecran()
    print("plein écran", fltk.largeur_fenetre(), fltk.hauteur_fenetre())

while True:
    fltk.plein_ecran()
    print("plein écran", fltk.largeur_fenetre(), fltk.hauteur_fenetre())
    fltk.attend_clic_gauche()
    fltk.redimensionne_fenetre(500, 500)
    print("fenetetrée", fltk.largeur_fenetre(), fltk.hauteur_fenetre())
    fltk.rectangle(0, 0, fltk.largeur_fenetre(), fltk.hauteur_fenetre(), remplissage="#0096FF")
    fltk.attend_clic_gauche()

while True:
    ev = fltk.attend_ev()
    tev = type(ev)
    print(ev, tev)

fltk.attend_fermeture()