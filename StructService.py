from StructPacket import Service
from config import services
import random, time
from colorama import Fore

class Distribution_Service():
    def __init__(self):
        self.number_attack = Service()
        self.services = services

    def phone(self, phone):
        self.number_attack.number(phone)

    def random_service(self):
        try:
            self.service = random.choice(self.services)
            exec(f'self.number_attack.{self.service}()')
            print(Fore.GREEN + f'[+] Отправлено {self.service}')

        except Exception as ex:
            pass


 