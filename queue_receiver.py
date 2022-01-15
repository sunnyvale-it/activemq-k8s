import time
import sys

import stomp

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

def connect():
    conn.connect('artemis', 'simetraehcapa', wait=True, keepalive=True, heartbeats=(4000, 4000))

def subscribe():
    conn.subscribe(destination='/queue/test-anycast', id=1, ack='auto')

def connect_and_subscribe():
    connect()
    subscribe()

hosts = [('localhost', 30979)]
conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
connect_and_subscribe()

time.sleep(99999999)
conn.disconnect()