
import sys
import gi

gi.require_version('Gtk', '4.0')

from gi.repository import Gtk, GLib

from AppWindow import AppWindow

APP_ID = 'com.codingcrucible.cinematoscope'

class Application(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id=APP_ID)

    def do_activate(self):
        win = AppWindow(application=self)
        win.present()
