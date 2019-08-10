import requests
from smart import config
from smart.config import regApiName
import datetime
import logging
from logging.handlers import RotatingFileHandler
import traceback
from smart import get_password

'''Logging handler'''
logger = logging.getLogger("API")
logger.setLevel(logging.DEBUG)
'''add a rotating handler'''
handler = RotatingFileHandler("API.log", maxBytes=300000000, backupCount=15)
handler.setLevel(logging.DEBUG)
fmtr = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
handler.setFormatter(fmtr)
logger.addHandler(handler)

def getToken(bearerTokengetToken=None):
    try:
        bearerToken = ''
        url = regApiName
        pwd_con = get_password.getPassword()
        token = requests.post(url, auth=(config.AuthorizationName, pwd_con))
        response = token.status_code
        print(response)
        bearerToken = token.content
        print(bearerToken)
        logger.info("Able to find Token:%s"%bearerToken)
    except Exception as eobj:
        logger.error("Error while getting bearer token:%s"%eobj)
    # return bearerTokengetToken()

getToken()