import cairo
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk
from gi.repository import Gtk as gtk
from os.path import abspath, dirname, join
from math import pi
import sys
import os
import cairo
from Xlib import X, display ,Xutil



def on_key_release( widget, ev, data=None):
    if ev.keyval == Gdk.KEY_Escape: #If Escape pressed, reset text
        exit(2)

win = gtk.Window()

header = gtk.HeaderBar( )

header.props.show_close_button = False

win.set_titlebar(header)

win2 = Gdk.get_default_root_window()
h = win2.get_height()
w = win2.get_width()




print ("The size of the window is %d x %d" % (w, h))

pb = Gdk.pixbuf_get_from_window(win2, 0, 0, w, h)


image = gtk.Image()
image.set_from_pixbuf(pb)


win.add(image)
#button.show()


if (pb != None):
    pb.savev("screenshot.png","png", (), ())
    print("Screenshot saved to screenshot.png.")
else:
    print("Unable to get the screenshot.")


win.connect("destroy", gtk.main_quit)
win.fullscreen()
win.connect("key-release-event",  on_key_release)
win.show_all()


win = Gdk.get_default_root_window()
h = win.get_height()
w = win.get_width()




gtk.main()
