from datetime import datetime, timedelta
import json
import redis
import time
import os
from dmxWriter import DmxWriter
from dmx import DMXInterface, DMXUniverse, DMXLight

print("START")


def main():
    redis_port = int(os.environ.get('REDIS_PORT', 6379))  # Default to 6379 if the environment variable is not set
    r = redis.Redis(host='redis', port=redis_port, db=0)

    with DMXInterface("FT232R") as interface:
        universe = DMXUniverse()
        all_channels = DmxWriter(address=1)
        universe.add_light(all_channels)

        interface.set_frame(universe.serialise())
        interface.send_update()
        
        while True:

            retrieved_dict = r.hgetall('dmx-channels')

            for k, v in retrieved_dict.items():
                key = int(k.decode('utf-8'))
                value = int(v.decode('utf-8'))
                
                all_channels.set(key, value)

            interface.set_frame(universe.serialise())
            interface.send_update()

            # # Convert the retrieved values back to integers
            # int_dict = {int(k.decode('utf-8')): int(v.decode('utf-8')) for k, v in retrieved_dict.items()}

            # data = r.lrange('dmx-channels', 0, -1)
            # print([item.decode('utf-8') for item in data])
            time.sleep(0.5)

if __name__ == "__main__":
    main()


    

# BROKER_URL = "192.168.1.126"
# executor = ThreadPoolExecutor(max_workers=1)

# # Shared object to track the last write time
# class SharedObject:
#     def __init__(self):
#         self._last_write_time = datetime.min
#         self._channels = [0] * 512

#     def should_write(self):
#         # If last write was more than a second ago
#         return datetime.now() - self._last_write_time > timedelta(seconds=1)

#     def update_write_time(self):
#         self._last_write_time = datetime.now()
        
#     def set(self, channel, value):
#         c = int(max(1, min(channel, 512)))
#         v = int(max(0, min(value, 255)))
#         self._channels[c-1] = v

# shared = SharedObject()
# i = shared._last_write_time


# channels = AllDmxChannels(address=1)
# channels.set(x, 255)
# channels.set(r, 255)
# channels.set(g, 0)
# channels.set(b, 0)

# async def send_dmx(interface,universe):
#     #if shared.should_write():
#     interface.set_frame(universe.serialise())
#     interface.send_update()
#     shared.update_write_time()

# # Function to periodically send DMX
# async def periodic_send_dmx(interface,universe):
#     while True:
#         await send_dmx(interface,universe)
#         await asyncio.sleep(1)

# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code "+str(rc))
#     client.subscribe("test")

# def on_message_easy(client, userdata, msg):
#     print(f"Received message on {msg.topic}: {msg.payload}")
#     interface, universe = userdata['interface'], userdata['universe']
    
#     value = int(msg.payload.decode("utf-8"))
#     channels.set(2, 0)
#     channels.set(3, 0)
#     channels.set(4, 0)
#     channels.set(value, 255)
#     interface.set_frame(universe.serialise())
#     interface.send_update()
#     shared.update_write_time()
    
# def on_message(client, userdata, msg):
#     print(f"Received message on {msg.topic}: {msg.payload}")
#     interface, universe = userdata['interface'], userdata['universe']
    
    
#     try:
#         decoded_payload = msg.payload.decode("utf-8")
#         data = json.loads(decoded_payload)

#     # Iterate over the dictionary and print each key-value pair
#         for key, value in data.items():
#             int_key = int(key)
#             int_value = int(value)
#             channels.set(int_key, int_value)
#     except ValueError:
#         print(f"Invalid message received: {msg.payload}")

#     interface.set_frame(universe.serialise())
#     interface.send_update()
#     shared.update_write_time()
            

# def main():
#     with DMXInterface("FT232R") as interface:
#         universe = DMXUniverse()
#         universe.add_light(channels)
        
#         client = mqtt.Client(userdata={'interface': interface, 'universe': universe})
#         client.on_connect = on_connect
#         client.on_message = on_message
#         #client = MQTTClient()
        
#         client.connect(BROKER_URL, 1883, 60)

#         #await client.connect(BROKER_URL)

#         #await client.subscribe([("test", QOS_1)])
#         #asyncio.create_task(on_message(client, interface, universe))
        
#         # Non-blocking call that processes network traffic, dispatches callbacks, etc
#         client.loop_start()

#         loop = asyncio.get_event_loop()
#         try:
#             loop.run_until_complete(periodic_send_dmx(interface,universe))
#         except KeyboardInterrupt:
#             pass
#         finally:
#             client.loop_stop()  # Stop loop 
#             client.disconnect()  # Disconnect from MQTT

#         # Start the periodic DMX send
#         #await periodic_send_dmx(interface,universe)
# main()
# # Run the event loop
# #try:
#     #asyncio.run(main())
# #except KeyboardInterrupt:
#     #print("Gracefully shutting down...")
