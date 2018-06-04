import oauth2 as oauth
import time
from urllib.parse import parse_qsl
import json

import requests

from .config import read_config
from .config import read_reqauth

def prepare_request(url, url_params):
    reqconfig = read_reqauth()
    config = read_config()

    token = oauth.Token(
        key=reqconfig.oauth_token,
        secret=reqconfig.oauth_token_secret
    )

    consumer = oauth.Consumer(
        key=config.consumer_key,
        secret=config.consumer_secret
    )

    params = {
        "oauth_version": "1.0",
        "oauth_nonce": oauth.generate_nonce(),
        "oauth_timestamp": str(int(time.time()))
    }

    params["oauth_token"] = token.key
    params["oauth_consumer_key"] = consumer.key

    params.update(url_params)

    req = oauth.Request(method="GET", url=url, parameters=params)

    signature_method = oauth.SignatureMethod_HMAC_SHA1()
    req.sign_request(signature_method, consumer, token)

    return req.to_url
