import easywebdav
import uuid

from config import davconfig

class WebDavHandler():
    def __init__(self):
        self.davclient = easywebdav.connect(host=davconfig['host'], port=davconfig['port'])

    def uploadFile(self, myFile):
        newId = str(uuid.uuid4())
        self.davclient.upload(myFile, remote_path=newId)
        newUrl = self.davclient.baseurl + '/' + newId
        return newUrl
