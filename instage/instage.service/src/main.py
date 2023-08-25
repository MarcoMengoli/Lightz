from datetime import datetime, timedelta
import json
import redis
import time
import os
from dmxWriter import DmxWriter
from dmx import DMXInterface, DMXUniverse, DMXLight

print("START")


def main():
    r = None
    while r is None:
        r = None
        try:
            redis_port = int(os.environ.get('REDIS_PORT', 6379))  # Default to 6379 if the environment variable is not set
            r = redis.Redis(host='localhost', port=redis_port, db=0)
            r.ping()

            with DMXInterface("FT232R") as interface:
                universe = DMXUniverse()
                all_channels = DmxWriter(address=1)
                universe.add_light(all_channels)

                interface.set_frame(universe.serialise())
                interface.send_update()
                
                while True:

                    retrieved_dict = r.hgetall('ch')

                    for k, v in retrieved_dict.items():
                        key = int(k.decode('utf-8'))
                        value = int(v.decode('utf-8'))
                        
                        if 1 <= key <= 512 and 0 <= value <= 255:
                            all_channels.set(key, value)

                    interface.set_frame(universe.serialise())
                    interface.send_update()

                    # # Convert the retrieved values back to integers
                    # int_dict = {int(k.decode('utf-8')): int(v.decode('utf-8')) for k, v in retrieved_dict.items()}

                    # data = r.lrange('dmx-channels', 0, -1)
                    # print([item.decode('utf-8') for item in data])
                    time.sleep(0.5)
        except Exception as e:
            print(f"Error: {e}. Retrying in 1 second...")
            time.sleep(1)
            r = None

if __name__ == "__main__":
    main()
