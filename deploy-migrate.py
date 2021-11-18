import os
import time

print('deploy de migrates')
time.sleep(1.5)

os.system('docker-compose run web python manage.py makemigrations')
os.system('docker-compose run web python manage.py migrate')
os.system('docker-compose run web python manage.py migrate --run-syncdb')