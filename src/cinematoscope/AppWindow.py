import gi

gi.require_version('Gtk', '4.0')

from gi.repository import Gtk

@Gtk.Template(filename="/home/aurix/cinematoscope/src/cinematoscope/ui/cinematoscope.xml")
class AppWindow(Gtk.ApplicationWindow):
    __gtype_name__ = "AppWindow"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

