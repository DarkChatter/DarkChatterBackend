#
#
# Back End Testing


import sys
from scapy.all import *


def build_packet(x, interface):
    ip=IP("HelloWOrld")
    #sendp(ip , loop=1,inter=0.2,iface="wlp2s0");
    sendp(RadioTap()/
          Dot11(addr1="ff:ff:ff:ff:ff:ff",
                addr2="00:01:02:03:04:05",
                addr3="00:01:02:03:04:05")/
          Dot11Beacon(cap="ESS", timestamp=1)/
          Dot11Elt(ID="SSID", info=x)/                     
          Dot11Elt(ID="Rates", info='testthisfield')/
          Dot11Elt(ID="DSset", info="breakEverything")/
          Dot11Elt(ID="TIM", info="\x00\x01\x00\x00"),
          iface=interface, loop=1)
    #sendp("I'm travelling on Ethernet", loop=1, inter=0.2)
    
  
    

build_packet("HellomynameisRyan","wlp2s0mon")





