import jwt
from django.conf import settings
from datetime import datetime, timedelta
from rest_framework.exceptions import AuthenticationFailed
def create_jwt(user):
    payload = {
        'user_id' : user.id,
        'exp' : datetime.utcnow()+timedelta(days=1),
        'iat' : datetime.utcnow()
    }
    
    if not valid_jwt(user.token) or user.token=="":
        token = jwt.encode(payload,settings.SECRET_KEY, algorithm='HS256')
        return token
    return user.token

def decode_jwt(token):
    try:
        payload = jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('token exiperd')
    except jwt.InvalidTokenError:
        raise AuthenticationFailed('invalid token')

def valid_jwt(token):
    try:
        jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False