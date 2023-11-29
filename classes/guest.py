import datetime
import enum


class Sex(enum.Enum):
    HOMME = "homme"
    FEMME = "femme"
    AUTRE = "autre" # Non binaire / Autre


class Guest():
    def __init__(self, first_name: str, last_name: str, birth: datetime.date, sex: Sex, balance: int, adherant_bde: bool) -> None:
        self.id: str
        self.first_name = first_name
        self.last_name = last_name
        self.birth = birth
        self.sex = sex

        self.balance = balance # As centimes, 
        self.adherant_bde = adherant_bde
        # self.alchool_level: float # g/100ml (average human have 5L of blood)n TODO : Rename this.
    
    def is_adult(self):
        # TODO
        today = datetime.datetime.today()
        if self.birth.year+18 < today.year:
            return True
        elif self.birth.year+18 == today.year: # Same year, should check the month
            if self.birth.month < today.month:
                return True
            elif self.birth.month == today.month: # Same month, check day
                if self.birth.day <= today.day:
                    return True
        return False


# user = Guest(
#     first_name="Aodren",
#     last_name="Commun",
#     birth=datetime.date(
#         year=2005,
#         month=5,
#         day=8
#     )
# )


# print(user.is_adult())
