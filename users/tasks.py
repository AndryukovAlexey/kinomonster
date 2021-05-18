from kinomonster.celery import app
from users.models import Premka
import datetime

@app.task
def check_prem():
    if Premka.objects.filter(date_end=datetime.datetime.today().date()):     
        Premka.objects.filter(date_end=datetime.datetime.today().date()).delete()