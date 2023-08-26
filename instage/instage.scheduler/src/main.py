import json
import redis
import time
import os
from model import DeviceScene, Scene, Chore
#from mongo_gateway import MongoGateway
from inmem_gateway import InMemGateway

print("START")

def fill_main_chores(gateway):
    pass


def main():

    r = None
    while r is None:
        r = None
        try:
            redis_port = int(os.environ.get('REDIS_PORT', 6379))  # Default to 6379 if the environment variable is not set
            redis_host = os.getenv('REDIS_HOST', 'localhost')     # Default to localhost if the environment variable is not set
            
            r = redis.Redis(host=redis_host, port=redis_port, db=0)
            r.ping()
    
            # gateway = MongoGateway()
            # gateway.open()
            gateway = InMemGateway()
            gateway.open()

            a = gateway.find_chore_by_name("AllBlack")
            b = gateway.find_chore_by_name("AllWhite")
            c = gateway.find_chore_by_name("AllStrobe")
            # fill_main_chores(gateway)

            # chore_name = "Test"
            # chore = gateway.find_chore_by_name(chore_name)

            # if not chore:
            #     print(f"Chore {chore_name} not found")
            #     exit()

            # print(chore.name)
            # print(chore.duration_seconds)
            # for scene in chore.scenes:
            #     print(f"Scene Name: {scene.name}")
            #     for device_scene in scene.device_scenes:
            #         print(f"Device Name: {device_scene.name}")
            #         print(f"Timer: {device_scene.timer}")
            #         print(f"Base Address: {device_scene.base_address}")
            #         print(f"Values: {device_scene.values}")
            #     print("------------------------------")

            default_chore_name = "AllBlack"

            chore_name_b = r.get('current_chore')
            chore_name = None
            
            if chore_name_b:
                chore_name = chore_name_b.decode('utf-8')
            if not chore_name:
                chore_name = default_chore_name

            chore = gateway.find_chore_by_name(chore_name)
            if not chore:
                chore = gateway.find_chore_by_name(default_chore_name)

            i = 0
            print(f"{i} - {chore.get_current_scene().name}")
            
            while True:

                timer = chore.get_current_tick_millis_timer()
                i = i + 1
                values = chore.tick()
                

                r.hset("ch", mapping=values)

                time.sleep(timer/1000)

                name_b = r.get('current_chore')
                name = None
                if name_b:
                    name = name_b.decode('utf-8')
                if name and name != chore_name:
                    chore = gateway.find_chore_by_name(chore_name)
                    print(f"{i} - {chore.get_current_scene().name} - {values}")
            
            gateway.close()

        except Exception as e:
            print(f"Error: {e}. Retrying in 1 second...")
            time.sleep(1)
            r = None





    #         with DMXInterface("FT232R") as interface:
    #             universe = DMXUniverse()
    #             all_channels = DmxWriter(address=1)
    #             universe.add_light(all_channels)

    #             interface.set_frame(universe.serialise())
    #             interface.send_update()
                
    #             while True:

    #                 retrieved_dict = r.hgetall('ch')

    #                 for k, v in retrieved_dict.items():
    #                     key = int(k.decode('utf-8'))
    #                     value = int(v.decode('utf-8'))
                        
    #                     if 1 <= key <= 512 and 0 <= value <= 255:
    #                         all_channels.set(key, value)

    #                 interface.set_frame(universe.serialise())
    #                 interface.send_update()

    #                 # # Convert the retrieved values back to integers
    #                 # int_dict = {int(k.decode('utf-8')): int(v.decode('utf-8')) for k, v in retrieved_dict.items()}

    #                 # data = r.lrange('dmx-channels', 0, -1)
    #                 # print([item.decode('utf-8') for item in data])
    #                 time.sleep(0.5)
    #     except Exception as e:
    #         print(f"Error: {e}. Retrying in 1 second...")
    #         time.sleep(1)
    #         r = None

if __name__ == "__main__":
    main()
