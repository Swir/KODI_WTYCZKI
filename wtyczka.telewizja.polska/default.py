# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
import sys,xbmc,xbmcaddon
import resources.lib.requests as requests
import re,os,xbmcplugin,xbmcgui
import urllib,urllib2
import urllib2,urlparse,json
mode = sys.argv[2]

addon = xbmcaddon.Addon('wtyczka.telewizja.polska')

addonVER = addon.getAddonInfo('version').decode('utf-8')
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
scriptID = addonID = addon.getAddonInfo('id').decode('utf-8')
addonDir = addon.getAddonInfo('path').decode('utf-8')
sys.path.append( xbmc.translatePath(addonDir))
sys.path.append( os.path.join(addonDir, "resources" ))
sys.path.append( os.path.join(addonDir, "resources/lib" ))
icon = xbmc.translatePath( os.path.join( addonDir, 'icon.png' ) ).decode('utf-8')
fanart = xbmc.translatePath( os.path.join( addonDir, 'fanart.jpg' ) ).decode('utf-8')
dodatki = 'https://raw.githubusercontent.com/neopack1/kodi/master/dodatki/'
tv = 'https://raw.githubusercontent.com/neopack1/kodi/master/dodatki/logo_tv/'
radio = 'https://raw.githubusercontent.com/neopack1/kodi/master/dodatki/logo_radio/'
images = imagesDir = 'https://raw.githubusercontent.com/neopack1/kodi/master/dodatki/images/'
fanartDir='https://raw.githubusercontent.com/neopack1/kodi/master/dodatki/fanarts/'
play = defaultImage = tv+'play.png'
UHD="[COLOR white] 4K UHD [/COLOR]"
FHD="[COLOR white] FULL HD [/COLOR]"
HD= "[COLOR white] HD [/COLOR]"
SD= "    "
LD= "[COLOR white] LQ [/COLOR]"
WIDOK_SET = addon.getSetting('widok')
WIDOK_SET_MAIN = addon.getSetting('widokMain')
ICON_SET = addon.getSetting('ikonki')
XXX_SET = addon.getSetting('xxx')
GRUPOWANIE = addon.getSetting('grupowanie')
KOLOROWANIE = addon.getSetting('kolorowanie')
GRUPA_HD = addon.getSetting('grupaHD')
if GRUPOWANIE=="false":
    addon.setSetting('kolorowanie',"false")
ext=" "

#xbmcgui.Dialog().ok("TEST", addonVER)
#xbmc.executebuiltin('Notification("TELE-WIZJA POLSKA","Pobieranie danych...",1500,'+icon+')')
#############################################################################
if ICON_SET == "1":
    tv = 'https://raw.githubusercontent.com/neopack1/kodi/master/dodatki/logo_tv_L/'
if ICON_SET == "2":
    tv = 'https://raw.githubusercontent.com/neopack1/kodi/master/dodatki/logo_tv_M/'
if ICON_SET == "3":
    tv = 'https://raw.githubusercontent.com/neopack1/kodi/master/dodatki/logo_tv_S/'
#############################################################################
###### sprawdzanie wersji

url="https://raw.githubusercontent.com/neopack1/kodi/master/files/wersja.json"
headers = post = {}
data = urllib.urlencode(post)
reqUrl = urllib2.Request(url, data, headers)
red_json = urllib2.urlopen(reqUrl)
obj_data = json.load(red_json)
for s in range(len(obj_data)):
    najnowsza_wersja = obj_data[s]['WERSJA']
    data_publikacji = obj_data[s]['DATA']
if najnowsza_wersja != addonVER:
    xbmc.executebuiltin('UpdateAddonRepos')
    info1 = 'Obecna wersja to: [COLOR navajowhite]v'+str(addonVER)+'[/COLOR] Wydano nowszą wersję: [COLOR navajowhite]v'+str(najnowsza_wersja)+'[/COLOR]'
    info2 = 'Uruchomiłem polecenie wymuszenia aktualizacji wtyczek'
    info3 = 'Przejdź do opcji Kodi i pobierz najnowsze aktualizacje'
    xbmcgui.Dialog().ok("[COLOR red][B]WTYCZKA JEST PRZEDAWNIONA[/B][/COLOR]",info1,info2,info3)
    xbmc.sleep(2000)
    xbmc.executebuiltin('UpdateLocalAddons')
    xbmc.sleep(2000)
    xbmc.executebuiltin('UpdateAddonRepos')
"""
###### wczytanie kolorów grup kanałów

    kolor10 = "[COLOR "+addon.getSetting('kol10')"]"
    kolor15 = "[COLOR "+addon.getSetting('kol15')"]"
    kolor20 = "[COLOR "+addon.getSetting('kol20')"]"
    kolor25 = "[COLOR "+addon.getSetting('kol25')"]"
    kolor30 = "[COLOR "+addon.getSetting('kol30')"]"
    kolor35 = "[COLOR "+addon.getSetting('kol35')"]"
    kolor40 = "[COLOR "+addon.getSetting('kol40')"]"
    kolor45 = "[COLOR "+addon.getSetting('kol45')"]"
    kolor50 = "[COLOR "+addon.getSetting('kol50')"]"
    kolor55 = "[COLOR "+addon.getSetting('kol55')"]"
    kolor99 = "[COLOR "+addon.getSetting('kol99')"]"
    kolorEnd= "[/COLOR]"
"""
kolor10 = "[COLOR peachpuff]"
kolor15 = "[COLOR crimson]"
kolor20 = "[COLOR darkturquoise]"
kolor25 = "[COLOR springgreen]"
kolor30 = "[COLOR darkorange]"
kolor35 = "[COLOR linen]"
kolor40 = "[COLOR orchid]"
kolor45 = "[COLOR deeppink]"
kolor50 = "[COLOR yellowgreen]"
kolor55 = "[COLOR blanchedalmond]"
kolor99 = "[COLOR red]"
kolorEnd= "[/COLOR]"

def widokFilmowy(tak_lub_nie):
    if tak_lub_nie == 'tak':
        xbmcplugin.setContent(int(sys.argv[1]), 'movies')
    if tak_lub_nie != 'tak':
        xbmcplugin.setContent(int(sys.argv[1]), 'files')
widokFilmowy('tak')


def main():
    if 'main' in mode: 
        widokFilmowy('nie')
        xbmc.sleep(50)
        xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET_MAIN+')') # Zmiana widoku Menu głównego
    xbmc.sleep(300)
    if 'xcat1' in mode: tvp()
    elif 'eska' in mode: eska()
    elif 'xcat3' in mode: looknij()
    elif 'telewizja' in mode: telewizja()
    elif 'xcat5' in mode: filmboxlive()
    elif 'xcat6' in mode: lokalna()
    elif 'xcat7' in mode: itivi()
    elif 'yt' in mode: yt()
    elif 'zagraniczna' in mode: zagraniczna()
    elif 'testy' in mode: testy()
    elif 'opcje' in mode: opcje()
    elif 'testy' in mode: testy()
    elif 'xxx' in mode: xxx()
    elif 'menuPPV' in mode: menuPPV()
    elif 'menu1' in mode: menu1() # Kanały MIX
    elif 'menu2' in mode: menu2() # Kanały HD
    elif 'menu3' in mode: menu3()
    elif 'menu4' in mode: menu4()
    elif 'menu5' in mode: menu5()
    elif 'menu6' in mode: menu6()
    elif 'menu7' in mode: menu7()
    elif 'menu8' in mode: menu8()
    elif 'menu9' in mode: menu9()
    elif 'menu10' in mode: menu10()
    else:
        
 #       addDir('TESTY', 'plugin://wtyczka.telewizja.polska/?testy', icon)
        nazwaTv="[B]TELEWIZJA[/B]"
        if GRUPA_HD=="true":
            nazwaTv="[B]WSZYSTKIE  KANAŁY[/B]"
        addDir(nazwaTv, 'plugin://wtyczka.telewizja.polska/?menu1', images+'dir_tv.png')
        if GRUPA_HD=="true":
            addDir('[B]TYLKO KANAŁY HD[/B]', 'plugin://wtyczka.telewizja.polska/?menu2', images+'dir_tv_hd.png' )
        
        url='https://raw.githubusercontent.com/neopack1/kodi/master/files/lista-menu.json'
        headers = post = {}
        post = {}
        data = urllib.urlencode(post)
        reqUrl = urllib2.Request(url, data, headers)
        xbmc.sleep(250)
        red_json = urllib2.urlopen(reqUrl)
        obj_data = json.load(red_json)
        for s in range(len(obj_data)):
            url_dir= obj_data[s]['URL']
            nazwa_dir=obj_data[s]['NAZWA']
            logo_dir=obj_data[s]['LOGO']
            widoczny=obj_data[s]['WIDOCZNY']
            if widoczny=="tak":
                addDir("[B]"+nazwa_dir+"[/B]",url_dir,imagesDir+logo_dir)
        addDir('[B]ESKA GO[/B]', 'plugin://wtyczka.telewizja.polska/?eska', images+'dir_eskago.png')
        addDir('[B]TVP STREAM[/B]', 'plugin://wtyczka.telewizja.polska/?xcat1x', images+'dir_tvpstream.png')
        addDir('[B]TVN PLAYER[/B]', 'plugin://script.module.tvnplayer/', images+'dir_tvnplayer.png')
        addDir('[B]YOU TUBE[/B]', 'plugin://wtyczka.telewizja.polska/?yt', images+'dir_youtube.png')
        addDir('[B]TELEWIZJA ZE ŚWIATA[/B]', 'plugin://wtyczka.telewizja.polska/?zagraniczna', images+'dir_int.png')
        if XXX_SET == 'true':
            addDir('[B]EROTYKA (18+)[/B]', 'plugin://wtyczka.telewizja.polska/?xxx', images+'dir_xxx2.png')
        addDir('[B][COLOR darkgrey]USTAWIENIA[/COLOR][/B]', 'plugin://wtyczka.telewizja.polska/?opcje', images+'settings.png')

        widokFilmowy('nie')
        xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET_MAIN+')') # Zmiana widoku Menu głównego
        xbmc.sleep( 150 )
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
        xbmc.sleep( 400 )
        sys.exit(0)


def testy():

    addLink("AAAA",'http://inea.live.e238-po.insyscd.net/axnhd.smil/chunklist_b2400000.m3u8',icon)
    addLink("BBBB",'http://inea.live.e238-po.insyscd.net/axnspinhd.smil/chunklist_2400000.m3u8',icon)
    addLink("CCCC",'http://inea.live.e238-po.insyscd.net/stopklatkahd.smil/chunklist_2400000.m3u8',icon)
    
    widokFilmowy('nie')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)

#####################################################################################################
if 'extrafanart' in sys.argv[2]: sys.exit(0)
if 'runstream' in sys.argv[2]:
    url = sys.argv[2].replace('?runstream=','')
    px = xbmc.translatePath( os.path.join( addonDir,"resources/lib/zapping.py") )
    xbmc.executebuiltin('RunScript('+px+',url='+url+')')
    sys.exit(0)
########################################################################
def xxx():
    addJson("https://raw.githubusercontent.com/neopack1/kodi/master/json/xxx.json")

    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)
#####################################################################################################
def addLink(name,url,iconImage):
        ok=True
        if 'looknij.tv' in url: url = 'plugin://wtyczka.telewizja.polska/?runstream=' + url + '***' + name + '***' + iconImage	
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconImage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

def addDir(name,url,iconImage):
    liz=xbmcgui.ListItem(name, iconImage="DefaultDir.png", thumbnailImage=iconImage)
    liz.setProperty( "Fanart_Image", fanart )
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

def get_url():

    basicurl = 'http://tvpstream.tvp.pl/'
    plurl = requests.get(basicurl)
    pattern = '<div class="button.*?data-video_id="([^"]+)" title="([^"]+)">.*?<img src="([^"]+)".*?</div>'
    rResult = parse(plurl.text, pattern)
    return rResult[1]

def find_between(s,first,last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def parse(sHtmlContent, sPattern, iMinFoundValue = 1, ignoreCase = False):
        if ignoreCase:
            aMatches = re.compile(sPattern, re.DOTALL|re.I).findall(sHtmlContent)
        else:
            aMatches = re.compile(sPattern, re.DOTALL).findall(sHtmlContent)
        if (len(aMatches) >= iMinFoundValue):                
            return True, aMatches
        return False, aMatches

def addJson(url):
    headers = post = {}
    post = {}
    data = urllib.urlencode(post)
    reqUrl = urllib2.Request(url, data, headers)
    red_json = urllib2.urlopen(reqUrl)
    obj_data = json.load(red_json)
    lp=0
    ext=" "
    for s in range(len(obj_data)):
        lp=lp+1
        lpt=str(lp)
        if lp < 10:
            lpt="0"+str(lp)
        url = obj_data[s]['URL']
        thumb=obj_data[s]['LOGO']
        nazwa=obj_data[s]['NAZWA']
        jakosc=obj_data[s]['JAKOSC']
        if jakosc == "ld" or jakosc == "lq":
            ext=LD
        if jakosc == "hd":
            ext=HD
        if jakosc == "fhd":
            ext=FHD
        if jakosc == "uhd" or jakosc == "4k":
            ext=UHD
        if jakosc == "sd" or jakosc == "":
            ext=SD
        nazwa1="[B][COLOR white]"+lpt+"[/COLOR][/B] "+nazwa+ext
        addLink(nazwa1,url,tv+thumb)
#     li = xbmcgui.ListItem(nazwa, thumbnailImage=tv+thumb, iconImage=tv+thumb
#     xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li)
#####################################################################################################



#####################################################################################################
def opcje():
    addon.openSettings(sys.argv[1])
    sys.exit(0)
#####################################################################################################
"""def vod():
    xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET+')') # Zmiana widoku wedłóg ustawień
    import urlparse, urllib, urllib2, json
    __myurl__ = 'http://pure-cast.net'
    addon = xbmcaddon.addon(id='wtyczka.telewizja.polska')
    base_url = sys.argv[0]
    addon_handle = int(sys.argv[1])
    args = urlparse.parse_qs(sys.argv[2][1:])
    def build_url(query):
        return base_url + '?' + urllib.urlencode(query)
    PASSPC = addon.getSetting('pass_PC')
    EMAILPC = addon.getSetting('email_PC')
    url = 'http://pure-cast.net/kodi-filmy' + '?email=' + EMAILPC + '&pass=' + PASSPC
    headers = post = {}
    post = {}
    data = urllib.urlencode(post)
    reqUrl = urllib2.Request(url, data, headers)
    red_json = urllib2.urlopen(reqUrl)
    obj_data = json.load(red_json)
    for s in range(len(obj_data)):
     url = obj_data[s]['movieURL']
     li = xbmcgui.ListItem(obj_data[s]['movieName'], thumbnailImage=obj_data[s]['movieLogo'], iconImage=obj_data[s]['movieLogo'])
     xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)"""
    
    

#####################################################################################################
def tvp():
    xbmc.sleep( 100 )
    link = get_url()
    for i in link:
        url = 'plugin://wtyczka.telewizja.polska/?runstream=' + i[0] + '***' + i[1] + '***' + i[2]
        addLink(i[1],url,i[2])
        widokFilmowy('tak')
        xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET_MAIN+')') # Zmiana widoku
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)
############################################################################################################

def eska():
    widokFilmowy('nie')
# tv ###########################
    addLink("Eska TV", "rtmp://stream.smcloud.net/live2/eskatv/eskatv_480p", tv+'eska.png')
    addLink("Eska Best Music"+HD, "rtmp://stream.smcloud.net/live2/best/best_720p", tv+'eska_best_music.png') 
    addLink("Eska Party"+HD,"rtmp://stream.smcloud.net/live2/eska_party/eska_party_720p live=1",tv+'eska_party.png')
    addLink("Eska Rock"+HD,"rtmp://stream.smcloud.net/live2/eska_rock/eska_rock_720p live=1",tv+'eska_rock.png')
    addLink("VOX Music TV", "rtmp://stream.smcloud.net/live/vox2/stream1", tv+'vox_music.png') 
    addLink("VOX Old's Cool"+HD, "rtmp://stream.smcloud.net/live2/vox/vox_720p", tv+'vox_tv_2.png') 
    addLink("WaWa TV"+HD, "rtmp://stream.smcloud.net/live2/wawa/wawa_720p", tv+'wawa.png') 
    addLink("Polo TV","rtmp://stream.smcloud.net/live/polotv",tv+'polo.png')
    addLink("Polo Party"+HD, "rtmp://stream.smcloud.net/live2/polo_party/polo_party_720p", tv+'polo_party.png') 

# radio #########################
    addLink("Radio ESKA","http://s3.deb1.scdn.smcloud.net/t042-1.aac",play)
    addLink("Radio ESKA Rock","http://s3.deb1.scdn.smcloud.net/t041-1.aac",play)
    addLink("Radio ESKA Rock Polska","http://s3.deb1.scdn.smcloud.net/t008-1.mp3",play)
    addLink("Radio ESKA Party","http://s3.deb1.scdn.smcloud.net/t005-1.aac",play)
    addLink("Radio ESKA Summer City","http://s3.deb1.scdn.smcloud.net/t010-1.mp3",play)
    addLink("Radio ESKA Club","http://s3.deb1.scdn.smcloud.net/t004-1.mp3",play)
    addLink("Radio ESKA Tiesto","http://s3.deb1.scdn.smcloud.net/t023-1.mp3",play)
    addLink("Radio ESKA Goraca 20","http://s3.deb1.scdn.smcloud.net/t019-1.aac",play)
    addLink("Radio ESKA Goraca 100","http://s3.deb1.scdn.smcloud.net/t039-1.mp3",play)
    addLink("Radio ESKA Love","http://s3.deb1.scdn.smcloud.net/t038-1.mp3",play)
    addLink("Radio ESKA Young Stars","http://s3.deb1.scdn.smcloud.net/t025-1.mp3",play)
    addLink("Radio ESKA Hity Nie Tylko Na Czasie","http://s3.deb1.scdn.smcloud.net/t014-1.aac",play)
    addLink("Radio ESKA Global Lista","http://s3.deb1.scdn.smcloud.net/t016-1.mp3",play)
    addLink("Radio ESKA Dance","http://s3.deb1.scdn.smcloud.net/t012-1.mp3",play)
    addLink("Radio ESKA R'N'B","http://s3.deb1.scdn.smcloud.net/t003-1.mp3",play)
    addLink("Radio ESKA Ballads","http://s3.deb1.scdn.smcloud.net/t011-1.mp3",play)
    addLink("Radio ESKA Rap","http://s3.deb1.scdn.smcloud.net/t002-1.mp3",play)
    addLink("Radio ESKA Cinema","http://s3.deb1.scdn.smcloud.net/t024-1.mp3",play)
    addLink("Radio ESKA Armin Van Buuren","http://s3.deb1.scdn.smcloud.net/t032-1.mp3",play)
    addLink("Radio ESKA Nicky Romero","http://s3.deb1.scdn.smcloud.net/t022-1.mp3",play)
    addLink("Radio ESKA Ultra Music","http://s3.deb1.scdn.smcloud.net/t029-1.mp3",play)
    addLink("Radio ESKA Teksty FM","http://s3.deb1.scdn.smcloud.net/t026-1.mp3",play)
    addLink("Radio ESKA Justin Bieber","http://s3.deb1.scdn.smcloud.net/t099-1.mp3",play)
    addLink("Radio ESKA One Direction","http://s3.deb1.scdn.smcloud.net/t098-1.mp3",play)
    xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET_MAIN+')') # Zmiana widoku
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)

#####################################################################################
def yt():
    url="https://raw.githubusercontent.com/neopack1/kodi/master/json/yt_kanaly.json"
    headers = post = {}
    post = {}
    data = urllib.urlencode(post)
    reqUrl = urllib2.Request(url, data, headers)
    red_json = urllib2.urlopen(reqUrl)
    obj_data = json.load(red_json)
    for s in range(len(obj_data)):
        url = obj_data[s]['URL']
        thumb=obj_data[s]['LOGO']
        nazwa=obj_data[s]['NAZWA']
        tekst=obj_data[s]['TEKST']
        if tekst != "":
            nazwa=nazwa+" "+tekst
        addDir(nazwa,url,thumb)
        xbmc.sleep(20)
    widokFilmowy('tak')
    xbmc.sleep(50)
    WIDOK_SET = addon.getSetting('widok')
    xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET_MAIN+')') # Zmiana widoku wedłóg ustawień
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)

########################################################################################################
def zagraniczna():
    widokFilmowy('nie')
    xbmc.sleep(50)
    addJson("https://raw.githubusercontent.com/neopack1/kodi/master/json/inter.json")
    xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET+')') # Zmiana widoku
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)

#######################################################################################################################
#######################################################################################################################
def menuPPV():
    url='https://raw.githubusercontent.com/neopack1/kodi/master/files/menu-ppv.json'
    headers = post = {}
    post = {}
    data = urllib.urlencode(post)
    reqUrl = urllib2.Request(url, data, headers)
    red_json = urllib2.urlopen(reqUrl)
    obj_data = json.load(red_json)
    for s in range(len(obj_data)):
        url_1= obj_data[s]['URL']
        nazwa_1=obj_data[s]['NAZWA']
        logo=obj_data[s]['LOGO']
        if logo=="play" or logo=="icon":
            logo=play
        czas=obj_data[s]['TIME']
        nazwa_1="[B]"+nazwa_1+"[/B]   ["+czas+"]     "
        addLink(nazwa_1,url_1,logo)
    widokFilmowy('tak')
    xbmc.sleep(50)
    xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET_MAIN+')') # Zmiana widoku wedłóg ustawień
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)

#####################
def menu1():  #menu odpowiedzialne za główne kanały tv
    widokFilmowy('tak')
    if GRUPOWANIE=="false":
        menu_url="https://raw.githubusercontent.com/neopack1/kodi/master/files/menu1-tv.json"
    if GRUPOWANIE=="true":
        menu_url="https://raw.githubusercontent.com/neopack1/kodi/master/files/menu1-tv-grupy.json"
    headers = post = {}
    post = {}
    data = urllib.urlencode(post)
    reqUrl = urllib2.Request(menu_url, data, headers)
    red_json = urllib2.urlopen(reqUrl)
    obj_data = json.load(red_json)
    lp=0
    ext=" "
    xbmc.sleep( 150 )
    for s in range(len(obj_data)):
        lp=lp+1
        lpt=str(lp)
        if lp < 10:
            lpt="0"+str(lp)
        url = obj_data[s]['URL']
        thumb=obj_data[s]['LOGO']
        nazwa=obj_data[s]['NAZWA']
        jakosc=obj_data[s]['JAKOSC']
        KAT_ID=obj_data[s]['KAT_ID']
        if jakosc == "ld" or jakosc == "lq":
            ext=LD
        if jakosc == "hd":
            ext=HD
        if jakosc == "fhd":
            ext=FHD
        if jakosc == "uhd" or jakosc == "4k":
            ext=UHD
        if jakosc == "sd" or jakosc == "":
            ext=SD
        if KAT_ID=="10" and KOLOROWANIE=="true":
            nazwa_koncowa="[B]"+kolor10+nazwa+kolorEnd+"[/B] "
        if KAT_ID=="15" and KOLOROWANIE=="true":
            nazwa_koncowa="[B]"+kolor15+nazwa+kolorEnd+"[/B] "
        if KAT_ID=="20" and KOLOROWANIE=="true":
            nazwa_koncowa="[B]"+kolor20+nazwa+kolorEnd+"[/B] "
        if KAT_ID=="25" and KOLOROWANIE=="true":
            nazwa_koncowa="[B]"+kolor25+nazwa+kolorEnd+"[/B] "
        if KAT_ID=="30" and KOLOROWANIE=="true":
            nazwa_koncowa="[B]"+kolor30+nazwa+kolorEnd+"[/B] "
        if KAT_ID=="35" and KOLOROWANIE=="true":
            nazwa_koncowa="[B]"+kolor35+nazwa+kolorEnd+"[/B] "
        if KAT_ID=="40" and KOLOROWANIE=="true":
            nazwa_koncowa="[B]"+kolor40+nazwa+kolorEnd+"[/B] "
        if KAT_ID=="45" and KOLOROWANIE=="true":
            nazwa_koncowa="[B]"+kolor45+nazwa+kolorEnd+"[/B] "
        if KAT_ID=="50" and KOLOROWANIE=="true":
            nazwa_koncowa="[B]"+kolor50+nazwa+kolorEnd+"[/B] "
        if KAT_ID=="55" and KOLOROWANIE=="true":
            nazwa_koncowa="[B]"+kolor55+nazwa+kolorEnd+"[/B] "
        if KAT_ID=="99" and KOLOROWANIE=="true":
            nazwa_koncowa="[B]"+kolor99+nazwa+kolorEnd+"[/B] "
        if KOLOROWANIE=="false":
            nazwa_koncowa="[B][COLOR ghostwhite]"+lpt+"[/COLOR][/B] "+nazwa
        
        
        addLink(nazwa_koncowa+ext,url,tv+thumb)
#     li = xbmcgui.ListItem(nazwa, thumbnailImage=tv+thumb, iconImage=tv+thumb
#     xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li)
    
    widokFilmowy('tak')
    xbmc.sleep(50)
    xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET+')') # Zmiana widoku
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)

def menu2():  #menu z kanałami HD
    widokFilmowy('tak')
    menu_url="https://raw.githubusercontent.com/neopack1/kodi/master/files/menu1-tv.json"
    headers = post = {}
    post = {}
    data = urllib.urlencode(post)
    reqUrl = urllib2.Request(menu_url, data, headers)
    red_json = urllib2.urlopen(reqUrl)
    obj_data = json.load(red_json)
    ext=" "
    for s in range(len(obj_data)):
        url = obj_data[s]['URL']
        thumb=obj_data[s]['LOGO']
        nazwa=obj_data[s]['NAZWA']
        jakosc=obj_data[s]['JAKOSC']
        if jakosc == "uhd" or jakosc == "4k":
            ext=UHD
            nazwa_koncowa="[B]"+nazwa+"[/B] "
            addLink(nazwa_koncowa+ext,url,tv+thumb)
        if jakosc == "fhd":
            ext=FHD
            nazwa_koncowa="[B]"+nazwa+"[/B] "
            addLink(nazwa_koncowa+ext,url,tv+thumb)
        if jakosc == "hd":
            ext=HD
            nazwa_koncowa="[B]"+nazwa+"[/B] "
            addLink(nazwa_koncowa+ext,url,tv+thumb)
    xbmc.sleep( 200 )
    menu_url="https://raw.githubusercontent.com/neopack1/kodi/master/files/menu3-filmbox.json"
    reqUrl = urllib2.Request(menu_url, data, headers)
    red_json = urllib2.urlopen(reqUrl)
    obj_data = json.load(red_json)
    for s in range(len(obj_data)):
        url = obj_data[s]['URL']
        thumb=obj_data[s]['LOGO']
        nazwa=obj_data[s]['NAZWA']
        jakosc=obj_data[s]['JAKOSC']
        if jakosc == "uhd" or jakosc == "4k":
            ext=UHD
            nazwa_koncowa="[B]"+nazwa+"[/B] "
            addLink(nazwa_koncowa+ext,url,tv+thumb)
        if jakosc == "fhd":
            ext=FHD
            nazwa_koncowa="[B]"+nazwa+"[/B] "
            addLink(nazwa_koncowa+ext,url,tv+thumb)
        if jakosc == "hd":
            ext=HD
            nazwa_koncowa="[B]"+nazwa+"[/B] "
            addLink(nazwa_koncowa+ext,url,tv+thumb)
    xbmc.sleep( 200 )
    menu_url="https://raw.githubusercontent.com/neopack1/kodi/master/files/menu4-lokalna.json"
    reqUrl = urllib2.Request(menu_url, data, headers)
    red_json = urllib2.urlopen(reqUrl)
    obj_data = json.load(red_json)
    for s in range(len(obj_data)):
        url = obj_data[s]['URL']
        thumb=obj_data[s]['LOGO']
        nazwa=obj_data[s]['NAZWA']
        jakosc=obj_data[s]['JAKOSC']
        if jakosc == "uhd" or jakosc == "4k":
            ext=UHD
            nazwa_koncowa="[B]"+nazwa+"[/B] "
            addLink(nazwa_koncowa+ext,url,tv+thumb)
        if jakosc == "fhd":
            ext=FHD
            nazwa_koncowa="[B]"+nazwa+"[/B] "
            addLink(nazwa_koncowa+ext,url,tv+thumb)
        if jakosc == "hd":
            ext=HD
            nazwa_koncowa="[B]"+nazwa+"[/B] "
            addLink(nazwa_koncowa+ext,url,tv+thumb)
            
    widokFilmowy('tak')
    xbmc.sleep(50)
    xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET+')') # Zmiana widoku
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)



    
def menu3():  # Kanały FilmBox
    addJson('https://raw.githubusercontent.com/neopack1/kodi/master/files/menu3-filmbox.json')
    widokFilmowy('nie')
    xbmc.sleep(50)
    xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET+')') # Zmiana widoku wedłóg ustawień
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)
    
def menu4(): # Kanały Lokalne
    widokFilmowy('tak')
    xbmc.sleep(50)
    addJson('https://raw.githubusercontent.com/neopack1/kodi/master/files/menu4-lokalna.json')
    xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET+')') # Zmiana widoku wedłóg ustawień
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)
    
def menu5(): # Kanały looknij.tv
    widokFilmowy('tak')
    xbmc.sleep(50)
    addJson('https://raw.githubusercontent.com/neopack1/kodi/master/files/menu5-looknij.json')
    xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET+')') # Zmiana widoku wedłóg ustawień
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)
def menu6():

    xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET+')') # Zmiana widoku wedłóg ustawień
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)
def menu7():

    xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET+')') # Zmiana widoku wedłóg ustawień
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)
def menu8():

    xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET+')') # Zmiana widoku wedłóg ustawień
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)
def menu9(): 

    xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET+')') # Zmiana widoku wedłóg ustawień
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)
def menu10():

    xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET+')') # Zmiana widoku wedłóg ustawień
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)
#########################

xbmc.sleep(150)
widokFilmowy('nie')
xbmc.executebuiltin('Container.SetViewMode('+WIDOK_SET_MAIN+')')
main()