import socket, time

try:
    f = open("onlined.txt", 'r')
    f.close()
except Exception:
    f = open("onlined.txt", 'w')
    f.write('1')
    f.close()

def tcp_echo_client():
    with open("onlined.txt", 'r') as f:
        f = f.read()
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(2)
        client_socket.connect(('YOUR_ADDRESS', YOUR_PORT))
        if f.find('0') != -1:
            print('Server onlined')
            with open("onlined.txt", 'w') as f:
                f.write('1')
    except ConnectionRefusedError or ConnectionResetError or socket.timeout:
        if f.find('1') != -1:
            print('Server offlined')
            with open("onlined.txt", 'w') as f:
                f.write('0')


while True:
    try:
        tcp_echo_client()
        time.sleep(5)
    except:
        pass
