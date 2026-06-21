import socket

target = "127.0.0.1"

print("--- Scanning Target: 127.0.0.1 ---")

for port in range(20, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port}: OPEN")
    s.close()

print("--- Scan Finished ---")
