from app import create_app
from config import Config

instance = create_app()
app = instance['app']
socket_io = instance['socket']

if __name__ =="__main__":
    socket_io.run(
        app,
        host = Config.HOST,
        port = Config.PORT,
        debug = Config.DEBUG
    )