import eyeD3
import string

__author__ = 'sabrsorensen'

class M3U_Gen:
    def __init__(self, name):
        self.tagger = eyeD3.Tag()
        name = removeDisallowedFilenameChars(name)
        self.m3u_out = open(name + '.m3u', 'w')
        self.m3u_out.write("#Playlist " + name + " generated by gmusic_playlist_export\n#EXTM3U\n")

    def M3UEntry(self, path):
        self.tagger.link(path)
        artist = self.tagger.getArtist()
        title = self.tagger.getTitle()
        artist = removeDisallowedFilenameChars(artist)
        title = removeDisallowedFilenameChars(title)
        self.m3u_out.write("#EXTINF:," + artist + " - " + title + "\n")
        self.m3u_out.write(path + "\n")

    def M3UClose(self):
        self.m3u_out.close()

import unicodedata

validFilenameChars = "-_.() %s%s" % (string.ascii_letters, string.digits)

def removeDisallowedFilenameChars(filename):
    cleanedFilename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore')
    return ''.join(c for c in cleanedFilename if c in validFilenameChars)
