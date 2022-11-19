# initial packets in the bucket
storage = int(input("Enter initial packets:"))
 
# total no. of times bucket content is checked
no_of_queries=int(input("Enter no of times to check:"))
 
# total no. of packets that can
# be accommodated in the bucket
bucket_size = int(input("Enter bucket size:"))
 
# no. of packets that enters the bucket at a time
input_pkt_size = int(input("Enter input size"))
 
# no. of packets that exits the bucket at a time
output_pkt_size = int(input("Enter output size"))
for i in range(0, no_of_queries):  # space left
 
    size_left = bucket_size - storage
    if input_pkt_size <= size_left:
      # update storage
        storage += input_pkt_size
    else:
        print("Packet loss = ", input_pkt_size)
 
    print(f"Buffer size= {storage} out of bucket size = {bucket_size}")
 
    # as packets are sent out into the network, the size of the storage decreases
    storage -= output_pkt_size