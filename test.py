from sendSMS import *
from printProcess import show
import time
import datetime
if __name__ == '__main__':
    # send("hello twilio!")

    total = 333 #总数
    c = 0 #计数
    start = datetime.datetime.now()
    while c <= total:
        show(c,total,interval=datetime.datetime.now()-start,DoneInfo='Finished')
        c += 1
        time.sleep(0.1)