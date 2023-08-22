from dmx import Colour, DMXInterface, DMXLight3Slot, DMXUniverse, DMXLight
from time import sleep
from typing import List
import asyncio
import paho.mqtt.client as mqtt
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
import json

print("HI")
BROKER_URL = "192.168.1.126"
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
    #if shared.should_write():
    interface.set_frame(universe.serialise())
    interface.send_update()
    shared.update_write_time()

# Function to periodically send DMX
async def periodic_send_dmx(interface,universe):
    while True:
        await send_dmx(interface,universe)
        await asyncio.sleep(1)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test")

def on_message_easy(client, userdata, msg):
    print(f"Received message on {msg.topic}: {msg.payload}")
    interface, universe = userdata['interface'], userdata['universe']
    
    value = int(msg.payload.decode("utf-8"))
    channels.set(2, 0)
    channels.set(3, 0)
    channels.set(4, 0)
    channels.set(value, 255)
    interface.set_frame(universe.serialise())
    interface.send_update()
    shared.update_write_time()
    
def on_message(client, userdata, msg):
    print(f"Received message on {msg.topic}: {msg.payload}")
    interface, universe = userdata['interface'], userdata['universe']
    
    
    try:
        decoded_payload = msg.payload.decode("utf-8")
        data = json.loads(decoded_payload)

    # Iterate over the dictionary and print each key-value pair
        for key, value in data.items():
            int_key = int(key)
            int_value = int(value)
            channels.set(int_key, int_value)
    except ValueError:
        print(f"Invalid message received: {msg.payload}")

    interface.set_frame(universe.serialise())
    interface.send_update()
    shared.update_write_time()
            

def main():
    with DMXInterface("FT232R") as interface:
        universe = DMXUniverse()
        universe.add_light(channels)
        
        client = mqtt.Client(userdata={'interface': interface, 'universe': universe})
        client.on_connect = on_connect
        client.on_message = on_message
        #client = MQTTClient()
        
        client.connect(BROKER_URL, 1883, 60)

        #await client.connect(BROKER_URL)

        #await client.subscribe([("test", QOS_1)])
        #asyncio.create_task(on_message(client, interface, universe))
        
        # Non-blocking call that processes network traffic, dispatches callbacks, etc
        client.loop_start()

        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(periodic_send_dmx(interface,universe))
        except KeyboardInterrupt:
            pass
        finally:
            client.loop_stop()  # Stop loop 
            client.disconnect()  # Disconnect from MQTT

        # Start the periodic DMX send
        #await periodic_send_dmx(interface,universe)
main()
# Run the event loop
#try:
    #asyncio.run(main())
#except KeyboardInterrupt:
    #print("Gracefully shutting down...")
