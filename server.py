import socket, ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="certs/cert.pem", keyfile="certs/key.rsa")

ADDRESS = "127.0.0.1"
PORT = 10221

print(f"Listening on {ADDRESS}:{PORT}")

bindsocket = socket.socket()
bindsocket.bind((ADDRESS, PORT))
bindsocket.listen(5)

def handle(connstream: socket.socket | ssl.SSLSocket):
    _ = connstream.send("Hello World".encode())


while True:
    connstream, fromaddr = bindsocket.accept()
    try:
        connstream = context.wrap_socket(connstream, server_side=True)
        print(f"Connection received: {fromaddr}")
        handle(connstream)
        print(" -> data sent")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        try:
            connstream.shutdown(socket.SHUT_RDWR)
            connstream.close()
        except:
            continue
