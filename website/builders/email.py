import json
# import requests
from django.conf import settings

class Mailer:
    def __init__(self):
        pass
    
    # def send_otp():
    #     return requests.post(
    #         "https://api.mailgun.net/v3/sandbox1955cf24da234bbf839b61e627bcede1.mailgun.org/messages",
    #         auth=("api", settings.MAILGUN_API_KEY),
    #         data={"from": "Andelinks <mailgun@sandbox1955cf24da234bbf839b61e627bcede1.mailgun.org>",
    #             "to": ['michaelejila13@gmail.com'],
    #             "subject": "New Upload",
    #             "template": "andelinks_otp",
    #             "t:variables": json.dumps({"otp": "New Response"})})
