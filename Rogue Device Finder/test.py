network_devices = [
    {"ip": "192.168.1.10", "login_attempts": 1, "data_mb": 45},
    {"ip": "192.168.1.15", "login_attempts": 2, "data_mb": 120},
    {"ip": "10.0.0.99", "login_attempts": 15, "data_mb": 5000},  # Suspicious!
    {"ip": "192.168.1.20", "login_attempts": 1, "data_mb": 10},
    {"ip": "185.220.10.5", "login_attempts": 8, "data_mb": 300}   # Suspicious!
]

normal_cluster = []
suspicous_cluster = []

for login, mb,ip in network_devices:
    if login > 5:
        suspicous_cluster.append()
        print("""Normal cluster""")
        print(f"{ip} [safe behaviour]")
    else:
        normal_cluster.append()
        print("""suspicous cluster""")
        print(f"{ip} high login attempts or massive download size")

    