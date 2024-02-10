"""
Add this file to beidge between the http server and the actual data. Tis will allow to use either SQL, Google Sheets, or plain files without changing the code.
"""
from classes.bracelet import Bracelet
from classes.buyables import Buyable
from classes.guest import Guest
import pathlib
import json
from datetime import date



guests: dict = {}

def is_adherant(guest: Guest) -> bool:
    pass


def get_guests() -> list[Guest]:
    guests_filepath = pathlib.Path("server/data/guests.json")
    guests: list[Guest] = []
    with open(guests_filepath, "r") as guests_file:
        guests_data: list[dict] = json.loads(guests_file.read())
        for guest_dict in guests_data:
            # guest_dict: dict
            guest = Guest(
                guest_id=guest_dict.get("guest_id", ""),
                first_name=guest_dict.get("first_name", ""),
                last_name=guest_dict.get("last_name", ""),
                birth=date.fromisoformat(guest_dict.get("birth", "")),
                balance=guest_dict.get("balance", ""),
            )
            guest.staff = guest_dict.get("staff", "")
            guest.organizer = guest_dict.get("organizer", "")
            guests.append(guest)
    return guests

def get_bracelet():
    pass