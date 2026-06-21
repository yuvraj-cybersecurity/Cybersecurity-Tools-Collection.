import psutil
import time

print("--- System Performance Monitor ---")
try:
    for i in range(5):  # 5 baar status dikhayega
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        print(f"Update {i+1}: CPU Usage: {cpu}% | RAM Usage: {mem}%")
        time.sleep(1)
    print("Monitoring Complete.")
except Exception as e:
    print(f"Error: {e}")
