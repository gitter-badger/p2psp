# The P2PSP.org project has been supported by the Junta de Andalucia
# through the Proyecto Motriz "Codificacion de Video Escalable y su
# Streaming sobre Internet" (P10-TIC-6548).

MAX_CHUNK_NUMBER = 65536
#MAX_CHUNK_NUMBER = 2048
#COUNTERS_TIMING = 0.1
COUNTERS_TIMING = 1
PEER_ID_LENGTH = 7
HELLO_PACKET_TIMING = 1 # Time between continuously sent packets
MAX_PEER_ARRIVING_TIME = 15 # Maximum time after peer retries incorporation
MAX_TOTAL_INCORPORATION_TIME = 60 # Peers needing longer to incorporate are removed from team
MAX_PREDICTED_PORTS = 20 # Number of probable source ports that will be tried
CONSOLE_MODE = True
