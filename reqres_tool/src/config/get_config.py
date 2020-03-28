from configparser import ConfigParser

__config = ConfigParser()
__config.read("reqres_tool/src/config/config.cfg")


def get_config():
    return __config
