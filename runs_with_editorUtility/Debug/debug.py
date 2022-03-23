import unreal 

asset_lists :list = unreal.EditorUtilityLibrary.get_selected_assets()

wraped_blend_mode = unreal.BlendMode

asset = asset_lists[0]

each = asset.materials[0]

MI = each.get_editor_property('material_interface')
MI_overridable_properties = MI.get_editor_property('base_property_overrides')
MI_overridable_properties.set_editor_property( 'override_blend_mode', True )

MI_overridable_properties.get_editor_property( 'override_blend_mode')




### 이거 돌리면 엔진 죽음 why? ###
MI_overridable_properties.set_editor_property( 'blend_mode', wraped_blend_mode.cast(1) )
### 이거 돌리면 엔진 죽음 why? ###
