import pprint
raw_network_data = [
    {"ip": "192.168.1.10", "type": "Server", "alerts": "2"},
    {"ip": "10.0.0.45", "type": "Workstation", "alerts": "7"},      # High Alert!
    {"ip": "172.16.0.5", "type": "Gateway", "alerts": "CRIT_ERR"},   # Corrupted! Handle safely.
    {"ip": "192.168.1.15", "type": "Database", "alerts": "9"},     # High Alert!
    {"ip": "10.0.0.99", "type": "IoT Camera", "alerts": "0"}
]

class networkdevice():
    def __init__(self, ip_address, device_type, raw_alerts):
        self.ip_address = ip_address
        self.device_type = device_type
        try:
            self.alerts = int(raw_alerts)
        except ValueError:
            print(f"failed to parse alert count for {self.ip_address} defaulting to 0 alerts")
            self.alerts = 0

    def get_status(self):
        return(f"[{self.ip_address}] Type : {self.device_type} | Alerts: {self.alerts}")
    
print("\n--- Phase 1 & 2: Initializing Device Registry ---")
device_pool = []
for index, data in enumerate(raw_network_data, start=1):
    new_device = networkdevice(
        ip_address=data["ip"],
        device_type=data["type"],
        raw_alerts=data["alerts"],
    )
    device_pool.append(new_device)
    print(f"Device #{index} registered -> {new_device.get_status()}")

determine_action = lambda alert_count: "QUARANTINE" if alert_count >=5 else "CLEAN"

quarantine_board = [
    {
        "ip": device.ip_address,
        "status": determine_action(device.alerts),
        "total_alerts": device.alerts
    }
    for device in device_pool
    if determine_action(device.alerts) == "QUARANTINE"
]

print("\n--- Phase 3: Active Quarantine Board ---")
pprint.pprint(quarantine_board, sort_dicts=False)
