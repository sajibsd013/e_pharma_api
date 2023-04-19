from users.models import MyUser
from partners.models import Doctor, CareGiver, Nurse, Partner
import requests
import json


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
        "recipient": to,
        "sender_id": "8809601003724",
        "type": "plain",
        "message": msg
    }
    # print(json.dumps(data, indent = 4) )

    responses = requests.post(url=api_url,  headers=headers,  json=data)
    response = responses.text
    print(response, responses)
    return responses.status_code


def send_sms_server2(to, msg):
    greenweburl = "http://api.greenweb.com.bd/api.php"
    print("SMS SENDING....")
    # your token code here
    token = "851716590116819019410ccdb961a9b493f4542db08e6013fc70"

    # sms receivers number here (separated by comma)

    data = {'token': token,
            'to': to,
            'message': msg}

    responses = requests.post(url=greenweburl, data=data)

    # response
    response = responses.text
    print(response)
    return response
    # print("SMS SEND!")



def get_num(obj, var):
    all_num = obj.objects.all().values(var)
    num_str = ""
    for num in all_num:
        phone = num[var]
        if "01" in phone:
            num_str += f"{phone},"
    return num_str


def promotional_sms(to_user, msg):
    print("promotional_sms called",)
    cust_num = get_num(MyUser, "phone")
    doc_num = get_num(Doctor, "mobile")
    care_num = get_num(CareGiver, "mobile")
    nurse_num = get_num(Nurse, "mobile")
    part_num = get_num(Partner, "mobile")

    if to_user == "All":
        all = cust_num+doc_num+care_num+nurse_num+part_num
        sms_num = all 
        # send_sms_server2(all, msg)
    elif to_user == "Customers":
        sms_num = cust_num 
        # send_sms_server2(cust_num, msg)
    elif to_user == "Doctor":
        sms_num = doc_num 
        # send_sms_server2(doc_num, msg)
    elif to_user == "Caregiver":
        sms_num = care_num 
        # send_sms_server2(care_num, msg)
    elif nurse_num == "Nurse":
        # send_sms_server2(nurse_num, msg)
        sms_num = nurse_num 
    elif part_num == "Partner":
        sms_num = part_num 
        # send_sms_server2(part_num, msg)

    res = send_sms_server2(sms_num, msg)
    return res

    


def send_otp(to, otp):
    msg = f"Your sasthosebok.com Verification Code is {otp}"
    send_sms(to, msg)


def send_admin_notifications(msg):
    send_sms("8801959970664", msg)
