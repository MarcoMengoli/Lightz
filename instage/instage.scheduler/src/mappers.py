from model import DeviceScene, Scene, Chore

class DeviceSceneMapper:
    @staticmethod
    def from_document(document: dict) -> DeviceScene:
        a = DeviceScene(
            name=document['name'],
            timer=document['timer'],
            base_address=document['base_address'],
            values=document['values'],
        )
        return a

class SceneMapper:
    @staticmethod
    def from_document(document: dict) -> Scene:
        device_scenes = [DeviceSceneMapper.from_document(device_scene_doc) for device_scene_doc in document.get('device_scenes', [])]
        a = Scene(document['name'], device_scenes)
        return a
    
    
class ChoreMapper:
    @staticmethod
    def from_document(document: dict, scenes: list[Scene]) -> 'Chore':
        a = Chore(document['name'], scenes, document['timer'])
        return a
