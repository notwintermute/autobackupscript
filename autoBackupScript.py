from shutil import copytree
from time import sleep
from datetime import date, datetime
from pytz import timezone

while True:
    current = date.today()
    year = str(current.year)
    month = str(current.month)
    day = str(current.day)
    timezone = timezone("US/Central")  # use whatever timezone you have
    naive = datetime.now()

    folderName = day + "-" + month + "-" + year + "-" + naive.strftime("%H.%M.%S")
    filePath = "back up\\" + folderName
    original = "whatever\\the\\source\\path\\is"
    target = "whatever\\the\\destination\\path\\is" + filePath

    copytree(original, target)
    print("Backed up at : ", end='')
    now = datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    sleep(600)  # in seconds
