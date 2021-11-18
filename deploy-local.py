import os
import time

print('deploy local da aplicação')
time.sleep(1.5)
os.system('docker-compose up --build -d')