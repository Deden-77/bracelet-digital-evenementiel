from fltk.fltk import fltk
import enum


class Disposition(enum.Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"

class Anchor(enum.Enum):
    TOP_RIGHT = "ne"
    TOP_LEFT = "nw" # Default for rectangles
    BOTTOM_RIGHT = "se"
    BOTTOM_LEFT="sw"
    CENTER = "center"
    TOP = "n"
    BOTTOM = "s"
    RIGHT = "e"
    LEFT = "w"



class Intent():
    def __init__(self) -> None:
        pass


class DoNothingIntent(Intent):
    pass

class GotoPageIntent(Intent):
    def __init__(self, page_id) -> None:
        super().__init__()
        self.page_id = page_id


class SizeType(enum.Enum):
    MATCH_PARENT = "match_parent"
    WRAP_CONTENT = "wrap_content"
    FIXED = "fixed"


class Size():
    def __init__(self, sizetype: SizeType, width: int = None, height: int = None) -> None:
        self.sizetype = sizetype
        self.width = width
        self.height = height
        


class Widget():
    def __init__(self) -> None:
        self.size: Size
        self.clickable: int = False

    def draw(self, x: int, y: int, anchor: Anchor = Anchor.TOP_LEFT):
        return
    
    def get_clickable_childs(self) -> list: # Return type is actually list[Widget]
        return []

    def is_clicked(self, x: int, y: int) -> bool:
        """
        Tells wether or not the x and y coordinates corresponds to the location of the widget on screen
        """
        return False
    
    def on_click(self):
        pass


class Label(Widget):
    def __init__(self, text: str, color: str = "black") -> None:
        super().__init__()
        self.text = text
        self.color = color

    def draw(self, x: int, y: int, anchor: Anchor = Anchor.TOP_LEFT):
        fltk.texte(
            x=x,
            y=y,
            chaine=self.text,
            couleur=self.color,
            ancrage=anchor.value
        )

    @property
    def size(self):
        size_fltk: tuple = fltk.taille_texte(chaine=self.text)
        s = Size(sizetype=SizeType.FIXED, width=size_fltk[0], height=size_fltk[1])
        return s


class EmptySpace(Widget):
    def __init__(self, size: Size) -> None:
        super().__init__()
        self.size = size

    def draw(self, x: int, y: int, anchor: Anchor = Anchor.TOP_LEFT):
        return # We draw nothing as we are empty space



class Margin(Widget): # Use emptySpace and Lists ?
    def __init__(self, child: Widget, top: int, bottom: int, right: int, left: int) -> None:
        super().__init__()
        self.child = child
    
    def draw(self, x: int, y: int, anchor: Anchor = Anchor.TOP_LEFT):
        pass

class MaterialButton(Widget):
    def __init__(self, size: Size, label: Label, fill_color: str = "", outline_thickness: int = 0, outline_color: str = "") -> None:
        super().__init__()
        self.clickable = True
        self.size = size
        self.label = label
        if self.size.sizetype == SizeType.WRAP_CONTENT:
            self.size.width = self.label.size.width
            self.size.height = self.label.size.height
        self.fill_color = fill_color
        self.outline_thickness = outline_thickness
        self.outline_color = outline_color
        self.x: int
        self.y: int

    def draw(self, x: int, y: int, anchor: Anchor = Anchor.TOP_LEFT):
        assert anchor == Anchor.TOP_LEFT
        self.x = x
        self.y = y
        fltk.rectangle(x, y, x+self.size.width, y+self.size.height, remplissage=self.fill_color)
        self.label.draw(x=x+self.size.width/2, y=y+self.size.height/2, anchor=Anchor.CENTER)

    def on_click(self):
        self.fill_color = "#FF0000"

    def is_clicked(self, x: int, y: int) -> bool:
        return (self.x < x < self.x+self.size.width) and (self.y < y < self.y+self.size.height)
    
    def get_clickable_childs(self):
        return [self]


class List(Widget):
    def __init__(self, children: list[Widget], disposition: Disposition) -> None:
        super().__init__()
        self.children = children
        self.disposition = disposition
    
    def draw(self, x: int, y: int, anchor: Anchor = Anchor.TOP_LEFT):
        if self.disposition == Disposition.VERTICAL:
            i_y = 0
            for child in self.children:
                child.draw(x=x, y=y+i_y)
                i_y += child.size.height
        elif self.disposition == Disposition.HORIZONTAL:
            i_x = 0
            for child in self.children:
                child.draw(x=x+i_x, y=y)
                i_x += child.size.height
        else:
            raise Exception("Unknown disposition. Should be Disposition.VERTICAL or Disposition.HORIZONTAL.")
    
    def get_clickable_childs(self):
        a = []
        for child in self.children:
            a += child.get_clickable_childs()
        return a


class TopBar(Widget):
    def __init__(self, title: Label, height_percent: float = 0.1) -> None:
        super().__init__()
        self.height_percent = height_percent
        self.title = title

    @property
    def size(self):
        s = Size(
            sizetype=SizeType.FIXED,
            width=fltk.hauteur_fenetre()*self.height_percent,
            height=fltk.largeur_fenetre()
        )
        return s

    def draw(self):
        fltk.rectangle(0, 0, fltk.largeur_fenetre(), self.size.height, remplissage="#000000")
        self.title.draw(0, 0) # TODO


# Design with classes in tkinter https://www.youtube.com/watch?v=eaxPK9VIkFM


class Page():
    def __init__(self, show_topbar: bool) -> None:
        self.show_topbar = show_topbar
        self.topbar: TopBar
        self.content: Widget
    
    def draw(self):
        self.topbar.draw()
        self.content.draw(x=0, y=self.topbar.size.height, anchor=Anchor.TOP_LEFT)
    
    def get_clickable_childs(self) -> list[Widget]:
        return self.content.get_clickable_childs() + self.topbar.get_clickable_childs()


