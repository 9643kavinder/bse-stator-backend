from __future__ import absolute_import, unicode_literals

import os
import json
from django.conf import settings
import redis
from celery import Celery
from zipfile import ZipFile
from io import BytesIO
from urllib.request import Request, urlopen
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
app = Celery('backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.enable_utc = False
app.autodiscover_tasks()


@app.task(bind=True)
def wake_up(self):
    redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                       port=settings.REDIS_PORT,
                                       password=settings.REDIS_PASSWORD,
                                       db=0)
    today = str(date.today())
    todays_date = list(today.split('-'))
    todays_date.reverse()
    dt = ""
    for x in todays_date:
        dt += x[-2:]
    req = Request(f'https://www.bseindia.com/download/BhavCopy/Equity/EQ{dt}_CSV.zip', headers={'User-Agent': 'Mozilla/5.0'})
    with ZipFile(BytesIO(urlopen(req).read())) as my_zip_file:
        for contained_file in my_zip_file.namelist():
            for line in my_zip_file.open(contained_file).readlines():
                output = line.decode()
                lst_info = output.split(',')
                dct = {
                    "code": lst_info[0],
                    "name": lst_info[1],
                    "open": lst_info[4],
                    "high": lst_info[5],
                    "low": lst_info[6],
                    "close": lst_info[7]
                }
                json_dct = json.dumps(dct)
                redis_instance.set(lst_info[1], json_dct)










# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))

# @app.task(bind=True)
# def send_import_summary(self):
#     print("Hello world")