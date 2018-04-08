f = open("fun_event_log")

events = {}
for line in f:
	line=line.split(" ")
	map_id=int(line[1], 16)
	fun1=int(line[6])
	fun2=int(line[8])
	if map_id not in events:
		events[map_id]=[]
	events[map_id] += [(fun1,fun2), (fun2,fun1)]
	
f.close()
	
for map_id in events:
	print("Fun events in map 0x{}".format(hex(map_id)[2:].zfill(4)))

	connected_components=[]
	processed=[False]*256
	for i in range(256):
		if processed[i]:
			continue
		equal=[]
		for j in range(256):
			if processed[j]:
				continue
			if (i,j) not in events[map_id]:
				equal.append(j)
				processed[j]=True
		processed[i]=True
		connected_components.append(equal)
	
	i = 1
	for cc in connected_components:
		if len(cc) < 2:
			continue
		print("Version {} found at values:".format(i))
		i+=1
		for j in cc:
			print("{},".format(j), end="")
		print("\n")

