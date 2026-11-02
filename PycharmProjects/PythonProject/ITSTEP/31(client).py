import asyncio
import sys


async def listen(reader):
    try:
        while True:
            data = await reader.read(100)
            if not data:
                print("\nDisconnected from server.")
                break
            sys.stdout.write(f"\r{data.decode()}\n> ")
            sys.stdout.flush()
    except asyncio.CancelledError:
        pass


async def send(writer):
    try:
        while True:
            message = await asyncio.to_thread(input, "> ")
            if not message.strip():
                continue
            writer.write(message.encode())
            await writer.drain()
    except (asyncio.CancelledError, ConnectionError):
        pass


async def main():
    try:
        reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
        print("Connected! Type message and press Enter.")
        sys.stdout.write("> ")
        sys.stdout.flush()

        listen_task = asyncio.create_task(listen(reader))
        send_task = asyncio.create_task(send(writer))

        await asyncio.gather(listen_task, send_task)
    except ConnectionRefusedError:
        print("Server is offline.")
    finally:
        if 'writer' in locals():
            writer.close()
            try:
                await writer.wait_closed()
            except ConnectionError:
                pass


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\nExit.")


