import requests
import datetime
import logging
from logging.handlers import RotatingFileHandler
import traceback
from smart import config
from smart.config import regApiName, currentPasswordName, resetPwdUrl, AuthorizationName

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
    global pwd_content
    try:
        pwd_content = ''
        url = currentPasswordName
        # print(url)
        password = requests.post(url)
        response = password.status_code
        pwd_content = password.content
        print("Get Password status.code", response)
        logger.info("Able to find the  password:%s"%str(pwd_content))
    except Exception as e:
        print(e)
        logger.error(traceback.format_exc())
    return pwd_content

def getToken(pwd_content,AuthorizationName):

    try:
        # bearerToken = ''
        url = regApiName
        pwd_content =getPassword()
        token = requests.post(url, auth=(config.AuthorizationName, pwd_content))
        response = token.status_code
        bearerToken = token.content
        logger.info("Able to find Token:%s"%bearerToken)
    except Exception as eobj:
        logger.error("Error while getting bearer token:%s"%eobj)
    return bearerToken

def reset_password(custEmail):

    pwd_content = getPassword()
    if len(pwd_content) >=6:
        BearerToken = getToken(pwd_content,AuthorizationName)
        print(BearerToken)
        customerInfo = {"email": custEmail}
        myUrl = resetPwdUrl
        h = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(BearerToken.decode("utf-8"))}
        response = requests.post(url=myUrl, headers=h, json=customerInfo)
        print("reset password Status.code", response.status_code)
        print(response.content)
    else:
        print("no data found")

custEmail = input("Enter your valid email address: ")
reset_password(custEmail)