# coding: utf-8

import xbmc

xbmc.log('script.tester service started')


class MyMonitor(xbmc.Monitor):
    def onNotification(self, sender, method, data):
        xbmc.log('### Monitor.onNotification ###')
        xbmc.log('Sender: {0}; Method: {1}; Data: {2}'.format(sender, method, data))
        xbmc.log('##############################')



class MyPlayer(xbmc.Player):
    current_time = -1
    total_time = -1
    def onPlayBackStarted(self):
        try:
            self.total_time = self.getTotalTime()
        except:
            self.total_time = -1
        xbmc.log('$$$ Player.onPlayBackStarted $$$')
        xbmc.log('$$$ File: {0} $$$'.format(self.getPlayingFile()))
        xbmc.log('$$$ Total time: {0} $$$'.format(self.total_time))

    def onPlayBackStopped(self):
        xbmc.log('$$$ Player.onPlayBackStopped $$$')
        xbmc.log('$$$ Current time: {0} $$$'.format(self.current_time))
        xbmc.log('$$$ Total time: {0} $$$'.format(self.total_time))

    def onPlayBackEnded(self):
        xbmc.log('$$$ Player.onPlayBackEnded $$$')
        xbmc.log('$$$ Current time: {0} $$$'.format(self.current_time))
        xbmc.log('$$$ Total time: {0} $$$'.format(self.total_time))

    def update_time(self):
        try:
            self.current_time = self.getTime()
        except:
            self.current_time = -1
        if self.total_time <= 0:
            try:
                self.total_time = self.getTotalTime()
            except:
                self.total_time = -1

        


monitor = MyMonitor()
player = MyPlayer()

while not monitor.abortRequested():
    xbmc.sleep(1000)
    if player.isPlaying():
        player.update_time()

xbmc.log('script.tester service stopped')
