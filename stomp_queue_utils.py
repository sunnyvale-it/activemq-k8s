import stomp

hosts = [('localhost', 30979)]
conn = stomp.Connection12(host_and_ports=hosts)
username = 'artemis'
password = 'simetraehcapa'

def connect():
    conn.connect(username, password, wait=True, keepalive=True, heartbeats=(4000, 4000))

def subscribe():
    conn.subscribe(destination='/queue/test-anycast', id=1, ack='auto')

def connect_and_subscribe():
    connect()
    subscribe()