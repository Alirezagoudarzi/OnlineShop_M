from kavenegar import *

def send_otp_code(phone_number,code):
    try:
        api = KavenegarAPI('6B687649436E70516F77624D5866573630506347694B553753393530417061464A716739423272453030303D')
        params = { 
            'sender' : '',
            'receptor': phone_number,
            'message' :f'کد تایید شما {code} می باشد. با تشکر گودرزی' 
            }
        response = api.sms_send( params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)


from kavenegar import *
