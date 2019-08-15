import base64
import requests
from smart.config import regApiName, getAllUrl

class Token:

    def __init__(self, custEmail, custPwd):

        self.custEmail = custEmail
        self.custPwd = custPwd
        self.tokenUrl = regApiName
        self.getallUrl = getAllUrl


    def get_token(self):

        emailAndPass = base64.b64encode(self.custEmail.encode('ascii') + ":".encode('ascii') + self.custPwd.encode('ascii')).decode("ascii")
        head = {'Authorization': 'Basic %s' % emailAndPass}
        token = requests.post(url=self.tokenUrl, headers = head)
        response = token.status_code
        token_content = token.content
        return token_content

    def get_all(self, in_token=None):

        in_token = self.get_token()
        h = {'Authorization': 'Bearer {0}'.format(in_token.decode("utf-8"))}
        response = requests.post(url=self.getallUrl, headers=h)
        res = response.content
        re = response.status_code
        return res

custEmail= input("Enter your valid email address:")
custPwd = input("Enter your Password:")
obj = Token(custEmail,custPwd)

print(obj.get_token())
print(obj.get_all(in_token=None))