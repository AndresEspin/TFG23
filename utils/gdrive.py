from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

import pandas as pd

from strenum import StrEnum

class GDriveHost(StrEnum):
    MINE = "root"
    SHARED_WITH_ME = "sharedWithMe"
    
class GDriveUtil():
    
    def __init__(self):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
        self.drive = GoogleDrive(gauth)

    def getFile(self, fileFQN):
        fileFQN_host="root"
        if fileFQN.find(":") !=-1:
            aux=fileFQN.split(":")
            if aux[0]!="":
                fileFQN_host=aux[0]
            fileFQN_path=aux[1]
        pathParts=fileFQN_path.split("/")
        del pathParts[0]
        fileID = fileFQN_host
        for pathPart in pathParts:
            if fileID == "sharedWithMe":
                fileList = self.drive.ListFile({'q': "sharedWithMe and trashed=false"}).GetList()
            else:
                fileList = self.drive.ListFile({'q': f"'{fileID}' in parents and trashed=false"}).GetList()
            
            for file in fileList:
                if(file['title'] == pathPart and file['mimeType'] != "application/vnd.google-apps.shortcut"):
                    fileID = file['id']
        return self.drive.CreateFile({'id': fileID})
    
    def saveFile(self,fileFQN, filename=None):
        file = self.getFile(fileFQN)
        if filename is None:
            file.FetchMetadata(fields='title')
            filename=file['title']
        file.GetContentFile(filename)
    
    def getFileAsString(self,fileFQN, encoding="utf-8"):
        return self.getFile(fileFQN).GetContentString(encoding=encoding)

    def getFileAsIO(self,fileFQN, encoding="utf-8"):
        return StringIO(
            self.getFileAsString(fileFQN, encoding=encoding)
        )
    def getCSVFileAsDF(self,fileFQN, **kwargs):
        return pd.read_csv(
            self.getFileAsIO(fileFQN),
            **kwargs
        )
    def getRPTFileAsDF(self,fileFQN, sep="|"):
        return pd.read_fwf(
            self.getFileAsIO(fileFQN),
            sep=sep
        )
    def getXLSFileAsDF(self,fileFQN, **kwargs):
        TMP_FILE="/tmp/tmp1.xls"
        self.saveFile(fileFQN, TMP_FILE)
        return pd.read_excel(
            TMP_FILE,
            **kwargs
        )






