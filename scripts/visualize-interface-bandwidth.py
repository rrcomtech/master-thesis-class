import matplotlib.pyplot as plt
import numpy as np

# Given data
attempts = np.array([1, 2, 3, 4, 5])
bytes_sent = np.array([1000, 1000, 1000, 1000, 1000])
bytes_received = np.array([1000, 1000, 1000, 1000, 1000])
duration = np.array([123, 97, 105, 133, 114])

throughput = [(bytes_sent[i] / duration[i]*1000) for i in range(0, len(duration))]

# Calculate the total bytes (sum of bytes sent and bytes received)
total_bytes = bytes_sent + bytes_received

# Plottinga
fig, ax1 = plt.subplots()

# Bar plot for bytes sent and received
width = 0.5  # Width of the bars
ax1.bar(attempts, throughput, width=width, label='Throughput', alpha=0.7)
# ax1.bar(attempts + width/2, bytes_received, width=width, label='Bytes Received', alpha=0.7)

# Set labels and title
ax1.set_xlabel('Run')
ax1.set_ylabel('Throughput in KB/s')
ax1.set_title('Data Latency for Communication with FPGA')

# Show legends
ax1.legend(loc='upper left')

# Show the plot
plt.show()
