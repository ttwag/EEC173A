# Wireshark Lab 2

1. What is the IP address of the client?

    **The IP address of the client is 192.168.1.100**

2. The client actually communicates with several different Google servers in order to implement “safe browsing.” (See extra credit section at the end of this lab). The main Google server that will serve up the main Google web page has IP address 64.233.169.104. In order to display only those frames containing HTTP messages that are sent to/from this Google, server, enter the expression “http && ip.addr == 64.233.169.104” (without quotes) into the Filter: field in Wireshark .

    ![Figure1](./image/Figure1.png)

3. Consider now the HTTP GET sent from the client to the Google server (whose IP address is IP address 64.233.169.104) at time 7.109267. What are the source and destination IP addresses and TCP source and destination ports on the IP datagram carrying this HTTP GET?

    **Source IP: 192.168.1.100**
    
    **Source Port: 4335**

    **Destination IP: 64.233.169.104**
    
    **Destination Port: 80**

    ![Figure2](./image/Figure2.png)


4. At what time is the corresponding 200 OK HTTP message received from the Google server? What are the source and destination IP addresses and TCP source and destination ports on the IP datagram carrying this HTTP 200 OK message? 

    **Time: 7.158797**

    **Source IP: 64.233.169.104**

    **Destination IP: 192.168.1.100**

    **Source Port: 80**

    **Destination Port: 4335**

    ![Figure3](./image/Figure3.png)

5. Recall that before a GET command can be sent to an HTTP server, TCP must first set up a connection using the three-way SYN/ACK handshake. At what time is the client-to-server TCP SYN segment sent that sets up the connection used by the GET sent at time 7.109267? What are the source and destination IP addresses and source and destination ports for the TCP SYN segment? What are the source and destination IP addresses and source and destination ports of the ACK sent in response to the SYN. At what time is this ACK received at the client? (Note: to find these segments you will need to clear the Filter expression you entered above in step 2. If you enter the filter “tcp”, only TCP segments will be displayed by Wireshark).

    ### TCP SYN
    **Time: 7.075657**

    **Source IP: 192.168.1.100**

    **Source Port: 4335**

    **Destination IP: 64.233.169.104**

    **Destination Port: 80**

    ### TCP ACK
    **Source IP: 64.233.169.104**

    **Source Port: 80**

    **Destination IP: 192.168.1.100**

    **Destination Port: 4335**

    ![Figure4](./image/Figure4.png)

6. In the NAT_ISP_side trace file, find the HTTP GET message was sent from the client to the Google server at time 7.109267 (where t=7.109267 is time at which this was sent as recorded in the NAT_home_side trace file). At what time does this message appear in the NAT_ISP_side trace file? What are the source and destination IP addresses and TCP source and destination ports on the IP datagram carrying this HTTP GET (as recording in the NAT_ISP_side trace file)? Which of these fields are the same, and which are different, than in your answer to question 3 above?

    **Time: 6.069168**

    **Source IP: 71.192.34.104**

    **Source Port: 4335**

    **Destination IP: 64.233.169.104**

    **Destination Port: 80**

    The Time and Source IP are different, and the rest is the same.

    ![Figure5](./image/Figure5.png)

7. Are any fields in the HTTP GET message changed? Which of the following fields in the IP datagram carrying the HTTP GET are changed: Version, Header Length, Flags, Checksum. If any of these fields have changed, give a reason (in one sentence) stating why this field needed to change.

    **The Checksum has changed. It could be due to the NAT Translation difference.**


8. In the NAT_ISP_side trace file, at what time is the first 200 OK HTTP message received from the Google server? What are the source and destination IP addresses and TCP source and destination ports on the IP datagram carrying this HTTP 200 OK message? Which of these fields are the same, and which are different than your answer to question 4 above?

    **Time: 6.117570**
    
    **Source IP: 64.233.169.104**

    **Destination IP: 71.192.34.104**

    **Source Port: 80**

    **Destination Port: 4335**

    Only the time and Destination IP has changed


9. In the NAT_ISP_side trace file, at what time were the client-to-server TCP SYN segment and the server-to-client TCP ACK segment corresponding to the segments in question 5 above captured? What are the source and destination IP addresses and source and destination ports for these two segments? Which of these fields are the same, and which are different than your answer to question 5 above?

    
    ### TCP SYN
    **Time: 6.035475**

    **Source IP: 71.192.34.104**

    **Source Port: 4335**

    **Destination IP: 64.233.169.104**

    **Destination Port: 80**

    ### TCP ACK
    **Source IP: 64.233.169.104**

    **Source Port: 80**

    **Destination IP: 71.192.34.104**

    **Destination Port: 4335**
