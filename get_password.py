import requests
import datetime
import logging
from logging.handlers import RotatingFileHandler
import traceback
from smart.config import currentPasswordName

'''Logging handler'''
logger = logging.getLogger("API")
logger.setLevel(logging.DEBUG)
'''add a rotating handler'''
handler = RotatingFileHandler("API.log", maxBytes=300000000, backupCount=15)
handler.setLevel(logging.DEBUG)
fmtr = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
handler.setFormatter(fmtr)
logger.addHandler(handler)


def getPassword():
    """
    Taking url api as input
    :return: returning password as token
    """
    # global pwd_content
    try:
        pwd_content = ''
        url = currentPasswordName
        print(url)
        password = requests.post(url)
        response = password.status_code
        pwd_content = password.content
        print(response)
        print(pwd_content)
        logger.info("Able to find the  password:%s"%str(pwd_content))
        #file.write(str(pwd_content))
    except Exception as e:
        print(e)
        logger.error(traceback.format_exc())
    return pwd_content
getPassword()