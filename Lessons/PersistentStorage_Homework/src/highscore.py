"""Creates a high score table from input, shelves it,
and then alters it to represent a new high score if necessary"""
import shelve

def scoreTable(playername, score):
    shelf = shelve.open(r'v:\workspace\PersistentStorage_Homework\src\testshelf.shlf')
    if playername in shelf.keys():
        if shelf[playername] < score:
            shelf[playername] = score
    else:
        shelf[playername] = score
    return shelf[playername]
    shelf.close()