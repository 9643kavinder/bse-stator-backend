# bse-stator-backend

Live URL : https://bseapp.osc-fr1.scalingo.io/api/ + {{ company-name }}
###Example : https://bseapp.osc-fr1.scalingo.io/api/tata

## Description
• This app extacts the zip file from bse website, parse and store the data.</br>
• With the help of celery, task of extacting is scheduled at sharp 6pm(IST) everyday.</br>
• Information of each company on bse can be visible for the current day.</br>

## Procedure
### Simple Clone This Repo

```bash
$git clone https://github.com/9643kavinder/bse-stator-backend.git
cd bse-stator-backend
pip install -r requirements.txt
python manage.py runserver
```

## Technologies Used
* Backend
  * Django/Python
  * Redis
  * Celery
