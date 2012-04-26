import logging
import dbus
 
# InspiredBy: http://bluesock.org/~willg/blog/dev/gnome_media_keys.html
class MediaKeyHandler(object):
    def __init__(self, app, name):
        self.app = app
        self.name = name
        self.bus = dbus.Bus(dbus.Bus.TYPE_SESSION)
        self.bus_object = self.bus.get_object(
            'org.gnome.SettingsDaemon', '/org/gnome/SettingsDaemon/MediaKeys')
 
        self.bus_object.GrabMediaPlayerKeys(
            self.name, 0, dbus_interface='org.gnome.SettingsDaemon.MediaKeys')
 
        self.bus_object.connect_to_signal(
            'MediaPlayerKeyPressed', self.handle_mediakey)
 
        #window.connect("focus-in-event", self.on_window_focus)
 
    def handle_mediakey(self, application, *mmkeys):
#if application != self.app:
#            return
        print "Got key"
        for key in mmkeys:
            if key == "Play":
                self.app.on_play_clicked()
            elif key == "Stop":
                self.app.on_stop_clicked()
            elif key == "Next":
                self.app.on_forward_clicked()
            elif key == "Previous":
                self.app.on_previous_clicked()
 
    def on_window_focus(self, window):
        self.bus_object.GrabMediaPlayerKeys(
            self.app, 0, dbus_interface='org.gnome.SettingsDaemon.MediaKeys')
        return False
 
def get_media_key_handler(window):
    """
    Creates and returns a MediaKeyHandler or returns None if such a thing
    is not available on this platform.
 
    :param window: a Gtk.Window instance
    """
    try:
        return MediaKeyHandler(window)
    except dbus.DBusException:
        logging.exception("cannot load MediaKeyHandler")
