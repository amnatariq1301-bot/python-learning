network_logs = [
    "user:amna -> traffic_port:443",
    "user:ali -> traffic_port:80",
    "user:usman -> traffic_port:22",     # Security alert!
    "user:aima -> traffic_port:443",
    "user:asif -> traffic_port:80",
    "user:zain -> traffic_port:22",      # Security alert!
    "user:raza -> traffic_port:INVALID", # Broken log entry
]

# https = 0
# http  = 0
# ssh = 0
print("\n--- Network Processing Logs ---")
for user in network_logs:
    parts = network_logs.split("->")
    username = parts[0].split(":")[1]
    trafiic_port = parts[1].split(":")[1]

print(f"Username : {username} accessed {trafiic_port} port")
    