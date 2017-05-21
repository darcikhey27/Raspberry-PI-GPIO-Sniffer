# pi_sniffer
## Raspberry pi GPIO - Python project
Project will be based on the observer pattern, PI will scan network traffic and report to the list of registerd observers.  
Observers will be notifed when a packet of interest is seen in the network.   
Observers will display a particular view either with stdout, python GPIO led lights, play a sound though a speaker, for example       "system.speak("telnet packet")"
  
## Network Utilities used for the project:   
* python scapy  
* tcpdump
* Raspberry PI GPIO  

### Observer pattern
