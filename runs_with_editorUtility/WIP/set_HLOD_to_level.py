import unreal 
from typing import List

temp1 :object = unreal.EditorLevelLibrary.get_editor_world()


temp2 :object = temp1.get_world_settings()

temp3 :object = temp2.get_editor_property('enable_hierarchical_lod_system')


temp2.set_editor_property('enable_hierarchical_lod_system', True)