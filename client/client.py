if __name__ == "__main__":
    print("\n#\n#  Please lauch __init__.py instead of launching this file.\n#\n")
    exit()
    
from fltk.fltk import fltk
from classes.widgets import *
from classes.pages import *


# fltk.plein_ecran()

# root: fltk.tk.Tk = fltk.__canevas.root # tk.Tk()

# screen_width = fltk.__canevas.root.winfo_screenwidth()
# screen_height = fltk.__canevas.root.winfo_screenheight()

# print(screen_height, screen_width)

# Set the window size to the screen width and height
# fltk.__canevas.root.attributes("-fullscreen", True)





pages = {
    "test": TestPage
}



def main():
    fltk.cree_fenetre(500, 500, redimension=True)
    fltk.rectangle(0, 0, fltk.largeur_fenetre()/2, fltk.hauteur_fenetre(), remplissage="#0096FF")
    fltk.plein_ecran()
    items_to_draw = []
    # page: Page = TestPage(show_topbar=True)
    page: Page = TestPage2(show_topbar=True)
    while True:
        fltk.efface_tout()
        # topbar = TopBar()
        # topbar.draw()
        page.draw()
        for item_to_draw in items_to_draw:
            item_to_draw.draw()
        ev = fltk.attend_ev()
        tev = fltk.type_ev(ev)
        print(ev, tev)
        if tev == "Quitte":
            fltk.ferme_fenetre()
            exit()
        elif tev == "ClicDroit": #ClicGauche in prod, this is for macos tests
            clickables = page.get_clickable_childs()
            for clickable in clickables:
                if clickable.is_clicked(x=fltk.abscisse(ev), y=fltk.ordonnee(ev)):
                    print("Hoora ! Button clicked !")
                    clickable.on_click()
                else:
                    print("Nope")


        # fltk.attend_fermeture()

main()