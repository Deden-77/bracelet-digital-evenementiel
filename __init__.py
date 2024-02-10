# https://patorjk.com/software/taag/#p=display&f=Thin&t=made%20by%20_Deden
# https://patorjk.com/software/taag/#p=display&f=Merlin1&t=%20Smart%0A%20%20%20%20%20%20%20%20Event%0ABracelets
import server.seb_web_server as seb_web_server

with open("assets/smart_event_bracelets.txt", "r") as file:
    print(file.read())
with open("assets/made_by_deden.txt", "r") as file:
    print(file.read())

print()
print()
print()
print("####################################################")
print("##                                                ##")
print("##              Quel mode utiliser ?              ##")
print("##                                                ##")
print("##       (1) Client (Bar/Vestiaire/Entrée)        ##")
print("##       (2) Serveur HTTP                         ##")
print("##       (3) Pacerelle LoRa                       ##")
print("##                                                ##")
print("####################################################")
print()
mode = None
# while not mode
mode = input("      --> ")

if mode == "1":
    import client.client
if mode == "2":
    seb_web_server.main()