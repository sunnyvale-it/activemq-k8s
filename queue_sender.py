import stomp
import sys

hosts = [('localhost', 30979)]
conn = stomp.Connection(host_and_ports=hosts)

conn.connect('artemis', 'simetraehcapa', wait=True)
conn.send(body=' '.join(sys.argv[1:]), destination='/queue/test-anycast')
conn.disconnect()