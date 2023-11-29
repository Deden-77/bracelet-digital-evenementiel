from .guest import Guest

class Bracelet():
    def __init__(self) -> None:
        self.id: str # 6 Letters, see id_generator.py
        self.belongs_to_guest_id: Guest.id