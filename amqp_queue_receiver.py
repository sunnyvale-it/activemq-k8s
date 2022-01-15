from proton.handlers import MessagingHandler
from proton.reactor import Container


class Recv(MessagingHandler):
    def __init__(self, url, count):
        super(Recv, self).__init__()
        self.url = url
        self.expected = count
        self.received = 0

    def on_start(self, event):
        self.acceptor = event.container.listen(self.url)

    def on_message(self, event):
        if event.message.id and event.message.id < self.received:
            # ignore duplicate message
            return
        if self.expected == 0 or self.received < self.expected:
            print(event.message.body)
            self.received += 1
            if self.received == self.expected:
                event.receiver.close()
                event.connection.close()
                self.acceptor.close()


try:
    Container(Recv('localhost:5672/queue/test-anycast', 0)).run()
except KeyboardInterrupt:
    pass