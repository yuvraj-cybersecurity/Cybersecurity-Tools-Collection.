import datetime

def log_activity(action):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("system_logs.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] Action: {action}\n")
    print(f"Logged: {action}")

# Test usage
log_activity("System Scan Initiated")
log_activity("Network Traffic Analyzed")
