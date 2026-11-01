import socket
s = socket.create_connection(('127.0.0.1', 9800))
cmds = [
    'router_clear',
    'router_begin cc', 'router_end',
    'router_begin prog', 'router_end',
    'router_begin pbend', 'router_end',
    'router_begin note',
    'router_chan 0 0 1 0',
    'router_end'
]
for c in cmds:
    s.sendall((c + '\n').encode('utf-8'))
print('ROUTER CONFIG APPLIED')
