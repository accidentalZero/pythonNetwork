#!/usr/bin/env python3
# Network Programming in Python: The Basics
# Сервер написан с помощью устаревшего модуля socketserver из стандартной библиотеки

from socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn
import zen_utils


class zenHandler(BaseRequestHandler):
    def handle(self):
        zen_utils.handle_conversation(self.request, self.client_address)


class ZenServer(ThreadingMixIn, TCPServer):
    allow_reuse_address = 1
    # address_family = socket.AF_INET6 #  Раскоментируйте эту строку, если нужны IPv6


if __name__ == '__main__':
    address = zen_utils.parse_command_line('legacy "SocketServer" server')
    server = ZenServer(address, ZenServer)
    server.serve_forever()
# Код приведен для ознакомления с возможными реализациями, 
# но не рекомендуется для использования в проектах