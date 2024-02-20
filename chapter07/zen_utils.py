#!/usr/bin/env python3
# Network Programming in Python: The Basics
# Константы и программы для поддержания взаимодействия в сети

import argparse, socket, time

aphorisms = {b'Beautiful is better than?': b'Ugly.',
             b'Explicit is better than?': b'Implicit.',
             b'Simple is better than?': b'Complex.'}


def get_answer(aphorism):
    '''Возвращает ответ, чтобы продолжить афоризм из "Дзен Python"'''
    time.sleep(0.0) # Для имитации дорогостоящей операции
    return aphorisms.get(aphorism, b'Error: unknown aphorism.')


def parse_command_line(description):
    '''Анализирует командную строку и возвращает адрес сокета'''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    return address


def create_srv_socket(address):
    '''Создает и возвращает слушающий сокет сервера'''
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(address)
    listener.listen(64)
    print('Listening at {}'.format(address))
    return listener


def accept_connections_forever(listener):
    '''Неопределенное время отвечает на входящие соединения по слушающему сокету'''
    while True:
        sock, address = listener.accept()
        print('Accepted connection from {}'.format(address))
        handle_conversation(sock, address)


def handle_conversation(sock, address):
    '''Общается с клиентом через sock, пока разговор не будет окончен'''
    try:
        while True:
            handle_request(sock)
    except EOFError:
        print('Client socket to {} has closed'.format(address))
    except Exception as e:
        print('Client {} error: {}'.format(address, e))
    finally:
        sock.close()


def handle_request(sock):
    '''Получает один запрос клиента через sock и отправляет ответ'''
    aphorism = recv_until(sock, b'?')
    answer = get_answer(aphorism)
    sock.sendall(answer)


def recv_until(sock, suffix):
    '''Получает байты через sock, пока не поступит suffix'''
    message = sock.recv(4096)
    if not message:
        raise EOFError('socket closed')
    while not message.endswith(suffix):
        data = sock.recv(4096)
        if not data:
            raise IOError('received {!r} then socket closed'.format(message))
        message += data
    return message
