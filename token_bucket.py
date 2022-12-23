import time

# Initial number of tokens in the bucket
TOKEN_BUCKET_SIZE = int(input("Enter the initial number of tokens:"))

# Maximum rate at which tokens are added to the bucket (in tokens/second)
TOKEN_ADDITION_RATE = int(input("Enter rate"))

# Current number of tokens in the bucket
tokens = TOKEN_BUCKET_SIZE

# Incoming packets to transmit
packets = ["Packet 1", "Packet 2", "Packet 3", "Packet 4", "Packet 5"]

# Implement the token bucket algorithm
for packet in packets:
  # Check if there are enough tokens in the bucket to transmit the packet
  if tokens >= 1:
    # Transmit the packet and remove a token from the bucket
    print("Transmitting packet:", packet)
    tokens -= 1
  else:
    # Wait for a token to become available
    print("Waiting for a token to transmit packet:", packet)
    time.sleep(1 / TOKEN_ADDITION_RATE)
    tokens += 1
    # Transmit the packet and remove a token from the bucket
    print("Transmitting packet:", packet)
    tokens -= 1
