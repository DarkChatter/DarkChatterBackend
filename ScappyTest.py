#
#
# Back End Testing


import sys
from scapy.all import *


def build_packet(x):
    target="www.google.com"
    ip=IP(dst=target)                  # Packets will be filled with default info 
    print(Net('www.google.com'))       # If you dont specify 
    sendp(ip , loop=1,inter=0.2);
    
    #sendp("I'm travelling on Ethernet", loop=1, inter=0.2)
    
  
    

build_packet("x")





