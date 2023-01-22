from users.models import MyUser
from .models import OTP

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


def send_sms(to, msg):
    token = 'Bearer 95|kpmjxX6RXffNm1IPzflQcrqmT15o4z08vG5nC2Vp'
    api_url = 'https://login.esms.com.bd/api/v3/sms/send'

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

# def send_sms_d_host(to, msg):
#     token = 'Bearer 95|kpmjxX6RXffNm1IPzflQcrqmT15o4z08vG5nC2Vp'
#     api_url = 'https://login.esms.com.bd/api/v3/sms/send'

#     headers = {
#         'Authorization': token,
#         'Accept': 'application/json',
#         'Content-Type': 'application/json',
#     }

#     data = {
#         'recipient': to,
#         'sender_id': '8809601003724',
#         'message': msg
#     }

#     responses = requests.post(url=api_url,  headers=headers,  json=data)
#     response = responses.text
#     print(response, responses)
#     return responses.status_code


def send_otp(to, otp):
    msg = f"Your sasthosebok.com Verification Code is {otp}"
    send_sms(to, msg)


def send_admin_notifications(msg):
    send_sms("8801959970664", msg)
