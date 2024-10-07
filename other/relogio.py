import os
import threading
from datetime import datetime

def relogio():
    os.system('cls')
    
    now = datetime.now().strftime("%H:%M:%S")
    print(now)
    threading.Timer(1, relogio).start()

relogio()
