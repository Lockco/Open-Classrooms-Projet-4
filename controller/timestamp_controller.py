import datetime

"""fichier permettant l'horodatage des matchs et tournois"""


def timestamp():
    now = datetime.datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    return date_time


timestamp()
