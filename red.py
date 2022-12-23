import random

# Threshold for the queue size
THRESHOLD = int(input("Enter threshold"))

# Drop probability for packets when the queue size is above the threshold
DROP_PROBABILITY = 0.1

# Current size of the queue
queue_size = int(input("Enter size of the queue"))

# Incoming packet
packet = "Packet"

# Implement the RED algorithm
if queue_size > THRESHOLD:
  # Generate a random number between 0 and 1
  r = random.uniform(0, 1)
  if r < DROP_PROBABILITY:
    # Drop the packet
    print("Dropping packet")
  else:
    # Accept the packet
    print("Accepting packet")
else:
  # Accept the packet
  print("Accepting packet")
