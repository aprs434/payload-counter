from time import sleep
from ulora import LoRa, ModemConfig, SPIConfig

# This is our callback function that runs when a message is received
def on_recv(payload):
    print('Length:', payload.length)
    print('Data:', payload.data)
    print('RSSI: {}; SNR: {}'.format(payload.rssi, payload.snr))

# Lora Parameters
RFM95_RST = 14
RFM95_SPIBUS = SPIConfig.heltec
RFM95_CS = 18
RFM95_INT = 26
RF95_FREQ = 433.775
CLIENT_ADDRESS = 1
SERVER_ADDRESS = 2

# initialise radio
lora = LoRa(RFM95_SPIBUS, RFM95_INT, SERVER_ADDRESS, RFM95_CS, reset_pin=RFM95_RST, freq=RF95_FREQ, receive_all=True)

# set callback
lora.on_recv = on_recv

# set to listen continuously
lora.set_mode_rx()

# loop and wait for data
print('The payload counter is running...')
while True:
    sleep(0.1)