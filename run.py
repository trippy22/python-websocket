from websocket import config, wsserver

# Runs server
print(f'Starting server on port {config.socket_port}. Waiting for connections... ')
wsserver.Server().run()
