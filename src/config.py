from configparser import SafeConfigParser

config = SafeConfigParser()
config.read('regis-config.ini')

mongoconfig = {
    'host': config.get('mongo', 'host'),
    'port': config.getint('mongo', 'port'),
    'user': config.get('mongo', 'username', fallback=None),
    'pass': config.get('mongo', 'password', fallback=None),
    'db'  :config.get('mongo', 'database'),
    'collection': config.get('mongo', 'collection')
}

davconfig = {
    'host': config.get('webdav', 'host'),
    'port': config.getint('webdav', 'port')
}

globalconfig = {
    'name': config.get('global', 'name'),
    'version': config.get('global', 'version'),
    'layerTypes': config.get('global', 'layertypes').split(',')
}
