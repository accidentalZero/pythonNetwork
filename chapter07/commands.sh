 --- modulename: srv_single, funcname: <module>
0.00 srv_single.py(6): import zen_utils
 --- modulename: zen_utils, funcname: <module>
0.01 zen_utils.py(5): import argparse, socket, time
0.04 zen_utils.py(7): aphorisms = {b'Beautiful is better than?': b'Ugly.',
0.04 zen_utils.py(8):              b'Explicit is better than?': b'Implicit.',
0.04 zen_utils.py(9):              b'Simple is better than?': b'Complex.'}
0.04 zen_utils.py(7): aphorisms = {b'Beautiful is better than?': b'Ugly.',
0.04 zen_utils.py(12): def get_answer(aphorism):
0.04 zen_utils.py(18): def parse_command_line(description):
0.04 zen_utils.py(29): def create_srv_socket(address):
0.04 zen_utils.py(39): def accept_connections_forever(listener):
0.04 zen_utils.py(47): def handle_conversation(sock, address):
0.04 zen_utils.py(60): def handle_request(sock):
0.04 zen_utils.py(67): def recv_until(sock, suffix):
0.04 srv_single.py(9): if __name__ == '__main__':
0.04 srv_single.py(10):     address = zen_utils.parse_command_line('simple single-threaded server')
 --- modulename: zen_utils, funcname: parse_command_line
0.04 zen_utils.py(20):     parser = argparse.ArgumentParser(description=description)
0.04 zen_utils.py(21):     parser.add_argument('host', help='IP or hostname')
0.04 zen_utils.py(22):     parser.add_argument('-p', metavar='port', type=int, default=1060,
0.04 zen_utils.py(23):                         help='TCP port (default 1060)')
0.04 zen_utils.py(22):     parser.add_argument('-p', metavar='port', type=int, default=1060,
0.04 zen_utils.py(24):     args = parser.parse_args()
