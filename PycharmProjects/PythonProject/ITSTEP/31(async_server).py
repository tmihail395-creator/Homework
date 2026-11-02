import asyncio
import socket

async def handle_client(reader,writer):
    address=writer.get_extra_info('peername')
    print("client connected:",address)

    data=await reader.recv(9999)

    print("client received:",data.decode())
    writer.write(data.encode())

    await writer.drain()

    writer.close()
    print("client closed")

async def main():
    server=await asyncio.start_server(handle_client,host='127.0.0.1',port=8888)
    print("server on {}".format(server.sockets[0].getsockname()))
    print("waiting for client")

    async with server:
        await server.serve_forever()