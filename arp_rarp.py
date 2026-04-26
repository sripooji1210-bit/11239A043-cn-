class ARP_RARP:
    def __init__(self):
        # IP → MAC
        self.arp = {
            "192.168.1.1": "AA:BB:CC:DD:01",
            "192.168.1.2": "AA:BB:CC:DD:02"
        }

        # MAC → IP (reverse)
        self.rarp = {v: k for k, v in self.arp.items()}

    def arp_request(self, ip):
        print("ARP:", ip, "→", self.arp.get(ip, "Not Found"))

    def rarp_request(self, mac):
        print("RARP:", mac, "→", self.rarp.get(mac, "Not Found"))


# Run
sim = ARP_RARP()

sim.arp_request("192.168.1.1")
sim.arp_request("192.168.1.10")

sim.rarp_request("AA:BB:CC:DD:01")
sim.rarp_request("AA:BB:CC:DD:99")