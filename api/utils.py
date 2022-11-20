from users.models import MyUser
from random import randrange
from .models import OTP, SMS_TOKEN

import requests


def send_otp_checker(phone, type):
    res = {
        "msg": 'NULL', "c_type": False
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
    msg = f"Your Verification Code is {otp}"
    print('send_otp', to)

    headers = {
        'Authorization': token,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    data = {
        'recipient': "+8801771148384",
        'sender_id': '8809601003724',
        'message': msg
    }

    responses = requests.post(url=api_url,  headers=headers,  json=data)
    response = responses.text
    print(response, responses)

    # return response


def send_sms(to, msg):
    token_dist = SMS_TOKEN.objects.get(status="active")
    token = token_dist.token
    api_url = token_dist.api_url

    headers = {
        'Authorization': token,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    data = {
        'recipient': to,
        'sender_id': '8809601003724',
        'message': msg
    }

    responses = requests.post(url=api_url,  headers=headers,  json=data)
    response = responses.text
    print(response, responses)
    return responses.status_code


def send_admin_notifications(msg):
    token_dist = SMS_TOKEN.objects.get(status="active")
    token = token_dist.token
    api_url = token_dist.api_url

    headers = {
        'Authorization': token,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    data = {
        'recipient': "+8801959970664",
        'sender_id': '8809601003724',
        'message': msg
    }

    responses = requests.post(url=api_url,  headers=headers,  json=data)
    response = responses.text
    print(response, responses)
    return responses.status_code
