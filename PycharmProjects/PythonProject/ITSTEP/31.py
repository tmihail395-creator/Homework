import asyncio

clients = set()


async def handle_client(reader, writer):
    address = writer.get_extra_info('peername')
    print('Client connected from {}'.format(address))
    clients.add(writer)

    try:
        while True:
            data = await reader.read(100)
            if not data:
                break
            print('Received:', data.decode().strip())

            for client in clients:
                if client != writer:
                    client.write(data)
                    await client.drain()
    except ConnectionError:
        pass
    finally:
        clients.discard(writer)
        writer.close()
        await writer.wait_closed()
        print('Client closed', address)


async def main():
    server = await asyncio.start_server(handle_client, host='127.0.0.1', port=8888)
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    print("waiting for a connection")
    async with server:
        await server.serve_forever()


asyncio.run(main())




