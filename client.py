import socket, ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# require a certificate from the server
ssl_sock = context.wrap_socket(s, server_side=False)
ssl_sock.connect(("localhost", 10221))

print("Connected: reading")
print(ssl_sock.read().decode())

# note that closing the SSLSocket will also close the underlying socket
ssl_sock.close()
