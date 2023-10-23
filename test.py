import winsound
from datetime import datetime, timedelta
import time
import playsound

prev = datetime.now()
# while timedelta(seconds=1) >= datetime.now() - prev:
winsound.Beep(440, 100)

time.sleep(1)
playsound.playsound('wake_up.mp3')