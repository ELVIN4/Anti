import random, string

mails = (
    "mail.ru",
    "inbox.ru",
    "list.ru",
    "bk.ru",
    "ya.ru",
    "yandex.com",
    "yandex.ua",
    "yandex.ru",
    "gmail.com",
    "outlook.com",
    "mail.yahoo.com",
    "mail.rambler.ru",
)

names = [
    'Showy', 'Andrey', 'Sasha', 'Masha','Petya', 'Vasya', 'Sonya', 'Evgeniy', 'Hykok', 'What', 'Youn', 'Iewa', 'Rooti'
    'Good', 'Jask', 'Luka', 'Artem', 'Maga' 'Fifi', 'Fufu', 'Lolik', 'Tolik', 'Petz', 'Hsdf', 'Pope', 'None', 'Noud', 'Urukbek',
    'James', 'Jony', 'Jacob', 'Cristi', 'Benjamin', 'Gregory', 'Caesar', 'Tony', 'Ara', 'Harry', 'Garry', 'Larry', 'Nixon', 'Kanny',
]

ru_name = [
    'Степа', 'Ксюша', 'Петр','Иван','Степан','Магомед','Мага', 'Люба', 'Маша', 'Паша', 'Ваня', 'Саша', 'Женя', 'Евгения', 'София', 
    'Арсений', 'Василий', 'Максим', 'Грегорий', 'Нурлан', 'Артем', 'Анастасия', 'Женя', 'Катя', 'Карина', 'Аня',
]

agent = open('user_agents.txt').read().split('\n')


def name():
    return random.choice(names)


def username():
    data_user = ''
    letters = 'wertyuiopbvcsdfghjklkjewfvgbnxcfghuiasdfgh'
    for new_user in letters[:8]:
        data_user+=data_user.join(random.choice(list(letters)))

    return name() + data_user

def x(int_range=4):
    numbers = []
    for _ in range(int_range):
        numbers.append(str(random.randint(1, 9)))
    return "".join(numbers)

def email():
    return name() + x() + "@" + random.choice(mails)

def password():
    return name() + x(int_range=9)

def user_agent():
    return random.choice(agent)



