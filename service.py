from default import Hosts
import xbmc
import xbmcaddon

mon = xbmc.Monitor()
isService = xbmcaddon.Addon(id='script.skinhelper.ping').getSetting('service').upper()
xbmc.log('[script.skinhelper.ping] Service started', xbmc.LOGINFO)

while not mon.abortRequested():
    if mon.onSettingsChanged(): isService = xbmcaddon.Addon(id='script.skinhelper.ping').getSetting('service').upper()
    if isService == 'TRUE':
        hosts = Hosts()
        xbmc.log('[script.skinhelper.ping] %s/%s Servers active' % (hosts.serveron, hosts.servercount), xbmc.LOGDEBUG)

    if mon.waitForAbort(10):
        if isService == 'TRUE': del hosts
        xbmc.log('[script.skinhelper.ping] Service stopped')
        break
