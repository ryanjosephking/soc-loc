# Maybe-TODO:
#  - Add xclip support?  "Copy" is no problem, and pretty clearly a win. The
#    issue is I don't know exactly what to do on "Paste" -- which selection
#    wins out?

bl_info = {
    "name": "Social Location: 3D Cursor Sharing",
    "author": "taniwha / rking",
    "version": (1, 0),
    "blender": (2, 6, 2),
    "location": "View3D > 'n' Panel > 3D Cursor > Copy/Paste",
    "description": "Allows remote users to quickly point out locations",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"}


import bpy
import mathutils


class CursorPaste(bpy.types.Operator):
    bl_idname = 'scene.cursor_3d_paste'
    bl_label = 'Paste coordinate string from clipboard to 3D Cursor location.'

    @classmethod
    def poll(cls, context):
        return True

    def get_clip(self):
        return bpy.data.window_managers['WinMan'].clipboard

    def set_cursor_to(self, raw):
        pieces = raw.split(',')
        if (3 != len(pieces)):
            err = "'%s' doesn't look like 'x,y,z'" % raw
            self.report({'ERROR_INVALID_INPUT'}, err)
            return {'CANCELLED'}
        vec = mathutils.Vector([float(c) for c in pieces])
        bpy.context.scene.cursor_location = vec
        return {'FINISHED'}

    def execute(self, context):
        return self.set_cursor_to(self.get_clip())


class CursorCopy(bpy.types.Operator):
    bl_idname = 'scene.cursor_3d_copy'
    bl_label = 'Copy coordinate string to clipboard from 3D Cursor location.'

    @classmethod
    def poll(cls, context):
        return True

    def get_cursor(self):
        return bpy.context.scene.cursor_location

    def copy_from(self, location):
        pieces = (str(component) for component in location)
        full = ', '.join(pieces)
        bpy.data.window_managers['WinMan'].clipboard = full
        self.report({'INFO'}, full + ' in clipboard')
        return {'FINISHED'}

    def execute(self, context):
        return self.copy_from(self.get_cursor())


def menu_draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text='', icon='CURSOR')
        row.operator('scene.cursor_3d_copy', text='Copy', icon='COPYDOWN')
        row.operator('scene.cursor_3d_paste', text='Paste', icon='PASTEDOWN')


def register():
    bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_PT_view3d_cursor.append(menu_draw)


def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.VIEW3D_PT_view3d_cursor.remove(menu_draw)


if __name__ == '__main__':
    register()
