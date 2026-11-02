import socket

def main():
    host = "127.0.0.1"
    port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Сервер запущено на {host}:{port}. Очікування підключення...")

    conn, addr = server_socket.accept()
    print(f"Клієнт підключився: {addr}")

    try:
        while True:
            data = conn.recv(1024).decode("utf-8")
            if not data or data.lower() == "exit":
                print("Клієнт завершив з'єднання.")
                break
            print(f"Клієнт: {data}")

            message = input("Ви: ")
            conn.sendall(message.encode("utf-8"))
            if message.lower() == "exit":
                print("Ви завершили з'єднання.")
                break
    finally:
        conn.close()
        server_socket.close()
        print("Сокети закрито.")

if __name__ == "__main__":
    main()