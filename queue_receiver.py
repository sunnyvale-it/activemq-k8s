import time
import sys

import stomp
from queue_utils import *

class MyListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print('Received an error "%s"' % frame.body)
    def on_message(self, frame):
        print('Received a message "%s"' % frame.body)
    def on_disconnected(self):
        print('Disconnected')
        connect_and_subscribe()
    def on_connected(self, frame):
        print("Connected")

conn.set_listener('', MyListener())
connect_and_subscribe()

time.sleep(99999999)
conn.disconnect()