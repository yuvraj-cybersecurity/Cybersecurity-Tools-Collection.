from scapy.all import sniff, IP

def packet_callback(packet):
    # Check agar packet mein IP layer hai
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Captured Packet: {src_ip} -> {dst_ip}")

print("Sniffing network traffic... (Capture 10 packets)")
# 10 packets sniff karke stop ho jayega
sniff(filter="ip", prn=packet_callback, count=10)
print("Finished!")
