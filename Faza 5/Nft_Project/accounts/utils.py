# Natalija
# Provera podataka za registarciju
from accounts.models import Korisnik
import re

from profiles.models import Registrovanikorisnik


def  check_data_for_registration(username, birthdate, birthplace, name,surname, phone_number, password, confirm_password, email, card):
    message= ""

    username = username.strip()
    birthdate = birthdate.strip()
    birthplace = birthplace.strip()
    name = name.strip()
    surname = surname.strip()
    phone_number = phone_number.strip()
    password = password.strip()
    confirm_password = confirm_password.strip()
    email = email.strip()
    card = card.strip()
    if exists_username(username):
        message+="Korisničko ime "+username+" već postoji!\n"
    else:
        if not valid_username_format(username):
            message += "Korisničko ime nije validnog formata!\n"
    if not valid_birthdate(birthdate):
        message += "Datum rođenja nije validan!\n"
    if not valid_birthplace(birthplace):
        message += "Mesto rođenja nije validno!\n"
    if not valid_name(name):
        message+="Ime nije validno!\n"
    if not valid_surname(surname):
        message+="Prezime nije validno!\n"
    if not valid_phone_number(phone_number):
        message+="Broj telefona nije u validnom formatu!\n"
    if not valid_password(password):
        message+="Šifra ne zadovoljava kriterijume!\n"
    else:
        if password != confirm_password:
            message+="Potvrda šifre i šifra se ne poklapaju!\n"
    if exists_email(email):
        message+="Mejl adresa "+email+" već postoji!\n"
    else:
        if not valid_email(email):
            message+="Mejl adresa nije u dobrom formatu!\n"
    if not valid_card_number(card):
        message+="Broj kartice nije u dobrom formatu (16 cifara)!\n"

    return message



# Provera da l username postoji u tabeli korisnik i tabeli poslatih zahetava za registraciju
def exists_username(username):
    return Korisnik.objects.filter(username=username).exists()

def exists_email(email):
    return Registrovanikorisnik.objects.filter(email=email).exists()


# Provera username formata
def valid_username_format(username):
    return re.match(r'^[a-zA-Z0-9]+$', username) is not None


def valid_birthdate(birthdate):
    from datetime import datetime, timedelta
    today = datetime.today()
    try:
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
        age = (today - birthdate) // timedelta(days=365.2425)
        return age >= 14
    except ValueError:
        return False


# mozda moze da se zameni sa nekom select formom koja sadrzi sva mesta u svetu npr. samo zemlje
def valid_birthplace(birthplace):
    return birthplace and birthplace[0].isupper()

def valid_name(name):
    return name and name[0].isupper() and name.isalpha()


def valid_surname(surname):
    return surname and surname[0].isupper() and surname.isalpha()


def valid_phone_number(phone_number):
    return len(phone_number) > 5 and phone_number.isdigit()


def valid_password(password):

    return len(password) >= 6 and not any(char.isspace() for char in password)

def valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None


def valid_card_number(card):
    return len(card) <= 16 and card.isdigit()
