import datetime

'''fichier permettant l'horodatage des matchs et tournois'''
def timestamp ():
    now = datetime.datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print(date_time)

timestamp()