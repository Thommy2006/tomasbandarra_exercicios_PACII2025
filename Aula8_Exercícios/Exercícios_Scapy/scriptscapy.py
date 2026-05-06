from scapy.all import ARP, Ether, srp, sniff

INTERFACE = "eth0" 
REDE = "192.168.1.0/24"

def analisa(pacote):
    print(pacote.summary())

print(f"Scan da Rede: {REDE}")
arp = ARP(pdst=REDE)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
pacote = ether/arp
respostas = srp(pacote, timeout=2, verbose=0)[0]

print("IP\t\tMAC")
for envio, recebido in respostas:
    print(f"{recebido.psrc}\t{recebido.hwsrc}")

print("Trafego:")
sniff(count=50, prn=analisa)