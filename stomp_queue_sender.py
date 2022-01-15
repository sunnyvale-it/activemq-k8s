import stomp
import sys
from stomp_queue_utils import *

class MyListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print('Received an error "%s"' % frame.body)
    def on_disconnected(self):
        print('Disconnected')
        connect()
    def on_connected(self, frame):
        print("Connected")

conn.set_listener('', MyListener())
connect()
conn.send(body=' '.join(sys.argv[1:]), destination='/queue/test-anycast')
print('Sent message: %s' % ' '.join(sys.argv[1:]))
conn.disconnect()