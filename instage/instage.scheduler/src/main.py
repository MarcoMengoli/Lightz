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

            bl = gateway.find_chore_by_name("AllBlack")
            print(lb.name)
            wh = gateway.find_chore_by_name("AllWhite")
            print(wh.name)
            st = gateway.find_chore_by_name("AllStrobe")
            print(st.name)
            a = gateway.find_chore_by_name("A")
            print(a.name)
            b = gateway.find_chore_by_name("B")
            print(b.name)
            c = gateway.find_chore_by_name("C")
            print(c.name)


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
                print(f"{i} - {chore.get_current_scene().name} - {values}")

                time.sleep(timer/1000)

                name_b = r.get('current_chore')
                name = None
                if name_b:
                    name = name_b.decode('utf-8')
                if name and name != chore.name:
                    print(f"Different-{name}-{chore_name}")
                    chore = gateway.find_chore_by_name(name)
                    if name == bl.name:
                        chore = bl
                    if name == wh.name:
                        chore = wh
                    if name == st.name:
                        chore = st
                    if name == a.name:
                        chore = a
                    if name == b.name:
                        chore = b
                    if name == c.name:
                        chore = c
                    print(f"{i} - {chore.name} - {values}")
                    print(f"NewChore-{chore.get_current_scene().name}")
            

        except Exception as e:
            print(f"Error: {e}. Retrying in 1 second...")
            time.sleep(1)
            r = None



if __name__ == "__main__":
    main()
