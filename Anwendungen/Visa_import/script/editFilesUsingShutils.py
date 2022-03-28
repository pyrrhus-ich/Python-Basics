# import built in module
import shutil, os.path
# import eigene module
from settings import *
from loghandler import logger as lg

# Räumt den dst Folder auf und verschiebt die Files nach arc

def cleanDst(dst):
    lg.info("<<<<<<<<<<<<<<   CLEARING DST Folder gestartet >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    dir = os.listdir(dst)
    for el in dir:
        src = dst + el
        shutil.move(src, arcFolder)
        lg.info("{} was moved to arc".format(el))
    lg.info("<<<<<<<<<<<<<<<  CLEARING DST Folder BEENDET >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def cleanArc(arc):
    lg.info("<<<<<<<<<<<<<<< Clearing Arc gestartet >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    dir = os.listdir(arc)
    dirSort = sorted(dir)
    lenDirSort = len(dirSort)
    while lenDirSort > 10:
        remFile = arc + dirSort[0]
        os.remove(remFile)
        lg.info("File {} removed".format(dirSort[0]))
        lenDirSort = lenDirSort -1
        dirSort.pop(0)
    lg.info("<<<<<<<<<<<<< Clearing Arc beendet >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    
   


        


