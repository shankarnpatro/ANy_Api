import requests
from smart.config import regApiName, currentPasswordName, AuthorizationName
from smart import get_password


class Token:

    def __init__(self):
        self.passwordUrl = currentPasswordName
        self.tokenUrl = regApiName
        self.user = AuthorizationName

    def get_password(self):
        password = requests.post(self.passwordUrl)
        response = password.status_code
        pwd_content = password.content
        return pwd_content

    def get_token(self):

        password = self.get_password()
        token = requests.post(url=self.tokenUrl, auth=(self.user, password))
        response = token.status_code
        token_content = token.content
        return token_content

obj = Token()
print(obj.get_token())