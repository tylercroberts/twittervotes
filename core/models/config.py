import os
import yaml

from .models import Config

def _read_yaml_file(filename, cls):
    core_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(core_dir, "..", filename)

    with open(filepath, 'r', encoding="UTF-8") as f:
        config = yaml.load(f)
        return cls(**config)


def read_config():
    try:
        return _read_yaml_file('config.yaml', Config)

    except IOError as e:
        print("""Couldn't find the configuration file `config.yaml` on your current directory
        
        Default format is:',

        consumer_key: 'your_consumer_key'
        consumer_secret: 'your_consumer_secret'
        request_token_url: 
        'https://api.twitter.com/oauth/request_token'
        access_token_url:  
        'https://api.twitter.com/oauth/access_token'
        authorize_url: 'https://api.twitter.com/oauth/authorize'
        api_version: '1.1'
        search_endpoint: ''
        """)
        raise