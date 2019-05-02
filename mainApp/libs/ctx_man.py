from contextlib import contextmanager

from requests import RequestException


@contextmanager
def catch_error(result_dict:dict):
    try:
        yield
    except Exception as e:
        if isinstance(e, (ConnectionError,RequestException)):
            result_dict['status'] = 2 # 网址无效，或者本地挂掉了
        elif isinstance(e,(IndexError)):
            result_dict['status'] = 0 # 账号密码错误，导致匹配不上，也可能是网页结构改变了
        elif isinstance(e,(TimeoutError)):
            result_dict['status'] = 3 # cookie过期或者不存在
        else:
            raise e #未知错误
