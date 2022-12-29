data = "10111010000000000000000"
gx = "10001000000100001"
rem = ""

for j in range(len(data)-len(gx)):
    cur_data = data[j:]
    print(f"cur_data : {cur_data}")
    print(f"gx : {gx}")
    for i in range(len(gx)):
        rem =  str(int(cur_data[i]) ^ int(gx[i]))
    if rem[0] == "0":
        rem = rem ^ 0 

# data = "10111010000000000000000"
# gx = "10001000000100001"
# rem = data[:18]

# for j in range(len(data)-len(gx)):
#     for i in range(len(gx)):
#         rem =  str(int(rem[i]) ^ int(gx[i]))
#     if rem[0] == "0":
#         rem = int(rem) ^ 0
#     rem = rem[1:]+data[j+19]

    
