cidr_string = "200.100.33.65/26"
cidr_split = cidr_string.split('/')

# Network
address = cidr_split[0]
# Subnet Mask (tells us how many IP there are)
subnet_mask = int(cidr_split[1])
octet_ip = address.split('.')

# Initialise the netmask and calculate based on CIDR mask
mask = [0, 0, 0, 0]
for i in range(subnet_mask):
    mask[i/8] = mask[i/8] + (1 << (7 - i % 8))
    # print(mask)

# Initialise net and binary and netmask with address to get network
net = []
for i in range(4):
	# Add the int from each byte of the IP address + the mask is the 
    net.append(int(octet_ip[i]) & mask[i])

# Start IP Range    
start_ip = net[:]
start_ip[3] = start_ip[3] + 1


# Duplicate net into broad array, gather host bits, and generate broadcast
broad = list(net)
broad_range = 32 - subnet_mask
for i in range(broad_range): 
	# << moves all bits to the left by (i % 8) bits 
	broad[3 - i/8] = broad[3 - i/8] + (1 << (i % 8))

# End IP Range    
end_ip = broad[:]
end_ip[3] = end_ip[3] - 1

# Convert Start IP Range to hexadecimal
start_ip_hex = []
for i in start_ip:
    # Reverse indexing
    n = 3 - start_ip.index(i)
    start_ip_hex.append(i * 256**n)

# Convert End IP Range to hexadecimal
end_ip_hex = []
for i in end_ip:
    # Reverse indexing
    n = 3 - end_ip.index(i)
    end_ip_hex.append(i * 256**n)


# Test
print("Network:", ".".join(map(str, net)))
print ("Broadcast: " , ".".join(map(str, broad)))
print("Start Ip:", ".".join(map(str, start_ip)))
print ("End Ip: " , ".".join(map(str, end_ip)))
print("Start IP Range Hexadecimal", sum(start_ip_hex))
print("End IP Range Hexadecimal", sum(end_ip_hex))
