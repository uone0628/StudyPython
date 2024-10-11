import matplotlib.pyplot as plt
import numpy as np

# Define the data for both Go-Back-N and Selective Repeat
time = np.arange(1, 11)

# Go-Back-N data (0 - Sent, 1 - Lost, 2 - Timeout, 3 - Retransmitted, 4 - Acked)
gbn_status = [0, 1, 0, 0, 0, 2, 3, 3, 3, 3] # Sequence 1 lost, all others retransmitted after timeout
gbn_ack = [1, 1, 1, 1, 1, 0, 2, 3, 4, 5] # Acked after retransmissions

# Selective Repeat data (0 - Sent, 1 - Lost, 2 - Timeout, 3 - Retransmitted, 4 - Acked)
sr_status = [0, 1, 0, 0, 0, 2, 3, 4, 4, 4] # Sequence 1 lost, only 1 retransmitted
sr_ack = [1, 3, 3, 4, 5, 0, 2, 2, 2, 2] # Acked individually except lost

# Plot setup
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# Plot for Go-Back-N
axs[0].plot(time, gbn_status, marker='o', label='Seq Status', linestyle='-')
axs[0].plot(time, gbn_ack, marker='x', label='ACKs', linestyle='--')
axs[0].set_title("Go-Back-N Protocol")
axs[0].set_xlabel("Time")
axs[0].set_ylabel("Status/ACK")
axs[0].set_yticks([0, 1, 2, 3, 4, 5])
axs[0].legend()
axs[0].grid(True)

# Plot for Selective Repeat
axs[1].plot(time, sr_status, marker='o', label='Seq Status', linestyle='-')
axs[1].plot(time, sr_ack, marker='x', label='ACKs', linestyle='--')
axs[1].set_title("Selective Repeat Protocol")
axs[1].set_xlabel("Time")
axs[1].set_ylabel("Status/ACK")
axs[1].set_yticks([0, 1, 2, 3, 4, 5])
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()
