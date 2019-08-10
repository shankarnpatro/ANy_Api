import base64
import requests
import logging
from logging.handlers import RotatingFileHandler
from smart.config import getAllUrl, regApiName, getSwtchControlUrl
import json

'''Logging handler'''
logger = logging.getLogger("API")
logger.setLevel(logging.DEBUG)
'''add a rotating handler'''
handler = RotatingFileHandler("API.log", maxBytes=300000000, backupCount=15)
handler.setLevel(logging.DEBUG)
fmtr = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
handler.setFormatter(fmtr)
logger.addHandler(handler)

def getToken(custEmail, custPwd, bearerToken=None, mystring=None):
    '''
    :param bearerToken: Bearer token
    :return: Token as CustReg
    '''
    try:
        bearerToken = ''
        API_ENDPOINT = regApiName
        emailAndPass = base64.b64encode(custEmail.encode('ascii') + ":".encode('ascii') + custPwd.encode('ascii')).decode("ascii")
        head = {'Authorization': 'Basic %s' % emailAndPass}
        token = requests.post(url=API_ENDPOINT, headers=head)
        print("token.status_code",token.status_code)
        # logger.info("Able to find Token:%s"%bearerToken)
    except Exception as eobj:
        logger.error("Error while getting bearer token:%s"%eobj)
        print("getToken", eobj)
    return token.content

def get_All(in_token):
    '''
    :param bearerToken: Bearer token
    :return: return getall detils of customer
    '''
    try:
        API_ENDPOINT = getAllUrl
        h = {'Authorization': 'Bearer {0}'.format(in_token.decode("utf-8"))}
        response = requests.post(url=API_ENDPOINT, headers=h)
        print("get_All-response.status_code: ",response.status_code)
        getallContent = json.loads(response.content)
        switch_control(getallContent, in_token)
    except Exception as eobj:
        logger.error("Error while getting return token:%s" % eobj)
        print("get_All",eobj)

def switch_control(getallContent, in_token=None):
    """
    :param getallContent: fetching all the data from get_all
    :param in_token: Bearer token
    :return: Status of the content
    """
    try:
        if len(getallContent):
            print(type(getallContent))
            serialNum = getallContent[0]['Serial']
            unitId = getallContent[0]['UnitId']
            level = getallContent[0]['Level']
            state = getallContent[0]['State_']
            endpoint = getSwtchControlUrl
            getAllData = {'Serial': str(serialNum), 'UnitId': str(unitId), 'Level': str(level), 'State_': str(state), 'Testing': 'true'}
            print(getAllData)
            print("type of ini_object", type(getAllData))
            # ini_string = json.dumps(getAllData)
            h = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(in_token.decode("utf-8"))}
            response = requests.post(url=endpoint, json=getAllData, headers=h)
            print("switch_control response.status_code :", response.status_code)
            print(response.content)
        else:
            print("No content recived")
    except Exception as eobj:
        logger.error("Error while getting return token:%s" % eobj)
        print("switch_control",eobj)

custEmail = input("Enter your valid email address: ")
custPwd = input("Enter your Password: ")
token = getToken(custEmail, custPwd)
get_All(token)