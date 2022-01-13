import time
import sys

import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print('received an error "%s"' % frame.body)

    def on_message(self, frame):
        print('received a message "%s"' % frame.body)

hosts = [('localhost', 30979)]
conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
conn.connect('artemis', 'simetraehcapa', wait=True)

conn.subscribe(destination='/queue/test-anycast', id=1, ack='auto')

print("Listening for messages...")


time.sleep(99999999)
conn.disconnect()