import os

#syslog üzerinde kayıt tutacak olan sınıfımızı çağırıyoruz
from syslogger import Syslogger

#syslog handlerimizi olusturuyoruz ki syslog üzerine kayıt yapabilelim.
#syslog kayıtları cat /var/log/syslog komutu ile görüntülenebilir.
sysloghandler = Syslogger()

sysloghandler.writesyslogFile("Program Arguments")


sysloghandler.writesyslogFile("Program Ended.")











