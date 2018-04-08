# Fools2018-lib

A Python library to interface with [TheZZAZZGlitch](https://github.com/zzazzdzz)'s [2018 April Fools event](https://zzazzdzz.github.io/fools2018).

Written by [ISSOtm](https://github.com/ISSOtm), with some help/inspiration from [ParzivalWolfram](https://github.com/ParzivalWolfram) and help from [jfb1337](https://github.com/joefarebrother), [NieDzejkob](https://github.comNieDzejkob), and [Riley/slipstream](https://github.com/Wack0).


# Usage

First, you need an account at [the event's site](https://zzazzdzz.github.io/fools2018). If you don't have one, register one.

To use the library, you need a connection token.

## Connecting to the server

### Without a token

You must first create a Connection object, then call the `get_token` method on it:
```
import Fools2018

connection = Fools2018.Connection("ip.ad.dr.ess", "port")
connection.get_token("username", "password")
```

**A connection without a token will always fail with a 500 error! Ensure you always call `get_token`!**

### With a token

If you already have a token, you can simply pass it to the Connection object:
```
import Fools2018

connection = Fools2018.Connection("ip.ad.dr.ess", "port", "token")
```


## Sending packets to the server

### Word of caution

Be careful, the server has a rate limiter, so don't hope to DoS the server using this lib. This also has chances to get your IP banned / account deleted. You have been warned.

ZZAZZ generally frowns upon sending many requests, even if it doesn't hit the rate limiter, since it has caused server failures a few times. He has stated that you shouldn't do more than **1 request per second**. The map dumper script does 2 requests per second (since 1 map == 2 requests, and there's a 1 second delay between maps), but I was the only one to run it when I wrote it.

tl;dr: You must not send packets faster than **1 request per second**. None of the scripts' authors can be held responsible for any problems that may arise if you do.


### The Packet class

The Packet class emulates the packets sent by the Game Boy to the client program. Emulation of the client program is done by a Connection object.

Packets have a length, a checksum, and a command type, as well as some variable-length data.


### Creating a packet

#### Predefined packets

Most of the time, you will simply want to create a packet that the game would send (eg. to analyze a map's data, or to check the lottery). The Packet class has some static functions that do just that:
* `map_name_packet(map_id)`: Creates a packet requesting a map's ID (`map_id` is a uint16). WARNING: THIS WILL EMPTY YOUR INVENTORY!!
* `map_packet(map_id)`: Creates a packet requesting a map's data (`map_id` is a uint16).
* `trend_packet(trend_str)`: Creates a packet attempting to change the trendy phrase. Note that the trendy phrase's length is capped at 15 characters, and the server usually responds to malformed demands with an error.
* `lottery_packet()`: Creates a packet requesting to play the lottery. This returns how many matches you got, and the lottery letters. (Note: this will grant the appropriate achievement(s)... or it would if the event wasn't over, lol).
* `therapy_packet()`: Creates a packet requesting for a Fun value change.
* `cavern4_packet()`: Creates a packet validating Cracker Cavern 4. Now you know why this wasn't published earlier :D


#### Manual creation

Packets can be manually instantiated: `Fools2018.Packet(type, data)`. `type` must be a `uint8`, though it's recommended to use the attributes listed below. `data` must be an iterable of uint8's, preferably a `list` or perhaps a `tuple`.

##### Packet types
```
TYPE_PING
TYPE_MAP_NAME
TYPE_MAP
TYPE_TREND
TYPE_LOTTERY
TYPE_THERAPY
TYPE_CAVERN4
```


#### Raw packets

It's possible to obtain the raw bytes forming a packet using its `get_bytes` method, and it's possible to create a packet from its raw bytes using `Packet.from_bytes(bytes)`. Further details won't be given in this document, you should check the functions themselves.


### Sending a packet

Sending a packet is done by calling the `send_packet` method on a `Connection` object. **The Connection must have obtained a token as described [here](#connecting-to-the-server), or this will fail!**

On success, this returns the server's response as a `Packet`. On failure, this will propagate the exception (usually a HTTPError raised by urllib).



## Maps

The `Map` class was created to automate map data analysis. A `Map` object is created by passing it the ID of the requested map (uint16) and the connection to use to retrieve the map. Note that the account used may matter (fun value, access to Cracker Cavern 3, 4 and 5, etc.)

The Map object gives a very detailed list of the map's properties when repr'd.



## Lottery

The lottery can be played by calling `play_lottery(connection)`. A tuple is returned, containing the number of matches the username got, and the lottery's letters.



## Fun

(The Fun research was done by jfb1337)

The fun value can be retrieved from any map name packet's last byte, or by calling `get_fun_value(connection)`. It's also possible to request a new fun value by using `set_fun_value(connection)`, which returns the new Fun value.

(Yes, the inconsistent spelling of "Fun" is intentional.)


## Trends

`update_trend(connection)` returns the current trend setter and the trending phrase. `set_trend(str, connection)` sets a new trend using the token's account. Note that the trend strings are normally 15 characters at most, and the server rejects bad strings.
