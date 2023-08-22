from dmx import Colour, DMXInterface, DMXLight3Slot, DMXUniverse, DMXLight
from time import sleep
from typing import List

PURPLE = Colour(255, 0, 255)


class DMXChannels(DMXLight):
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
        #return super().serialise() + self._channels
        return self._channels

x = 1
r = 2
g = 3
b = 4
m = 6
c = 7
s = 2#60/128

# Open an interface
with DMXInterface("FT232R") as interface:
    # Create a universe
    universe = DMXUniverse()

    # Define a light
    #light = DMXLight3Slot(address=1)
    channels = DMXChannels(address=1)

    # Add the light to a universe
    #universe.add_light(light)
    universe.add_light(channels)

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    while True:
        # Set light to purple
        #light.set_colour(PURPLE)

        channels.set(x, 255)
        channels.set(r, 255)
        channels.set(g, 0)
        channels.set(b, 0)
        #channels.set(m, 252)
        #channels.set(c, 190)

        # Update the interface's frame to be the universe's current state
        interface.set_frame(universe.serialise())

        # Send an update to the DMX network
        interface.send_update()

        sleep(s)
        
        channels.set(x, 255)
        channels.set(r, 0)
        channels.set(g, 255)
        channels.set(b, 0)
        #channels.set(m, 252)
        #channels.set(c, 190)
        interface.set_frame(universe.serialise())
        interface.send_update()

        sleep(s)
        
        channels.set(x, 255)
        channels.set(r, 0)
        channels.set(g, 0)
        channels.set(b, 255)
        #channels.set(m, 252)
        #channels.set(c, 190)
        interface.set_frame(universe.serialise())
        interface.send_update()

        
        sleep(s)
 
