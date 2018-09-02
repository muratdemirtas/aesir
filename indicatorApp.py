import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

class AppIndicatorExample:
    def __init__(self, indicator_id):
        self.ind = appindicator.Indicator.new(str(indicator_id),
                                              "indicator-messages",
                                              appindicator.IndicatorCategory.SYSTEM_SERVICES)

        self.ind.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.ind.set_attention_icon("indicator-messages-new")

        # create a menu
        self.menu = gtk.Menu()

        item = gtk.MenuItem(str(indicator_id))

        item2 = gtk.MenuItem("Options")

        item.show()
        item2.show()

        item2.connect("activate", self.clicked)

        self.menu.append(item)
        self.menu.append(item2)

        image = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        image.connect("activate", self.quit)
        image.show()
        self.menu.append(image)

        self.menu.show()

        self.ind.set_menu(self.menu)

    def quit(self, widget, data=None):
        gtk.main_quit()

    def clicked(self, widget):
        print ("Item selected")



