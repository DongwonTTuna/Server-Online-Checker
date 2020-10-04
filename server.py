import asyncio

async def handle_echo(reader, writer):
    addr = writer.get_extra_info('peername')

    print(f"Connected with {addr!r}")

    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, '0.0.0.0', 'YOUR_PORT')

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())