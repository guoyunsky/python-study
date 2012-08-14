'''
Created on Aug 14, 2012

@author: guoyun
'''
import os
import pyinotify

class OnWriteHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        os.system('echo create file:%s' % (os.path.join(event.path, event.name)))
        print "create file: %s" % os.path.join(event.path, event.name)
        
def auto_compile(path='.'):
    wm = pyinotify.WatchManager()
    mask = pyinotify.IN_CREATE
    notifier = pyinotify.Notifier(wm, OnWriteHandler())
    wm.add_watch(path, mask, rec = True, auto_add = True)
    print '==&gt; Start monitoring %s (type c^c to exit)' % path
    
    while True:
        try:
            notifier.process_events()
            if notifier.check_events():
                notifier.read_events()
        except KeyboardInterrupt:
            notifier.stop()
            break
            

if __name__ == '__main__':
    auto_compile('/tmp/test')