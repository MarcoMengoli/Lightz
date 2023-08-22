from dmx import Colour, DMXInterface, DMXLight3Slot, DMXUniverse, DMXLight
from time import sleep
from typing import List
import asyncio
#from hbmqtt.client import MQTTClient, ClientException
#from hbmqtt.mqtt.constants import QOS_1
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

print("HI")
BROKER_URL = "mqtt://your_mqtt_broker"
executor = ThreadPoolExecutor(max_workers=1)

# Shared object to track the last write time
class SharedObject:
    def __init__(self):
        self._last_write_time = datetime.min
        self._channels = [0] * 512

    def should_write(self):
        # If last write was more than a second ago
        return datetime.now() - self._last_write_time > timedelta(seconds=1)

    def update_write_time(self):
        self._last_write_time = datetime.now()
        
    def set(self, channel, value):
        c = int(max(1, min(channel, 512)))
        v = int(max(0, min(value, 255)))
        self._channels[c-1] = v

shared = SharedObject()
i = shared._last_write_time


class AllDmxChannels(DMXLight):
    def __init__(self, address: int = 1):
        super().__init__(address=address)
        self._channels = [0] * 512

    @property
    def slot_count(self) -> int:
        return 512

    def set(self, channel, value):
        c = int(max(1, min(channel, 512)))
        v = int(max(0, min(value, 255)))
        self._channels[c-1] = v

    def serialise(self) -> List[int]:
        return self._channels

x = 1
r = 2
g = 3
b = 4
m = 6
c = 7
s = 2#60/128


channels = AllDmxChannels(address=1)
channels.set(x, 255)
channels.set(r, 255)
channels.set(g, 0)
channels.set(b, 0)

async def send_dmx(interface,universe):
    if shared.should_write():
        interface.set_frame(universe.serialise())
        interface.send_update()
        shared.update_write_time()

# Function to periodically send DMX
async def periodic_send_dmx(interface,universe):
    while True:
        await send_dmx(interface,universe)
        await asyncio.sleep(1)
        

async def main():
    with DMXInterface("FT232R") as interface:
        universe = DMXUniverse()
        universe.add_light(channels)
        # Start the periodic DMX send
        await periodic_send_dmx(interface,universe)

# Run the event loop
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Gracefully shutting down...")
