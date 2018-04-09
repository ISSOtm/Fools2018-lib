#!/usr/bin/python3


import Fools2018
import time



ip = "167.99.192.164"
port = "12709"
token = "f03c8789210012c8a1bed3201300dd283fb706806ed4d363396c03d389350eee264401a300074c59830e6d86a1b1127d4e1b80018f9972c8266a17216433a80e"

connection = Fools2018.Connection(ip, port, token)


while True:
	draw = Fools2018.play_lottery(connection)
	print("[{}] Lottery draw: {} matches, letters are \"{}\"".format( time.strftime("%H:%M:%S"), draw[0], draw[1] ))
	time.sleep(3 * 3600) # Wait until next draw
