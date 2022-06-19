from scapy.all import  * 

network_packets = rdpcap('ping.pcapng')
with open("myresult_total.txt", "w") as binary_file:
    for packet in network_packets:
        if packet.type == 8 or packet[IP].src != '10.1.0.10' and packet.haslayer(ICMP):
            continue
        data_bytes = packet.load
        binary_file.write(chr(len(data_bytes)))