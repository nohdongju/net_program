import struct
import socket
import binascii

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        #4개의 필드를 네트워크 바이트 순서(빅엔디안)로 2바이트씩 패킹
        return struct.pack('!HHHH', self.src_port, self.dst_port, self.length, self.checksum) 

def unpack_Udphdr(buffer):
    return struct.unpack('!HHHH', buffer[:8])

def getSrcPort(udp_unpack):
    return udp_unpack[0]

def getDstPort(udp_unpack):
    return udp_unpack[1]

def getLength(udp_unpack):
    return udp_unpack[2]

def getChecksum(udp_unpack):
    return udp_unpack[3]


udp = Udphdr(5555, 80, 1000, 0xFFFF)

packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr).decode())

unpacked = unpack_Udphdr(packed_udphdr)
print(f"({getSrcPort(unpacked)},{getDstPort(unpacked)},{getLength(unpacked)},{getChecksum(unpacked)})")
print(f"Source Port:{getSrcPort(unpacked)} Destination port:{getDstPort(unpacked)} Length:{getLength(unpacked)} Checksum:{getChecksum(unpacked)}")
