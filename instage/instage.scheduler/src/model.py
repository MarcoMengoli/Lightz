import math

class DeviceScene:
    def __init__(self, name: str, timer: int, base_address: int, values: list[list[int]]):
        self.name = name
        self.timer = timer
        self.base_address = base_address
        self.values = [[min(255, max(0, val)) for val in sublist] for sublist in values]
        self._tick_millis = self.timer # default is like timer, but would be <=
        self.reset()
    
    def tick(self) -> dict[int,int]:
        try:
            values = self.get_values()
            ticks_before_enhance = self.timer / self._tick_millis
            if self._current_tick + 1 == ticks_before_enhance:
                self._current_tick = 0
                self._current_set_index = (self._current_set_index + 1) % len(self.values)
            else:
                self._current_tick = self._current_tick + 1
            
            return values
        
        except Exception as e:
            print(f"Error calculating device scene tick: {e}")
            return False

    def reset(self) -> None:
        self._current_tick = 0
        self._current_set_index = 0
    
    def get_values(self) -> dict[int,int]:
        current_values = self.values[self._current_set_index % len(self.values)]
        values = {self.base_address + i: value for i, value in enumerate(current_values)}
        return values
    
    def set_tick_value(self, tick_value: int) -> None:
        self._tick_millis = min(tick_value, self.timer)

class Scene:
    def __init__(self, name: str, device_scenes: list[DeviceScene]):
        self.name = name
        self.device_scenes = device_scenes
        self.tick_millis = self.gcd()

        for dev in self.device_scenes:
            dev.set_tick_value(self.tick_millis)

    def reset(self) -> None:
        for dev in self.device_scenes:
            dev.reset()

    def tick(self) -> dict[int,int]:
        merged_dict = {}
        for device_scene in self.device_scenes:
            vals = device_scene.tick()
            merged_dict.update(vals)
        
        return merged_dict
        
    def get_values(self) -> dict[int,int]:
        merged_dict = {}
        
        for device_scene in device_scene.device_scenes:
            merged_dict.update(device_scene.get_values())

        return merged_dict

    def gcd(self) -> int:
        try:
            if not self.device_scenes:
                return 0
            
            timers = [device_scene.timer for device_scene in self.device_scenes if device_scene.timer != 0]


            if not timers:
                return 1000

            result = timers[0]
            for timer in timers[1:]:
                result = math.gcd(result, timer)
            return result
        except Exception as e:
            print(f"Error calculating greatest common divisor: {e}")
            return 1000


    
class Chore:
    def __init__(self, name: str, scenes: list[Scene], duration_seconds: int):
        self.name = name
        self.scenes = scenes
        self.duration_seconds = duration_seconds
        self._current_tick = 0
        self._current_scene_index = 0

    def get_current_tick_millis_timer(self) -> int:
        if len(self.scenes) == 0:
            return 1000
        
        return self.get_current_scene().tick_millis
    
    def tick(self) -> dict[int,int]:
        try:
            ticks_before_enhance = self.duration_seconds * 1000 / self.get_current_tick_millis_timer()
            if self._current_tick + 1 == ticks_before_enhance:
                self.get_current_scene().reset()
                self._current_tick = 0
                self._current_scene_index = (self._current_scene_index + 1) % len(self.scenes)
            else:
                self._current_tick = self._current_tick + 1
            
            values = self.get_current_scene().tick()
            return values
        
        except Exception as e:
            print(f"Error calculating chore tick: {e.with_traceback}")
            return False
        
    def reset(self) -> None:
        self._current_tick = 0
        self._current_scene_index = 0
        for scene in self.scenes:
            scene.reset()
        
    def get_values(self) -> dict[int,int]:
        return self.get_current_scene().get_values()

    def get_current_scene(self):
        return self.scenes[self._current_scene_index % len(self.scenes)]