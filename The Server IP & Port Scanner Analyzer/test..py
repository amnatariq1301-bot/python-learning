network_dump = [
    {"ip": "192.168.1.1", "port": "80"},      # Keep (Port <= 1000)
    {"ip": "10.0.0.5", "port": "22"},         # Keep (Port <= 1000)
    {"ip": "172.16.0.2", "port": "8080"},     # Filter out (> 1000)
    {"ip": "192.168.1.50", "port": "MALFORMED"}, # Filter out (Invalid)
    {"ip": "10.0.0.12", "port": "443"}        # Keep (Port <= 1000)
]

print("\n --------ANALYZING PORTS---------")
for index, logs in enumerate(network_dump):
    print(f"Audit row {index}: Auditing ip {logs['ip']} ....")


print("\n --- High-Risk Target Inspection List ---")
def clean_port(port):
    try:
        return int(port)
    except ValueError:
        return -1
# The List Comprehension builds our final dictionary list in one line!
inspection_list = [
    {"ip": logs["ip"], "port": clean_port(logs["port"])} # Create a clean dictionary format
    for logs in network_dump                            # Loop through the records
    if clean_port(logs["port"]) != -1 and clean_port(logs["port"]) <= 1000 # Filter rules
]

print(inspection_list)



    
    
