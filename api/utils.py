from asyncio.windows_events import NULL
from users.models import MyUser
from random import randrange
from .models import OTP, SMS_TOKEN

import requests


def send_otp_checker(phone, type):
    res = {
        "msg": NULL, "c_type": False
    }

    try:
        user = MyUser.objects.get(phone=phone)
        if type == "register":
            res["c_type"] = False
            res["msg"] = "User already exists"

        elif type == "login":
            res["c_type"] = True

        return res

    except:
        if type == "login":
            res["c_type"] = False
            res["msg"] = "User Not Found"

        elif type == "register":
            res["c_type"] = True

        return res


def send_otp(to, otp):

    token_dist = SMS_TOKEN.objects.get(status="active")
    token = token_dist.token
    api_url = token_dist.api_url
    msg = f"Your OTP is {otp}"

    data = {'token': token,
            'to': to,
            'message': msg
            }

    responses = requests.post(url=api_url, data=data)

    response = responses.text
    print(response, responses)

    # return response
