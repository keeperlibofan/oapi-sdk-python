# -*- coding: UTF-8 -*-
from larksuiteoapi.service.authen.v1 import Service as AuthenV1Service, AuthenAccessTokenReqBody

from sample.config.config import test_config_with_memory_store, test_config_with_redis_store
from larksuiteoapi import DOMAIN_FEISHU, DOMAIN_LARK_SUITE, Config

# for Cutome APP（企业自建应用）
app_settings = Config.new_internal_app_settings_from_env()

# for redis store and logger(level=debug)
conf = test_config_with_redis_store(DOMAIN_FEISHU, app_settings)

# for memory store and logger(level=debug)
# conf = test_config_with_memory_store(DOMAIN_FEISHU, app_settings)

service = AuthenV1Service(conf)


def test_access_token():
    body = AuthenAccessTokenReqBody()
    body.grant_type = "authorization_code"
    body.code = "VGXBlhrGO3LYkPzz0CA65f"
    resp = service.authens.access_token(body).do()
    print('request id = %s' % resp.get_request_id())
    print(resp.code)
    if resp.code == 0:
        print(resp.data)
    else:
        print(resp.msg)
        print(resp.error)


if __name__ == '__main__':
    test_access_token()
