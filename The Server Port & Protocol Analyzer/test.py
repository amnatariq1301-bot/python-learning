network_logs = [
    "user:amna -> traffic_port:443",
    "user:ali -> traffic_port:80",
    "user:usman -> traffic_port:22",     # Security alert!
    "user:aima -> traffic_port:443",
    "user:asif -> traffic_port:80",
    "user:zain -> traffic_port:22",      # Security alert!
    "user:raza -> traffic_port:INVALID", # Broken log entry
]

# Initialize your protocol counters
https = 0
http  = 0
ssh   = 0

print("\n--- Network Processing Logs ---")

# We only need one loop to handle everything step-by-step
for log in network_logs:
    # 1. Split the current log string safely
    parts = log.split(" -> ")
    username = parts[0].split(":")[1]
    raw_port = parts[1].split(":")[1]

    # 2. Try converting the extracted string port to an integer
    try:
        valid_port = int(raw_port)
        
        # 3. Apply your protocol conditional rules and update counters
        if valid_port == 22:
            print(f"[ALERT] {username} tried to access sensitive traffic on port {valid_port}!")
            ssh += 1
        elif valid_port == 80:
            print(f"[SAFE] {username} accessed HTTP traffic on port {valid_port}")
            http += 1
        elif valid_port == 443:
            print(f"[SAFE] {username} accessed HTTPS traffic on port {valid_port}")
            https += 1
        else:
            print(f"[INFO] {username} accessed an unknown port: {valid_port}")
            
    except ValueError:
        # 4. Fill in your empty except block to handle "INVALID" safely
        print(f"[ERROR] Failed to parse port data for {username} (Invalid data: '{raw_port}')")

# 5. Print the final frequency dictionary summary at the very end
print("\n--- Protocol Frequency Summary ---")
protocol_summary = {
    "HTTPS": https,
    "HTTP": http,
    "SSH": ssh
}
print(protocol_summary)