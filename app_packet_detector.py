import pyshark
# Read the PCAP file
capture = pyshark.FileCapture('/home/kali/wireshark.pcapng')  #put your full .pcapng file here. #EDIT HERE
source_ip = '192.168.43.48'					#Put one of the IP here.  #EDIT here
destination_ip = '192.168.43.209'				#Put other IP here #Edit here
# Iterate over the packets

for packet in capture:
	if 'ARP' in  packet:
    		# Print the packet summary
		if packet.arp.src_proto_ipv4 == source_ip and packet.arp.dst_proto_ipv4 == destination_ip:
			arp_operation = packet.arp.get_field_value('arp.opcode')
			if arp_operation == '1':
				print ('\n\nThis is the ARP request: ')
				print(packet)
				break
			else:
				print('\n\nThis is not an ARP packet')
				break

for packet in capture:
	if 'ARP' in packet:
		if packet.arp.src_proto_ipv4 == destination_ip and packet.arp.dst_proto_ipv4 == source_ip:
			arp_operation = packet.arp.get_field_value('arp.opcode')
			if arp_operation == '2':
				print('\n\nThis is the corresponding ARP response')
				print(packet)
				break
			else:
				print('\n\nThis is not an ARP packet.')
				break
