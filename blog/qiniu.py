# -*- coding:utf-8 -*-
from hashlib import sha1
import hmac
import base64
import datetime
import time
import os


def getToken():
    AK = 'akHgJmEI_OItYI6BkyDCMyAwxVl4sVeBYH6jXi8N'
    SK = 'skZhe0qoWRRyEelxeXcO2CL7IoClhI0uv8CCIPxB'
    dl=int(time.mktime(datetime.datetime.now().timetuple()))+21600
    s='{"scope":"skyin","deadline":%s,"returnBody":"{"name":$(fname)}"}'%(dl,)
    s=base64.urlsafe_b64encode(s)
    sign=hmac.new(SK,s,sha1).digest()
    sign = base64.urlsafe_b64encode(sign)
    token = AK + ':' + sign + ':' + s
    return token
