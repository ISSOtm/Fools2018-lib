#!/usr/bin/python3
"""	
	Written by jfb1337
	Thanks to ISSOtm, Parzival, Niedzejkob, Riley/RoL, and TheZZAZZGlitch
"""

from Fools2018 import Connection, Packet, Map, set_fun_value, get_fun_value
from time import sleep
import os
import codecs
from os import mkdir
from urllib.request import HTTPError

dump_folder = "fun_dumps"
log_filename = "fun_event_log"
valid_maps = [
	0x0000,
	0x0001,
	0x0110,
	0x0210,
	0x0327,
	0x0364,
	0x043a,
	0x0523,
	0x0565,
	0x0566,
	0x062f,
	0x0667,
	0x0668,
	0x0669,
	0x066a,
	0x0734,
	0x0824,
	0x0932,
	0x096b,
	0x098a,
	0x0a32,
	0x0b2d,
	0x0c2c,
	0x0d3e,
	0x0e3c,
	0x0e6c,
	0x0f3b,
	0x103b,
	0x106d,
	0x113d,
	0x116e,
	0x123d,
	0x1321,
	0x1337,
	0x1432,
	0x146f,
	0x152d,
	0x1631,
	0x1639,
	0x1670,
	0x1671,
	0x1672,
	0x1720,
	0x1730,
	0x1731,
	0x1732,
	0x182a,
	0x1927,
	0x1a3c,
	0x1a73,
	0x1b37,
	0x1c2c,
	0x1d3b,
	0x1e33,
	0x1e92,
	0x1f3a,
	0x1f79,
	0x1f7a,
	0x202f,
	0x207b,
	0x2125,
	0x2174,
	0x223a,
	0x2275,
	0x2276,
	0x2277,
	0x232d,
	0x2435,
	0x2478,
	0x2536,
	0x2632,
	0x2725,
	0x2731,
	0x2791,
	0x2833,
	0x2939,
	0x2a31,
	0x2b29,
	0x2b7c,
	0x2b7d,
	0x2b7e,
	0x2c29,
	0x2d27,
	0x2e2b,
	0x2f38,
	0x2f7f,
	0x2f80,
	0x2f81,
	0x302c,
	0x3120,
	0x318b,
	0x318c,
	0x318d,
	0x318e,
	0x318f,
	0x323f,
	0x3336,
	0x3420,
	0x3482,
	0x353c,
	0x3621,
	0x3724,
	0x3828,
	0x3920,
	0x3a3e,
	0x3b22,
	0x3b30,
	0x3b31,
	0x3b32,
	0x3c36,
	0x3d20,
	0x3d83,
	0x3e31,
	0x3e90,
	0x3f3d,
	0x4026,
	0x412e,
	0x423a,
	0x432a,
	0x4384,
	0x4430,
	0x4528,
	0x4530,
	0x4585,
	0x4628,
	0x472b,
	0x4786,
	0x4787,
	0x4788,
	0x482b,
	0x4889,
	0x4933,
	0x4a34,
	0x4b3a,
	0x4c21,
	0x4c93,
	0x4d3a,
	0x4e22,
	0x4f21
]

fun_dumps = {}
num_seen_fun_vals = 0

try:
	mkdir(dump_folder)
except FileExistsError:
	pass
	
class RawMap:
	def __init__(self, data):
		self.raw_data = data
# at some point this script crashed due to not handling a ratelimit properly
# so I want to resume from existing data - don't want to have to make more requests than necassary
for dir in os.listdir(dump_folder):
	fun_val = int(dir)
	fun_dumps[fun_val]={}
	num_seen_fun_vals+=1
	for map in os.listdir("{}/{}".format(dump_folder, fun_val)):
		id = int(map[0:4], 16)
		map_file = open("{}/{}/{}".format(dump_folder, fun_val, map))
		line = ""
		dump=""
		while line != "Raw dump:":
			line=map_file.readline()[:-1]
		while line != "":
			line=map_file.readline()[:-1]
			dump+=line
		map_file.close()
		fun_dumps[fun_val][id] = RawMap(list(codecs.decode(dump,'hex_codec')))
		
print(num_seen_fun_vals)

log_file = open(log_filename, "a")

connection = Connection()
connection.get_token("WDGasterDump", "redacted")
fun_val = get_fun_value(connection)



def get_fresh_fun_val():
	global fun_val, fun_dumps, num_seen_fun_vals, connection
	attempts = 0
	while (fun_val in fun_dumps):
		fun_val = set_fun_value(connection)
		attempts+=1
		if attempts%4 == 0:
			print("Made {} of attempts at finding a fun value. Sleeping.".format(attempts))
			sleep(4)
	print("Found a new fun value after {} attempts: {}".format(attempts, fun_val))
	num_seen_fun_vals+=1
	return fun_val
	
def myhex(num):
	return hex(map_id)[2:].zfill(4)
	
#apparently fun value 255 doesn't exist - so this is 255 not 256
while num_seen_fun_vals < 255:
	get_fresh_fun_val()
	try:
		mkdir("{}/{}".format(dump_folder, fun_val))
	except FileExistsError:
		print("this directory shouldn't already exist...")
		pass
		
	print("Dumping maps for fun value {}".format(fun_val))
	fun_dumps[fun_val] = {}
	
	for map_id in valid_maps:
		print("Dumping map 0x{}".format(myhex(map_id)), end="")
		try:
			map = Map(map_id, connection)
		except HTTPError as error:
			print("Error while dumping map {} at fun val {}".format(myhex(map_id), fun_val))
				
		else:
			print(", {}".format(map.name))
			map_file = open("{}/{}/{}_{}.txt".format( dump_folder, fun_val, myhex(map_id), map.name ), "w")
			# Write the repr to the file (everything happens automatically o/)
			map_file.write(str(map))
			map_file.close()
			
			fun_dumps[fun_val][map_id] = map
			for val in fun_dumps:
				if (map_id in fun_dumps[val]):
					other_map = fun_dumps[val][map_id]
					if (other_map.raw_data != map.raw_data):
						msg = "Map 0x{} differs in fun values {} and {}".format(myhex(map_id), fun_val, val)
						
						log_file.write(msg+"\n")
						log_file.flush()
						print(msg)
	
		sleep(0.25)
		
log_file.close()
	

	



