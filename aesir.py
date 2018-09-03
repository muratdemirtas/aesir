import os
import sys
import  parameters
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from indicatorApp import  AppIndicatorExample

#syslog üzerinde kayıt tutacak olan sınıfımızı çağırıyoruz
from syslogger import Syslogger

#syslog handlerimizi olusturuyoruz ki syslog üzerine kayıt yapabilelim.
#syslog kayıtları cat /var/log/syslog komutu ile görüntülenebilir.
sysloghandler = Syslogger()

sysloghandler.writesyslogFile("Program Arguments")

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

sysloghandler.writesyslogFile( str(sys.argv))





from gi.repository import Gdk

win = Gdk.get_default_root_window()
h = win.get_height()
w = win.get_width()

print ("The size of the window is %d x %d" % (w, h))

pb = Gdk.pixbuf_get_from_window(win, 0, 0, w, h)

if (pb != None):
    pb.savev("screenshot.png","png", (), ())
    print("Screenshot saved to screenshot.png.")
else:
    print("Unable to get the screenshot.")




clipboard = gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
clipboard.set_image(pb)
clipboard.store()






if __name__ == "__main__":
    indicator = AppIndicatorExample(1)

    gtk.main()