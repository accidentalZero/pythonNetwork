#!/usr/bin/env python3
# Network Programming in Python: The Basics
# Однопоточный сервер, который обслуживает по одному клиенту за раз,
# пока другие клиенты ждут

import zen_utils


if __name__ == '__main__':
    address = zen_utils.parse_command_line('simple single-threaded server')
    listener = zen_utils.create_srv_socket(address)
    zen_utils.accept_connections_forever(listener)
