from dmx import DMXInterface, DMXUniverse, DMXLight
from typing import List

class DmxWriter(DMXLight):
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