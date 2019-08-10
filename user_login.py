import requests
import datetime
import logging
from logging.handlers import RotatingFileHandler
import traceback
from smart import config
from smart.config import currentPasswordName, regApiName, reg_newApi

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
        #file = open('E:\\SmartAny\config\pwd.json','w')#Need to change this to json
        url = currentPasswordName
        # print(Url)
        password = requests.post(url)
        res = password.status_code
        pwd_content = password.content
        logger.info("Able to find the  password:%s"%str(pwd_content))
        #file.write(str(pwd_content))
    except Exception as e:
        print (e)
        logger.error(traceback.format_exc())
    return pwd_content

def bearerToken(args):
    pass

def getToken(bearerToken=None):
    '''
    :param bearerToken: Bearer token
    :return: Token as CustReg
    '''
    try:
        bearerToken = ''
        url = regApiName
        pwd_con = getPassword()
        token = requests.post(url, auth=(config.AuthorizationName, pwd_con))
        bearerToken = token.content
        # print(bearerToken)
        logger.info("Able to find Token:%s"%bearerToken)
    except Exception as eobj:
        logger.error("Error while getting bearer token:%s"%eobj)
    return bearerToken

def customerRegister(custName,custEmail,custPwd):
    '''
    Taking Token as input for Creating CustID
    :param custName: sankar
    :param custEmail: sankar@gmail.com
    :param custPwd: sanka@R#4
    :return: CustID for Upadeting Csmt
    '''
    try:
        customerInfo = {"customerName": custName, "email": custEmail, "password": custPwd}
        print(customerInfo)
        BearerToken = getToken()
        print(BearerToken)
        myUrl = reg_newApi
        h = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(BearerToken.decode("utf-8"))}
        response = requests.post(url=myUrl, headers=h, json=customerInfo)
        print(response.status_code)
    except Exception as eobj:
        logger.error("Error while getting return token:%s"%eobj)

custName = input("Enter your name:")
custEmail = input("Enter your valid email address:")
custPwd = input("Enter your Password:")
customerRegister(custName,custEmail,custPwd)