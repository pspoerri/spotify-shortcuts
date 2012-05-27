#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dbus
import dbus.service
import dbus.glib
import gobject

import media_key_handler

class Spotify:
    def __init__(self):
        self.dbus = dbus.SessionBus()
        self.spotify = self.dbus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')        
        self.register()
        print "Registered with spotify"

    def register(self):
        self.dbusregistration = media_key_handler.MediaKeyHandler(self, "SpotifyShortCutHandler")

    def on_play_pressed(self):
        self.spotify.PlayPause()

    def on_stop_pressed(self):
        self.spotify.Stop()

    def on_forward_pressed(self):
        self.spotify.Next()

    def on_previous_pressed(self):
        self.spotify.Previous()
    
    

def main():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    mainloop = gobject.MainLoop()
    app = Spotify()
    mainloop.run()

if __name__ == "__main__":
    main()
