import random, string
from user_agent import generate_user_agent

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
    'Showy', 'Andrey', 'sasha', 'masha','petya', 'vasya', 'sonya', 'evgeniy', 'hykok', 'what', 'you', 'iewa', 'rooti'
    'good', 'Jask', 'Luka', 'Artem', 'Maga' 'fifi', 'fufu', 'lolik', 'tolik', 'petz', 'hsdf', 'pope', 'none', 'nou', 'urukbek',
    'James', 'Jony', 'Jacob', 'Cristi', 'Benjamin', 'Gregory', 'Caesar', 'Tony', 'Ara', 'Harry', 'Garry', 'Larry', 'Nixon', 'Kanny',
]

ru_name = [
    'степа', 'ксюша', 'Петр','Иван','Степан','Магомед','Мага', 'Люба', 'маша', 'паша', 'ваня', 'саша', 'женя', 'евгения', 'софия', 'котик', 'джони', 'ваня', 'урукбек', 'миша', 'котик', 
    'Арсений', 'Василий', 'Максим', 'Грегорий', 'Нурлан', 'Элвин', 'Артем', 'Анастасия', 'Женя', 'Катя', 'Карина', 'Аня',
]

agent = [generate_user_agent(device_type="desktop", os=("linux")), generate_user_agent(device_type="desktop", os=("mac"))]


def name():
    return random.choice(names)

def _ru_name_():
    return random.choice(ru_name)

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



