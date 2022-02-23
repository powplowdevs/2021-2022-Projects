import socket
import struct
import textwrap
import binascii

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5003

#MAIN FUNC
def main():
   s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

   while True:
      raw_data, addr = s.recvfrom(65536)
      dest_mac, src_mac, eth_proto, data = ETH_frame(raw_data)
      version, header_length, ttl, proto, src, target, data = ipv4_packet(raw_data)
      print("\n ETH FRAME: ")
      print('Dest: {}, Source {}, Protocal {}'.format(dest_mac, src_mac, eth_proto,))
      print('version: {}, header_length: {}, ttl: {}, proto: {}, ipv4: {}, ipv4: {}, data: {}'.format(version, header_length, ttl, proto, src, target, data))

#UNPACK ETH FRAME
def ETH_frame(data):
   #dest_mac: the data destination
   #src_mac: the data source or sender
   #proto: data type
   dest_mac, src_mac, proto = struct.unpack('! 6s 6s H',data[:14])
   #We use the get_mac_addr func cus the data return from the unacking of the data
   #in the line above is not in the normal mac addr format so we should make it more human readable
   return get_mac_addr(dest_mac),get_mac_addr(src_mac),socket.htons(proto), data[14:] #this is the rest of the data


#FORMAT MAC ADDR TO HUMAN READABLE MAC ADDR
def get_mac_addr(bytes_addr):
   bytes_str = map("{:02x}".format, bytes_addr)
   mac_addr = ":".join(bytes_str).upper()
   return mac_addr

#UNPACK IPV4 PACKET
def ipv4_packet(data):
   version_header_length = data[0]
   version = version_header_length >> 4
   header_length = (version_header_length & 15) * 4
   ttl, proto, src, target = struct.unpack("! 8x B B 2x 4s 4s", data[:20])
   return version, header_length, ttl, proto, ipv4(src), ipv4(target), data[header_length:]

#FORMAT IPV4
def ipv4(addr):
   return ".".join(map(str, addr))


main()

