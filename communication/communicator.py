"""
Ce fichier contient la class nécessaire à la communication entre les différents appareils.
La communication se fait par le biais d'internet (Wifi/4G) ou via LoRa ou LoRaWAN.
"""

import enum



class ConnexionType(enum.Enum):
    WIFI = "WIFI"
    LORA = "LORA"

wifi_server_adress: str = "the-seb-project-server-foyer-bde-tunnels.aodren.co" # URL vers le serveur (Rpi) situé au BDE. Il contient les 

class Communicator():
    def __init__(self, connexion_type: ConnexionType) -> None:
        self.connexion_type = connexion_type
    
    def get_user(self, USER_ID_OU_AUTRE):
        if self.connexion_type == ConnexionType.WIFI:
            pass