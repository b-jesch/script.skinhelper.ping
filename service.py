from default import Hosts
import xbmc
import xbmcaddon

mon = xbmc.Monitor()
xbmc.log('[script.skinhelper.ping] Service started', xbmc.LOGINFO)

while not mon.abortRequested() and xbmcaddon.Addon().getSetting('service').upper() == 'TRUE':
    hosts = Hosts()
    xbmc.log('[script.skinhelper.ping] %s/%s Servers active' % (hosts.serveron, hosts.servercount), xbmc.LOGDEBUG)

    if mon.waitForAbort(10):
        del hosts
        xbmc.log('[script.skinhelper.ping] Service stopped')
        break