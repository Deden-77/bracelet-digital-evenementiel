from .widgets import *


######### PAGES ######### (should be in another file?)



class TestPage(Page):
    def __init__(self, show_topbar: bool) -> None:
        super().__init__(show_topbar)
        self.content = List(
            children=[
                MaterialButton(
                    width=400,
                    height=50,
                    label=Label(
                        text="Hello ! I'm a button with a label !"
                    ),
                    fill_color="#0096FF"
                )
            ],
            disposition=Disposition.VERTICAL
        )


class TestPage2(Page):
    def __init__(self, show_topbar: bool) -> None:
        super().__init__(show_topbar)
        self.topbar = TopBar(
            title=Label(
                text="Hello !",
                color="#FFFFFF"
            )
        )
        self.content = List(
            children=[
                MaterialButton(
                    size=Size(sizetype=SizeType.WRAP_CONTENT),
                    label=Label(
                        text="Hello ! I'm a button with a label !"
                    ),
                    fill_color="#0096FF"
                ),
                EmptySpace(
                    size=Size(sizetype=SizeType.FIXED, width=0, height=100),
                ),
                MaterialButton(
                    size=Size(sizetype=SizeType.WRAP_CONTENT),
                    label=Label(
                        text="Awasome !"
                    ),
                    fill_color="#FFFFFF"
                )
            ],
            disposition=Disposition.VERTICAL
        )
