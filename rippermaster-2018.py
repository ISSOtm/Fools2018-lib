"""
RipperMaster 2018

Version 0.1-GARBO
Data Ripper for TheZZAZZGlitch's April Fools 2018 challenge

Written by Parzival Wolfram

Thanks to NieDzejkob for helping me understand the checksumming process!

My first attempt at code that is actually annotated for
others to read. Trust me, i'm a bad enough coder that annotations are needed
for all but the most hardcore RE-literate techs to understand my code.

Variable-based packet format:
length + checksum + command_ID + maploop

Full, technical packet format:

Example packet: "0700a1a80407f5"

0700 - Length, little endian
a1 - Checksum One: All data bytes are added together, A5h is added, then everything's modulo 256 (or it wraps around to 00 after adding to an FF byte)
a8 - Checksum Two: All data bytes are XORed together, then 5A is XORed to the resultant byte
04 - Command byte: "server, I need this" - 04 is map data request, 03 is sync data, 77 is the one you need for Cavern 4.
07f5 - Data: The actual data. Nothing special. With command ID 04, this will be 2 bytes long, which will 
"""
length = "0700" # Length of the total packet, including these bytes. ALWAYS more than 5 as you need these bytes, the two checksums, and the command bytes.
command_ID = "04" # Command ID. Required for packet to be valid. 04 is to request map data.

import urllib2 # For requests to the server.
import time # For delay between requests (so as to not flood the server)

global maploop # Fucking loop variable access rules...
global outputhex
global failnum
failnum = 0 # For log purposes.
maploop = 0 # Used as loop controller and stores the next map to download.
logout = open("C:\\packets\\packets.log","w") # Hardcoded for debugging ease. Change per your preferences.
timestart = time.time() # Start total-time-this-shit-took timer.
while maploop <= 65535: # Start of the worst loop ever.
    checksum = "0000" # Variable init is important!
    outputhex = str(hex(maploop))[2:] # Strip the "0x" from the beginning of the hex number because that's some bullshit, Python.
    if len(outputhex) % 4 != 0: # THE MOST BULLSHIT HEX PADDING PROCESSING EVER!!!
        if len(outputhex) == 3: # You can clearly see that this is terrible, and this is also pretty self-explanatory code.
            outputhex = "0" + outputhex
        elif len(outputhex) == 2:
            outputhex = "00" + outputhex
        elif len(outputhex) == 1:
            outputhex = "000" + outputhex
    checksumone = str(hex((int(outputhex[:2],16)+int(outputhex[2:],16)+int("A5",16))% 256))[2:] # Generate Checksum One.
    checksumtwo = str(hex((int(outputhex[:2],16)^int(outputhex[2:],16))^int("5A",16)))[2:] # Generate Checksum Two.
    if len(checksumone) == 1: # MOAR TERRIBLE HEX PADDING!!!11!!1
            checksumone = "0" + checksumone
    if len(checksumtwo) == 1: # So how was your day?
            checksumtwo = "0" + checksumtwo
    checksum = checksumone + checksumtwo # So I don't have to type two variables instead of one later when I group four variables together for the same reason.
    packet = str(length + checksum + command_ID + outputhex) # Because i'm too lazy to copy-paste the big concat string throughout the script.
    time.sleep(0.1) # hey tails... gotta go slooooooooooooooooooow
    try: # this is lazy coding, plain and simple.
        headers = {'Accept-Identity': 'identity',  'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': ' Python-urllib/3.3', 'Host': '167.99.192.164:12709'} # Client ID, etc. Just stuff I pulled because it was needed and I wanted to look somewhat like the normal Fools2018 connection client.
        req = urllib2.Request('http://167.99.192.164:12709/req/f03c8789210012c8a1bed3201300dd283fb706806ed4d363396c03d389350eee264401a300074c59830e6d86a1b1127d4e1b80018f9972c8266a17216433a80e', packet.decode("hex").encode("base64"),headers) # Long userstring. Also, HAH, THIS IS FROM A TEST ACCOUNT! NO INFO FOR YOU!!!
        response = urllib2.urlopen(req) # i'm gonna be honest here: I pulled the urllib code from Stack Exchange. Also, this just connects to the URL above.
        map = response.read() # *yawn* this gets the server's response.
        pageout = open("C:\\packets\\"+packet,"w") # Hard-coded for debug purposes. Also, this saves the packet data to a file called what the outgoing packet is.
        pageout.write(map.decode("base64")) # this just writes the received data to the file.
        pageout.close() # I'm tired.
        print "Packet " + str(packet) + " - SUCCESS, written to file\n" # Log our success to the screen.
        logout.write("Packet " + str(packet) + " - SUCCESS, written to file\n") # Log our success to the log, too, because redundancy.
        logout.flush() # yup.
    except Exception as e: # LITERALLY GENERIC BULLSHIT.
        print "Packet " + str(packet) + " - FAIL, reason \"" + str(e) + "\"" # Print our fuckup to the screen...
        logout.write("Packet " + str(packet) + " failed to request with error \"" + str(e) + "\"\n") # then stick the fail in the log...
        logout.flush() # then write the log to disk...
        failnum = failnum + 1 # then increment the fail counter...
        pass # then stop giving a fuck.
    maploop = maploop + 1 # NEXT MAP!
    logout.flush() # less memory usage plzty.
timeend = time.time() # Stop total-time-this-shit-took timer.
logout.write("All requests completed in " + str(timeend-timestart) + " seconds.") # Tell the log how much time we wasted on this bullshit, then cry in the corner for a while.
logout.write("\nNumber of failed request attempts: " + str(failnum)) # GUESS HOW MANY TIMES WE FUCKED UP?
logout.close() # write the log to disk, then allow shit to modify it. It's older than 18 milliseconds, it's fair game. ;)




















# ok i'm tired now bye
