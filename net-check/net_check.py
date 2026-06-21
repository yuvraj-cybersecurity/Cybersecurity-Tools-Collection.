import os

def check_network():
    print("--- Network Connectivity Tool ---")
    # Google DNS (8.8.8.8) ko ping karke connection check karna
    hostname = "8.8.8.8"
    response = os.system(f"ping -c 1 {hostname}")
    
    if response == 0:
        print("\nStatus: Network is UP and reachable.")
    else:
        print("\nStatus: Network is DOWN or Unreachable.")

if __name__ == "__main__":
    check_network()
