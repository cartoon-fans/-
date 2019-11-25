from socket import *
import struct

data = [(1, "Lily", 10, 78),
        (2, "tom", 6, 91),
        (3, "jame", 18, 80),
        (4, "abby", 11, 87),
        (5, "levi", 9, 76),

        ]

server_addr = ("127.0.0.1", 9526)
st = struct.Struct("i16sii")
sockfd = socket(AF_INET, SOCK_DGRAM)
for id, name, age, score in data:
    z = st.pack(id, name.encode(), age, score)
    sockfd.sendto(z, server_addr)
sockfd.close()
