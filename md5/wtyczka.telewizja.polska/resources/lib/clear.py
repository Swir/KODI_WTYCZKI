# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
 
import sys,xbmc,xbmcaddon,sqlite3
import re,os,xbmcplugin,xbmcgui

try: os.remove(xbmc.translatePath("special://thumbnails/"))
except: pass
try: os.remove(xbmc.translatePath("special://database/Textures13.db"))
except: pass

conn = sqlite3.connect(xbmc.translatePath("special://database/Textures13.db"))
try:
    with conn:
        list = conn.execute("SELECT id, cachedurl FROM texture WHERE url LIKE '%%%s%%';" % ".highwebmedia.com")
        for row in list:
            conn.execute("DELETE FROM sizes WHERE idtexture LIKE '%s';" % row[0])
            try: os.remove(xbmc.translatePath("special://thumbnails/" + row[1]))
            except: pass
        conn.execute("DELETE FROM texture WHERE url LIKE '%%%s%%';" % ".githubusercontent.com")
except:
    pass
    
    
xbmcgui.Dialog().ok("Czyszczenie", 'Wykonano próbę wyczyszczenia starych ikon','','Sprawdź czy ikony wyświetlane są prawidłowo[CR]Ewentualnie uruchom program ponownie')
