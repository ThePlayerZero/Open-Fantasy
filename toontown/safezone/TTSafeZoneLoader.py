from pandac.PandaModules import *
from . import SafeZoneLoader
from . import TTPlayground
import random
from toontown.launcher import DownloadForceAcknowledge


class TTSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(
            self, hood, parentFSM, doneEvent)
        self.playgroundClass = TTPlayground.TTPlayground
        self.musicFile = 'user/resources/default/phase_4/audio/bgm/TC_nbrhood.ogg'
        self.activityMusicFile = 'user/resources/default/phase_3.5/audio/bgm/TC_SZ_activity.ogg'
        self.dnaFile = 'user/resources/default/phase_4/dna/toontown_central_sz.dna'
        self.safeZoneStorageDNAFile = 'user/resources/default/phase_4/dna/storage_TT_sz.dna'

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.birdSound = list(map(base.loader.loadSfx,
                                  ['user/resources/default/phase_4/audio/sfx/SZ_TC_bird1.ogg',
                                   'user/resources/default/phase_4/audio/sfx/SZ_TC_bird2.ogg',
                                   'user/resources/default/phase_4/audio/sfx/SZ_TC_bird3.ogg']))

    def unload(self):
        del self.birdSound
        SafeZoneLoader.SafeZoneLoader.unload(self)

    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)

    def exit(self):
        SafeZoneLoader.SafeZoneLoader.exit(self)
