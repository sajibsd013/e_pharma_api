from rest_framework_simplejwt.tokens import RefreshToken
from api.models import OTP


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'token': str(refresh.access_token),
    }


def isOtpMatcheed(phone, otp, type):
    try:
        otp_dict = OTP.objects.filter(phone=phone)
        otp_db = otp_dict[len(otp_dict)-1].otp
        if otp == otp_db:
            if type == "login":
                otp_dict.delete()
            return True
        return False
    except:
        return False
