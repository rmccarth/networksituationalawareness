# networksituationalawareness
script files for NSA Assignment 6

requestparse.py offers 4 switches to specify the content that the user wants to examine from the requested URL. 
-h -> provided by default; help menu
-H -> return header
-c -> return response code
-b -> return response body

scapyscript.py will examine an entered pcap file (give it your full path to pcap) and will look for any packets in the capture which did not utilize an HTTP/1.1 tag inside a GET request. 

