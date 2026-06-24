import datetime
class packet:
    def __init__(self, source_ip : str, destination_ip : str, payload_size:int, protocol : str ):
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.payload_size = payload_size
        self.protocol = protocol
        self.timestamp = datetime.datetime.now()

    def get_risk_score(self):
        if self.payload_size > 2000:
            return 20
        return 0
    

class TCP_packet(packet):
    def __init(self, source_ip: str, destination_ip : str,  payload_size:int, dest_port:int, flags: str ):
        super().__init__( source_ip, destination_ip, payload_size, "TCP")
        self.dest_port = dest_port
        self.flags = flags

    def get_risk_score(self) -> int:
        score = super().get_risk_score()
        sensitive_ports = {22 : "SSH" , 21 : "FTP", 23 : "Telnet"}
        if self.dest_port in sensitive_ports:
            score+=40
            if self.payload_size > 3000:
                score+=45

        if self.flags == "SYN" and self.payload_size > 1000:
            score+=20

        return min(score, 100)
    
class UDP_packet(packet):
    def __init__(self, source_ip: str, destination_ip : str, payload_size:int, service: str):
        super.__init__( source_ip, destination_ip,  payload_size, )
        self.service = service

    def get_risk_Score(self)-> int:
        score = super().get_risk_score() 
        if self.service in ["NTP", "DNS"] and self.payload_size > 1024:
            score+=20
        return min(score, 100)
class NetworkScanner:
    """Manages collections of packets and extracts security/ML insights."""
    def __init__(self):
        # Python Data Type: LIST to store objects sequentially
        self.packet_log = []

    def add_packet(self, packet: packet):
        """Adds a packet object to the network log."""
        self.packet_log.append(packet)
        print(f"[LOG] Processed {packet.protocol} packet from {packet.source_ip}")

    def get_unique_ips(self) -> set:
        """Python Data Type: SET to filter out all duplicate IP addresses."""
        unique_ips = set()
        for packet in self.packet_log:
            unique_ips.add(packet.source_ip)
            unique_ips.add(packet.destination_ip)
        return unique_ips

    def get_protocol_distribution(self) -> dict:
        """Python Data Type: DICTIONARY to count protocol frequencies."""
        distribution = {"TCP": 0, "UDP": 0}
        for packet in self.packet_log:
            if packet.protocol in distribution:
                distribution[packet.protocol] += 1
        return distribution

    def check_for_threats(self):
        """Cybersecurity Logic: Scans logged packets for high-risk flags."""
        print("\n--- Running Threat Intelligence Audit ---")
        threats_found = False
        
        for packet in self.packet_log:
            risk = packet.get_risk_score()
            if risk >= 60:
                threats_found = True
                print(f"[ALERT] High Risk Packet Detected!")
                print(f"  Source IP: {packet.source_ip} -> Dest IP: {packet.destination_ip}")
                print(f"  Protocol:  {packet.protocol} | Risk Score: {risk}/100")
                
                # Dynamic info based on subclass type (Checking object type)
                if isinstance(packet, TCP_packet):
                    print(f"  Details:   Targeting Port {packet.dest_port} with flags '{packet.flags}'")
                elif isinstance(packet, UDP_packet):
                    print(f"  Details:   Targeting Service '{packet.service}'")
                print("-" * 40)
                
        if not threats_found:
            print("[INFO] No immediate high-risk threats detected.")

    def export_to_ml_format(self) -> list:
        """ML Bridge: Flattens complex OOP objects into numerical dictionaries for ML models."""
        ml_dataset = []
        for packet in self.packet_log:
            # Map categorical protocols to numbers (ML models only read numbers)
            is_tcp = 1 if packet.protocol == "TCP" else 0
            
            # Extract port if TCP, otherwise default to a placeholder (e.g., 53 for general UDP/DNS)
            port = packet.dest_port if isinstance(packet, TCP_packet) else 53
            
            feature_vector = {
                "payload_size": packet.payload_size,
                "is_tcp": is_tcp,
                "port": port,
                "risk_score": packet.get_risk_score()
            }
            ml_dataset.append(feature_vector)
        return ml_dataset


# ==========================================
# EXECUTION SIMULATION
# ==========================================

if __name__ == "__main__":
    # Initialize the scanner engine
    scanner = NetworkScanner()

    print("--- Simulating Network Traffic Ingestion ---")
    # 1. Normal web browsing packet
    p1 = TCP_packet(source_ip="192.168.1.50", destination_ip="10.0.0.1", payload_size=1500, dest_port=80, flags="ACK")
    
    # 2. Malicious: Massive data payload targeted at SSH (Port 22)
    p2 = TCP_packet(source_ip="185.220.101.5", destination_ip="10.0.0.1", payload_size=4500, dest_port=22, flags="SYN") 
    
    # 3. Normal DNS request
    p3 = UDP_packet(source_ip="192.168.1.50", destination_ip="8.8.8.8", payload_size=64, service="DNS")
    
    # 4. Suspect: Large payload on HTTPS port
    p4 = TCP_packet(source_ip="185.220.101.5", destination_ip="10.0.0.2", payload_size=2500, dest_port=443, flags="SYN")

    # Ingest the simulated traffic
    scanner.add_packet(p1)
    scanner.add_packet(p2)
    scanner.add_packet(p3)
    scanner.add_packet(p4)

    # Output Data Metrics
    print("\n--- Network Metrics ---")
    print(f"Protocol Distribution: {scanner.get_protocol_distribution()}")
    print(f"Unique Network IPs Discovered: {scanner.get_unique_ips()}")

    # Run the security logic
    scanner.check_for_threats()

    # Export data prepared for Machine Learning training
    print("\n--- Exporting Flattened Data for Machine Learning Models ---")
    ml_data = scanner.export_to_ml_format()
    
    # Pretty print the final dataset
    import json
    print(json.dumps(ml_data, indent=2))  


