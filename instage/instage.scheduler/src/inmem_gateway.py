from model import Scene, Chore, DeviceScene
from typing import Optional

class InMemGateway:
    def __init__(self):
        pass

    def open(self):
        self._w1 = DeviceScene("Par001", 2000,1, [[255, 255, 255, 255, 0, 0, 0]])
        self._w2 = DeviceScene("Par017", 2000,17, [[255, 255, 255, 255, 0, 0, 0]])
        self._w3 = DeviceScene("Head33", 2000,33, [[255, 255, 255, 255]])
        self._white_scene = Scene("WhiteScene", [self._w1,self._w2,self._w3])
        self._white_chore = Chore("AllWhite", [self._white_scene], 60000)
        
        self._b1 = DeviceScene("Par001", 2000,1, [[0, 0, 0, 0, 0, 0, 0]])
        self._b2 = DeviceScene("Par017", 2000,17, [[0, 0, 0, 0, 0, 0, 0]])
        self._b3 = DeviceScene("Head33", 2000,33, [[0, 0, 0, 0]])
        self._black_scene = Scene("BlackScene", [self._b1,self._b2,self._b3])
        self._black_chore = Chore("AllBlack", [self._black_scene], 60000)

        self._m1 = DeviceScene("Move42", 1000,42,[[0,200],[70,150],[30,180],[70,0],[200,0],[200,255],[200,0]])        

        self._s1 = DeviceScene("Par001", 2000,1, [[255, 0, 0, 0, 0, 255, 15],[255, 0, 0, 0, 0, 255, 140],[255, 0, 0, 0, 0, 255, 230],[255, 0, 0, 0, 0, 255, 200],[255, 0, 0, 0, 0, 255, 170],[255, 0, 0, 0, 0, 255, 45]])
        self._s2 = DeviceScene("Par017", 2000,17, [[255, 0, 0, 0, 0, 255, 230],[255, 0, 0, 0, 0, 255, 200],[255, 0, 0, 0, 0, 255, 170],[255, 0, 0, 0, 0, 255, 45],[255, 0, 0, 0, 0, 255, 15],[255, 0, 0, 0, 0, 255, 140]])
        self._s3 = DeviceScene("Head33", 2000,33, [[80, 255, 0, 0, 0, 0, 0, 0, 255],[80, 255, 255, 0, 0, 0, 0, 0, 255],[80, 0, 255, 0, 0, 0, 0, 0, 255],[80, 0, 255, 255, 0, 0, 0, 0, 255],[80, 0, 0, 255, 0, 0, 0, 0, 255],[80, 0, 0, 255, 0, 0, 0, 0, 255],[80, 255, 0, 0, 0, 0, 0, 0, 255]])
        self._strobe_scene = Scene("StrobeScene", [self._s1,self._s2,self._s3, self._m1])
        self._strobe_chore = Chore("AllStrobe", [self._strobe_scene], 60000)
        
        self._chores = [self._white_chore, self._black_chore, self._strobe_chore]
        self._scenes = [self._white_scene, self._black_scene, self._strobe_scene]

    def find_all_scenes(self) -> list[Scene]:
        try:
            return self._scenes
        except Exception as e:
            print(f"Error fetching all scenes: {e}")
            return []

    def find_scenes_by_names(self, names: list[str]) -> list[Scene]:
        try:
            filtered = [scene for scene in self._scenes if scene.name in names]
            return filtered
        except Exception as e:
            print(f"Error fetching scenes by names: {e}")
            return []

    def find_chore_by_name(self, name: str) -> Optional[Chore]:
        try:
            filtered = [chore for chore in self._chores if chore.name in name]
            if len(filtered) != 1:
                return None
            
            return filtered[0]
        except Exception as e:
            print(f"Error fetching chore by name: {e}")
            return None
        
    def find_all_chores(self) -> list[str]:
        try:
            return self._chores
        except Exception as e:
            print(f"Error fetching all chores: {e}")
            return []

    def close(self):
        try:
            self.client.close()
        except Exception as e:
            print(f"Error closing connection: {e}")
