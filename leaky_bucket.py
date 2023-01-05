import random

data = []
data_choices = [8,16,32,64,128]
packet_choices = [8,32,64]
packet_size = random.choice(packet_choices)
max_val = random.choice(data_choices)
buffer = 0
letters = [chr(i) for i in range(65,91)]
i = 1

while buffer <= max_val:
    packet = "".join([random.choice(letters) for i in range(packet_size)])
    # print(f"Packets {i} : {packet}")
    buffer += packet_size
    if buffer <= max_val:
        data.append(packet)
    else:
        print(f"Packet {i} rejected : {packet}\nProcess Stopped")
    i+=1



# print(f"Buffer val : {buffer}")
print(f"Max Val : {max_val}")
print(f"Packet size : {packet_size}")
print(f"Data : {data}")