#!/usr/bin/python3


"""
	TheZZAZZGlitch April Fools 2018 server communication lib
	
	Written by ISSOtm
	Thanks to Parzival, Niedzejkob, Riley/RoL, and TheZZAZZGlitch
	
	
	You are allowed to re-use and modify this module if you credit the people mentioned in this header.
"""


from urllib import request
import codecs
import json


Poke_chars = [
	"<char 0x0>", "<char 0x1>", "<char 0x2>", "<char 0x3>", "<char 0x4>", "<char 0x5>", "<char 0x6>", "<char 0x7>", "<char 0x8>", "<char 0x9>", "<char 0xa>", "<char 0xb>", "<char 0xc>", "<char 0xd>", "<char 0xe>", "<char 0xf>",
	"<char 0x10>", "<char 0x11>", "<char 0x12>", "<char 0x13>", "<char 0x14>", "<char 0x15>", "<char 0x16>", "<char 0x17>", "<char 0x18>", "<char 0x19>", "<char 0x1a>", "<char 0x1b>", "<char 0x1c>", "<char 0x1d>", "<char 0x1e>", "<char 0x1f>",
	"<char 0x20>", "<char 0x21>", "<char 0x22>", "<char 0x23>", "<char 0x24>", "<char 0x25>", "<char 0x26>", "<char 0x27>", "<char 0x28>", "<char 0x29>", "<char 0x2a>", "<char 0x2b>", "<char 0x2c>", "<char 0x2d>", "<char 0x2e>", "<char 0x2f>",
	"<char 0x30>", "<char 0x31>", "<char 0x32>", "<char 0x33>", "<char 0x34>", "<char 0x35>", "<char 0x36>", "<char 0x37>", "<char 0x38>", "<char 0x39>", "<char 0x3a>", "<char 0x3b>", "<char 0x3c>", "<char 0x3d>", "<char 0x3e>", "<char 0x3f>",
	"<char 0x40>", "<char 0x41>", "<char 0x42>", "<char 0x43>", "<char 0x44>", "<char 0x45>", "<char 0x46>", "<char 0x47>", "<char 0x48>", "<char 0x49>", "<char 0x4a>", "<char 0x4b>", "<char 0x4c>", "<char 0x4d>", "<char 0x4e>", "<char 0x4f>",
	"<NUL>", "<char 0x51>", "<char 0x52>", "<char 0x53>", "<char 0x54>", "<char 0x55>", "<char 0x56>", "<char 0x57>", "<char 0x58>", "<char 0x59>", "<char 0x5a>", "<char 0x5b>", "<char 0x5c>", "<char 0x5d>", "<char 0x5e>", "<char 0x5f>",
	"<char 0x60>", "<char 0x61>", "<char 0x62>", "<char 0x63>", "<char 0x64>", "<char 0x65>", "<char 0x66>", "<char 0x67>", "<char 0x68>", "<char 0x69>", "<char 0x6a>", "<char 0x6b>", "<char 0x6c>", "<char 0x6d>", "<char 0x6e>", "<char 0x6f>",
	"<char 0x70>", "<char 0x71>", "<char 0x72>", "<char 0x73>", "<char 0x74>", "<char 0x75>", "<char 0x76>", "<char 0x77>", "<char 0x78>", "<char 0x79>", "<char 0x7a>", "<char 0x7b>", "<char 0x7c>", "<char 0x7d>", "<char 0x7e>", " ",
	"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
	"Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "(", ")", ":", ";", "[", "]",
	"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
	"q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "é", "<'d>", "<'l>", "<'s>", "<'t>", "<'v>",
	"<char 0xc0>", "<char 0xc1>", "<char 0xc2>", "<char 0xc3>", "<char 0xc4>", "<char 0xc5>", "<char 0xc6>", "<char 0xc7>", "<char 0xc8>", "<char 0xc9>", "<char 0xca>", "<char 0xcb>", "<char 0xcc>", "<char 0xcd>", "<char 0xce>", "<char 0xcf>",
	"<char 0xd0>", "<char 0xd1>", "<char 0xd2>", "<char 0xd3>", "<char 0xd4>", "<char 0xd5>", "<char 0xd6>", "<char 0xd7>", "<char 0xd8>", "<char 0xd9>", "<char 0xda>", "<char 0xdb>", "<char 0xdc>", "<char 0xdd>", "<char 0xde>", "<char 0xdf>",
	"'", "<Pk>", "<Mn>", "-", "<'r>", "<'m>", "?", "!", ".", "<char 0xe9>", "<char 0xea>", "<char 0xeb>", "<empty cursor>", "<full cursor>", "<down arrow>", "<male symbol>",
	"$", "<mult>", "<. (duplicate)>", "/", ",", "<male symbol>", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

def Pokeify(str):
	return encode_str(str, Poke_chars)

def DePokeify(bytes):
	return decode_str(bytes, Poke_chars)


ZZAZZ_chars = [
	"<NUL>", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
	"P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", 
	"f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
	"v", "w", "x", "y", "z", "!", ",", "?", "\"", "-", ".", ":", "(", ")", " ", "< 0x3F>",
	"$", "'", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "é", "<Deliria A>", "<Deliria B>",
	"<Deliria C>", "<Deliria D>", "<Deliria E>", "<Deliria F>", "<Deliria G>", "<Deliria H>", "<Deliria I>", "<Deliria J>", "<Deliria K>", 	"<Deliria L>", "<Deliria M>", "<Deliria N>", "<Deliria O>", "<Deliria P>", "<Deliria Q>", "<Deliria R>",
	"<Deliria S>", "<Deliria T>", "<Deliria U>", "<Deliria V>", "<Deliria W>", "<Deliria X>", "<Deliria Y>", "<Deliria Z>", "<Deliria a>", 	"<Deliria b>", "<Deliria c>", "<Deliria d>", "<Deliria e>", "<Deliria f>", "<Deliria g>", "<Deliria h>",
	"<Deliria i>", "<Deliria j>", "<Deliria k>", "<Deliria l>", "<Deliria m>", "<Deliria n>", "<Deliria o>", "<Deliria p>", "<Deliria q>", 	"<Deliria r>", "<Deliria s>", "<Deliria t>", "<Deliria u>", "<Deliria v>", "<Deliria w>", "<Deliria x>",
	"<Deliria y>", "<Deliria z>", "<Deliria !>", "<Deliria ?>", "<Deliria *>", "<Deliria .>", "<Deliria :>", "<Deliria (>", "<Deliria )>", "<Deliria shrink.>", "<Deliria shrink!>", "<Deliria shrink?>", "<char 0x8b>", "<char 0x8c>", "<Braille A>", "<Braille B>", "<Braille C>",
	"<Braille D>", "<Braille E>", "<Braille F>", "<Braille G>", "<Braille H>", "<Braille I>", "<Braille J>", "<Braille K>", "<Braille L>", "<Braille M>", "<Braille N>", "<Braille O>", "<Braille P>", "<Braille Q>", "<Braille R>", "<Braille S>",
	"<Braille T>", "<Braille U>", "<Braille V>", "<Braille W>", "<Braille X>", "<Braille Y>", "<Braille Z>", "<char 0xa7>", "<char 0xa8>", "<char 0xa9>", "<char 0xaa>", "<char 0xab>", "<char 0xac>", "<char 0xad>", "<char 0xae>", "<char 0xaf>",
	"<char 0xb0>", "<char 0xb1>", "<char 0xb2>", "<char 0xb3>", "<char 0xb4>", "<char 0xb5>", "<char 0xb6>", "<char 0xb7>", "<char 0xb8>", "<char 0xb9>", "<char 0xba>", "<char 0xbb>", "<char 0xbc>", "<char 0xbd>", "<char 0xbe>", "<char 0xbf>",
	"<char 0xc0>", "<char 0xc1>", "<char 0xc2>", "<char 0xc3>", "<char 0xc4>", "<char 0xc5>", "<char 0xc6>", "<char 0xc7>", "<char 0xc8>", "<char 0xc9>", "<char 0xca>", "<char 0xcb>", "<char 0xcc>", "<char 0xcd>", "<char 0xce>", "<char 0xcf>",
	"<char 0xd0>", "<char 0xd1>", "<char 0xd2>", "<char 0xd3>", "<char 0xd4>", "<char 0xd5>", "<char 0xd6>", "<char 0xd7>", "<char 0xd8>", "<char 0xd9>", "<char 0xda>", "<char 0xdb>", "<char 0xdc>", "<char 0xdd>", "<char 0xde>", "<char 0xdf>",
	"<char 0xe0>", "<char 0xe1>", "<char 0xe2>", "<char 0xe3>", "<char 0xe4>", "<char 0xe5>", "<char 0xe6>", "<char 0xe7>", "<char 0xe8>", "<char 0xe9>", "<char 0xea>", "<char 0xeb>", "<char 0xec>", "<char 0xed>", "<char 0xee>", "<char 0xef>",
	"<char 0xf0>", "<control char 0xf1 NEXTPAGE>", "<control char 0xf2 SECONDLINE>", "<control char 0xf3 WAITBUTTONCLEAR>",
	"<control char 0xf4 WAITBUTTON>", "<control char 0xf5 CALLSUBSTR>", "<control char 0xf6 RETSUBSTR>", "<control char 0xf7 SETFONT>", "<control char 0xf8 PLAYSFX>", "<char 0xf9>", "<char 0xfa>", "<char 0xfb>", "<char 0xfc>", "<char 0xfd>", "<char 0xfe>", "<char 0xff>"
]

def ZZAZZify(str):
	return encode_str(str, ZZAZZ_chars)

def DeZZAZZify(bytes):
	return decode_str(bytes, ZZAZZ_chars)


def encode_str(str, char_list):
	byte_list = []
	
	for char in str:
		byte_list.append(char_list.index(char))
	
	return bytes(byte_list)

def decode_str(bytes, char_list):
	str = ""
	
	for byte in bytes:
		str += char_list[byte]
	
	return str



class Packet:
	
	TYPE_PING     = 0x01
	TYPE_MAP_NAME = 0x03
	TYPE_MAP      = 0x04
	TYPE_TREND    = 0x06
	TYPE_LOTTERY  = 0x07
	TYPE_THERAPY  = 0x0A
	TYPE_CAVERN4  = 0x77
	
	
	def __init__(self, type = 0, data = []):
		self.set_type(type)
		# Set data and length
		self.set_data(data)
		self.write_checksum()
	
	def from_bytes(bytes):
		packet = Packet(bytes[4], list(bytes[5:]))
		packet.checksum = (bytes[2], bytes[3])
		
		return packet
	
	def map_name_packet(map_id):
		return Packet(Packet.TYPE_MAP_NAME, [0] + [0xFF] * 0x28 + [map_id % 0x100, map_id // 0x100])
	
	def map_packet(map_id):
		return Packet(Packet.TYPE_MAP, [map_id // 0x100, map_id % 0x100])
	
	def trend_packet(trend_str):
		# The packet must be 0x15 bytes in length
		return Packet(Packet.TYPE_TREND, ZZAZZify( trend_str + "f" * ( 16 - len(trend_str)) ))
	
	def lottery_packet():
		return Packet(Packet.TYPE_LOTTERY, [0xFF])
		
	def therapy_packet():
		return Packet(Packet.TYPE_THERAPY, [0xFF])
	
	def cavern4_packet():
		return Packet(Packet.TYPE_CAVERN4, [0x13, 0x37, 0xCC])
	
	
	def __repr__(self):
		return "Length: {}\nType: {}\nData: {}".format(self.length, self.type, ",".join([hex(byte) for byte in self.data]))
	
	def __str__(self):
		return ",".join([hex(byte) for byte in self.get_bytes()])
	
	
	def __len__(self):
		return self.length
	
	def get_data(self):
		return self.data
	
	def get_type(self):
		return self.type
	
	
	def set_data(self, data):
		if len(data) > 0xFFFF:
			raise ValueError("Packet too large! (at most 0xFFFF bytes long, header included)")
		
		self.data = data
		self.length = len(self.data) + 5 # Include header size
	
	def set_type(self, type):
		assert type >= 0 and type < 0x100, "Type must be an unsigned byte"
		
		self.type = type
	
	
	def calc_checksum(self):
		checksum1 = 0xa5 # e
		checksum2 = 0x5a # d
		
		for byte in self.data:
			checksum1 += byte
			checksum2 ^= byte
		
		return (checksum1 & 0xFF),checksum2
	
	def write_checksum(self):
		self.checksum = self.calc_checksum()
	
	def verify_checksum(self):
		return self.checksum == self.calc_checksum()
	
	
	def get_bytes(self):
		raw_bytes = []
		
		# Length
		raw_bytes.append(self.length  % 0x100)
		raw_bytes.append(self.length // 0x100)
		
		# Checksum
		raw_bytes.append(self.checksum[0])
		raw_bytes.append(self.checksum[1])
		
		# Type
		raw_bytes.append(self.type)
		
		# Data
		raw_bytes.extend(self.data)
		
		return bytes(raw_bytes)


class Connection:
	
	def __init__(self, ip="167.99.192.164", port="12709", token = ""):
		self.ip = ip
		self.port = port
		self.token = token
	
	
	def request(self, path, data):
		if (isinstance(data, str)):
			data = bytes(data, "utf8")
		headers = {'Accept-Identity': 'identity',  'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': ' Python-urllib/3.5', 'Host': "{}:{}".format(self.ip, self.port)}
		req = request.Request("http://{}:{}".format(self.ip, self.port) + path, data, headers)
		return req
	
	def register_account(self, username, password, message):
		self.request("/api/register", "username={}&password={}&message={}".format(username, password, message))
	
	# FIXME: Check if this request returns the token and nothing else
	def get_token(self, username, password):
		req = self.request("/api/relogin", "username={}&password={}".format(username, password))
		response = request.urlopen(req).read().decode("utf8")
		token = json.loads(response)['sessid']
		self.token = token
		return token
	
	def send_packet(self, packet, retry_if_503 = True):
		packet.write_checksum()
		
		req = self.request("/req/" + self.token, codecs.encode(packet.get_bytes(), "base64")[:-1]) # strip trailing newline
		
		try:
			response = request.urlopen(req)
		except request.HTTPError as error:
			code = error.getcode()
			
			# The server rejects requests sent too quickly ; if it happens, hold on for a bit, then try again
			if code == 503 and retry_if_503:
				print("Might've hit rate limiter. Trying again in 5 seconds.")
				sleep(5)
				self.send_packet(packet, False)
			
			else:
				raise
		
		return Packet.from_bytes( codecs.decode(response.read(), "base64") )



class Map:
	
	def __init__(self, map_id, connection):
		map_name_packet = connection.send_packet( Packet.map_name_packet(map_id) )
		map_packet = connection.send_packet( Packet.map_packet(map_id) )
		
		raw_name_data = map_name_packet.get_data()
		raw_name = []
		i = 0
		while raw_name_data[i] != 0x50:
			raw_name.append(raw_name_data[i])
			i += 1
		self.name = DePokeify(raw_name)
		
		self.raw_data = map_packet.get_data()
		ptr = 0xB800
		def get_byte():
			nonlocal ptr
			ptr += 1
			return self.raw_data[ptr - 0xB801]
		
		def get_ptr():
			return get_byte() + get_byte() * 256
		
		def get_bytes(size):
			nonlocal ptr
			data = self.get_data_at(ptr, size)
			ptr += size
			return data
		
		self.tilesetID = get_byte()
		self.height = get_byte()
		self.width = get_byte()
		self.map_data_ptr = get_ptr()
		self.map_text_ptr = get_ptr()
		self.map_script_ptr = get_ptr()
		self.connections = get_byte()
		self.obj_data_ptr = get_ptr()
		self.loading_script_ptr = get_ptr()
		self.setup_ptr = get_ptr()
		ptr += 1
		self.musicID = get_byte()
		self.music_bank = get_byte()
		self.warp_list = []
		for i in range(4):
			self.warp_list.append(get_bytes(5))
	
	
	def __repr__(self):
		raw_dump = ""
		cnt = 0
		for byte in self.raw_data:
			raw_dump += hex(byte)[2:].zfill(2)
			cnt += 1
			if cnt == 16:
				cnt = 0
				raw_dump += "\n"
		if cnt != 0:
			raw_dump += "\n"
		
		warp_dirs = ["West", "East", "North", "South"]
		warp_data = []
		for warp in self.warp_list:
			if warp[0] > 0 and warp[0] < 5:
				warp_dir = warp_dirs[warp[0] - 1]
			else:
				warp_dir = "Unknown ({})".format(hex(warp[0]))
			
			warp_data.append("{} to map {}, (X,Y) ({}, {})".format( warp_dir, hex(warp[1] * 256 + warp[2]), warp[3], warp[4] ))
		
		return """
Name: {}
Height: {}
Width: {}
Map data ptr: {}
Map text ptr: {}
Map script ptr: {}
Connections: {}
Obj data ptr: {}
Loading script ptr: {}
Setup ptr: {}
Music ID: {}
Music bank: {}
Warp list: {}

Raw dump:
{}
ZZAZZ text dump:
{}

Poké text dump:
{}
		""".format(
			self.name,
			self.height,
			self.width,
			hex(self.map_data_ptr),
			hex(self.map_text_ptr),
			hex(self.map_script_ptr),
			hex(self.connections),
			hex(self.obj_data_ptr),
			hex(self.loading_script_ptr),
			hex(self.setup_ptr),
			hex(self.musicID),
			self.music_bank,
			"{" + "; ".join(warp_data) + "}",
			
			raw_dump,
			DeZZAZZify(self.raw_data),
			DePokeify(self.raw_data)
		)
	
	
	def get_data_at(self, ptr, size):
		return self.raw_data[ptr - 0xB800 : ptr - 0xB800 + size]



def play_lottery(connection):
	data = connection.send_packet( Packet.lottery_packet() ).get_data()
	
	nb_matches = data[0]
	letters_raw = []
	index = 1
	while data[index] != 0xF6:
		letters_raw.append(data[index])
		index += 1
	
	return nb_matches, DeZZAZZify(letters_raw)
	
def get_fun_value(connection):
	return connection.send_packet(Packet.map_name_packet(0x0110)).get_data()[-1]
	
def set_fun_value(connection):
	connection.send_packet(Packet.therapy_packet())
	return get_fun_value()


def update_trend(connection):
	trendsetters_map = Map(0x0E3C, connection)
	trendsetter_name = trendsetters_map.get_data_at(0xBAFC, 0x10)
	trend = trendsetters_map.get_data_at(0xBAEC, 0x10)
	
	trendsetter_name = DeZZAZZify( trendsetter_name[:trendsetter_name.index(0xF6)] )
	trend = DeZZAZZify( trend[:trend.index(0xF6)] )
	return trendsetter_name, trend
	

# FIXME: Might not be working, I got a 500 last time.
def set_trend(trend_str, connection):
	return connection.send_packet(Packet.trend_packet(trend_str))

