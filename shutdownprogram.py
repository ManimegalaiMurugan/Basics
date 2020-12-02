import os
shutdown = input("type yes to shutdown pc else no " )
if shutdown == 'yes':
    os.system("shutdown /s /t 1")
else :
    exit()
