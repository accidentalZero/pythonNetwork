#!/usr/bin/env python3
# Network Programming in Python: The Basics
# Асинхронный ввод-вывод осуществляется напрямую системным вызовом poll()

import select, zen_utils

def all_events_forever(poll_object):
    while True:
        for fd, event in poll_object.poll():
            yield fd, event


def serve(listener):
    sockets = {listener.fileno(): listener}
    address = {}
    bytes_received = {}
    bytes_to_send = {}

    poll_object = select.poll()
    poll_object.register(listener, select.POLLIN)

    for fd, event in all_events_forever(poll_object):
        sock = sockets[fd]

        # Сокет закрыт: удаляем его из структур данных
        if event & (select.POLLHUP | select.POLLERR | select.POLLNVAL):
            address = address.pop(sock)
            rb = bytes_received.pop(sock, b'')
            sb = bytes_to_send.pop(sock, b'')
            if rb:
                print('Client {} sent {} but then closed'.format(address, rb))
            elif sb:
                print('Client {} closed before we sent {}'.format(address, sb))
            else:
                print('Client {} closed socket normally'.format(address))
            poll_object.unregister(fd)
            del sockets[fd]
        
        # Новый сокет: добавляем его в структуры данных
        elif sock is listener:
            sock, address = sock.accept()
            print('Accepted connection from {}'.format(address))
            sock.setblocking(False) # Усилим socket.timeout, если мы ошибаемся
            sockets[sock.fileno()] = sock
            address[sock] = address
            poll_object.register(sock, select.POLLIN)
        
        # Входящие данные: продолжаем получать данные, пока не получим suffix
        elif event & select.POLLIN:
            more_data = sock.recv(4096)
            if not more_data:   # конец файла
                sock.close()    # следующий poll() выполнит POLLNVAL
                                # и тем самым произведет очистку
                continue
            data = bytes_received.pop(sock, b'') + more_data
            if data.endswith(b'?'):
                bytes_to_send[sock] = zen_utils.get_answer(data)
                poll_object.modify(sock, select.POLLOUT)
            else:
                bytes_received[sock] = data
            
        # Сокет готов к отправке: данные отправляются,
        # пока не будут доставлены все байты
        elif event & select.POLLOUT:
            data = bytes_to_send.pop(sock)
            n = sock.send(data)
            if n < len(data):
                bytes_to_send[sock] = data[n:]
            else:
                poll_object.modify(sock, select.POLLIN)


if __name__ == '__main__':
    address = zen_utils.parse_command_line('low-level async server')
    listener = zen_utils.create_srv_socket(address)
    serve(listener)
   