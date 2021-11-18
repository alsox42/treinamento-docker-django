import os
import time

print('deploy de admin')
time.sleep(1.5)
os.system('docker-compose run web python manage.py createsuperuser')
