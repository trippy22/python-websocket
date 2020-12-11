from websocket import config, wsserver

# Runs server
print(f'Starting server on port %s. Waiting for connections... {config.socket_port}')
wsserver.Server().run()
