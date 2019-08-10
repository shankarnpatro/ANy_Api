import base64
import requests
import logging
from logging.handlers import RotatingFileHandler
import traceback
from smart.config import getAllUrl, regApiName

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
        # print(head)
        token = requests.post(url=API_ENDPOINT, headers=head)
        print("Bearer token",token.content)
        print("token.status_code",token.status_code)

        logger.info("Able to find Token:%s"%bearerToken)
    except Exception as eobj:
        logger.error("Error while getting bearer token:%s"%eobj)
        print("getToken", eobj)
    return token.content

def get_All(in_token):
    """
    :param in_token: Bearer
    :return: Customers Details
    """
    try:
        API_ENDPOINT = getAllUrl
        h = {'Authorization': 'Bearer {0}'.format(in_token.decode("utf-8"))}
        response = requests.post(url=API_ENDPOINT, headers=h)
        print("get_All-response.status_code",response.status_code)
        print(response.content)
    except Exception as eobj:
        logger.error("Error while getting return token:%s" % eobj)
        print("get_All",eobj)

custEmail = input("Enter your valid email address:")
custPwd = input("Enter your Password:")
token = getToken(custEmail, custPwd)
get_All(token)
