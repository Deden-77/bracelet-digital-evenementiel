from classes.guest import Guest
from utilities.name_normalizer import normalize_name

def query_matches_guest(query, guest: Guest):
    if normalize_name(guest.display_name()) == query:
        return 1
    