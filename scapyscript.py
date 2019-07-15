from scapy.all import *

def check_GET(pcap_file):
    a = rdpcap(pcap_file)
    sessions = a.sessions()
    for session in sessions:
        for packet in sessions[session]:
            http_payload = ""

            try:

                http_payload += str(packet[TCP].payload)
                method = http_payload.find("GET",0,4)       #looks for GET in first 4 characters of the payload
                uri_check = http_payload.find("HTTP/1.1")   #find HTTP/1.1 in payload (function returns -1 if not found)
                if method !=-1 and uri_check == -1:         #logic to find GETs that do not use HTTP/1.1.
                    print(http_payload)

            except:
                pass

def main():
    pcap_file = raw_input("Enter the path to your pcap file here: ")
    print pcap_file
    check_GET(pcap_file)

main()
