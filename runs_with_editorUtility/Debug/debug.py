import struct
import unreal 

eal = unreal.EditorAssetLibrary 

asset_lists :list                  = unreal.EditorUtilityLibrary.get_selected_assets()
asset :object                      = asset_lists[0]
each :struct                       = asset.materials[0]
masked :struct                     = unreal.BlendMode.cast(1) # static enum UBlendMode[1] = BlendMode::Masked
MI :object                         = each.material_interface
MI_overridable_properties :struct  = MI.get_editor_property('base_property_overrides')
#MI_lightmass_setting        = MI.get_editor_property('lightmass_settings')

MI_overridable_properties.set_editor_property( 'override_blend_mode', True )

blend_mode = MI_overridable_properties.get_editor_property('override_blend_mode')

MI_overridable_properties.set_editor_property('override_two_sided', True)
MI_overridable_properties.set_editor_property('two_sided', True)

### 이거 돌리면 엔진 죽음 why? ###
MI_overridable_properties.set_editor_property('blend_mode', masked)
### 이거 돌리면 엔진 죽음 why? ###
#### 무조건 Serialize 해야함  -> PY에 serialize 있나? 

