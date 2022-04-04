import os
from pathlib import Path

def by_mtime(file):
    return file.stat().st_mtime

workDir = os.getcwd()           
srcFld=workDir + "\\Anwendungen\\Zir_File_RepNrAbschneidenUndDatumUmwandeln\\srcZir\\"    
srcFile = max((p for p in Path(srcFld).iterdir() if p.is_file()), key=by_mtime,)
srcFileName= os.path.split(srcFile)[1]  
dstFile = workDir +"\\Anwendungen\\Zir_File_RepNrAbschneidenUndDatumUmwandeln\\dstZir\\changed-"+ srcFileName





