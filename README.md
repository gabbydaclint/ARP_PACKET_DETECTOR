#This program analyse the pcap trace for an ARP packet. It receives the ".pcapng" file (A packet capture file via wireshark.)
# To run the program, pyshark need to be installed. You can install that by running "pip install pyshark".

#What it does.
#1.) It determines if a PACKET is an ARP packet or not.
#2.) If it does, the it process it further to print out the ARP header. (i.e hardware type, protocol type, mac address e.t.c)
#3.) It can also prints out the ARP requests and response between 2 host, you will need to supply the IP.

#How to run the program

#===> To install the program all you need to do is to
# 1.) specify the path to your ".pcapng" file. You should try specifying the absolute file path.
# 2.) specify both the source ip  and  destination ip.

#How it work:

# The reads a PCAP file (wireshark.pcapng) using the FileCapture class from pyshark, then it takes the source and destination ip, then it checks if it contains the ARP layer, if it does then it does the filtering based on the specified source and destination IP, then it checks if the opcade value is sent to one and print out the corresponding ARP request details. If not it print out that it isn't an ARP request and break out of the loop. 
# It then check again if the if the source and destination IP addresses match the reversed order, If the conditions are met, it extracts the ARP operation code and checks if it is '2', indicating an ARP response. If the ARP operation code is '2', it prints the message "This is the corresponding ARP response" along with the packet details.If the ARP operation code is not '2', it prints the message "This is not an ARP packet" and breaks out of the loop.


#In suummary, the code essentially captures ARP packets from the PCAP file and filters them based on the specified source and destination IP addresses. It then prints the ARP request and the corresponding ARP response packets, if present, along with their details.





