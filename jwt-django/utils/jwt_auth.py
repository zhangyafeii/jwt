# -*- coding:utf-8 -*-

import jwt
import datetime
from jwt import exceptions

JWT_SALT = 'iv%x6xo7l7_u9bf_u!9#g#m*)*=ej@bek5)(@u3kh*72+unjv='


def create_token(payload, timeout=60):
    """
    :param payload:  例如：{'user_id':1,'username':'wupeiqi'}用户信息
    :param timeout: token的过期时间，默认60分钟
    :return:
    """
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout)
    result = jwt.encode(payload=payload, key=JWT_SALT, algorithm="HS256", headers=headers).decode('utf-8')
    return result


def parse_payload(token):
    """
    对token进行和发行校验并获取payload
    :param token:
    :return:
    """
    result = {'status': 200, 'data': None, 'error': None}
    try:
        verified_payload = jwt.decode(token, JWT_SALT, True)
        result['data'] = verified_payload
    except exceptions.ExpiredSignatureError:
        result['status'] = 251
        result['error'] = 'token已失效'
    except jwt.DecodeError:
        result['status'] = 252
        result['error'] = 'token认证失败'
    except jwt.InvalidTokenError:
        result['status'] = 253
        result['error'] = '非法的token'
    return result
