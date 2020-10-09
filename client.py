import asyncio, time

try:
    f = open("onlined.txt", 'r')
    f.close()
except Exception:
    f = open("onlined.txt", 'w')
    f.write('1')
    f.close()

async def tcp_echo_client():
    with open("onlined.txt", 'r') as f:
        f = f.read()
    try:
        reader, writer = await asyncio.open_connection('YOUR_IP', 'YOUR_PORT')
        writer.close()
        if f == '0':
            print('Server onlined')
            with open("onlined.txt", 'w') as f:
                f.write('1')
    except ConnectionRefusedError or ConnectionResetError:
        if f == '1':
            print('Server offlined')
            with open("onlined.txt", 'w') as f:
                f.write('0')
        return


while True:
    try:
        asyncio.run(tcp_echo_client())
        time.sleep(5)
    except:
        pass