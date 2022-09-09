import shutil
import time
import datetime

while True:
    original = r"C:\whateverthesourcepathis"
    target = r"C:\whateverthetargetpathis"
    shutil.copyfile(original, target)

    time.sleep(600)  # in seconds
    print("Backed up at : ", end='')
    now = datetime.datetime.now()
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
