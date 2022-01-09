bl_info = {
    "name": "Minimise Group sockets",
    "author": "Ed O'Connell",
    "version": (1, 0, 0),
    "blender": (2, 91, 0),
    "location": "Operator",
    "description": "Adds a simple operator for collapsing group sockets. Operator name: node.minimise_group_socket.",
    "category": "Interface",
}

import bpy

def main(operator, context):
    nodes = context.selected_nodes
    CurrentState = None

    for node in nodes:
        for i in range(len(node.inputs)):
            if hasattr(node.inputs[i], 'show_group_sockets'):
                if CurrentState is None:
                    CurrentState = node.inputs[i].show_group_sockets
                node.inputs[i].show_group_sockets = not CurrentState


class MinimiseGroupSocket(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "node.minimise_group_socket"
    bl_label = "Minimise group sockets"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def execute(self, context):
        main(self, context)
        return {'FINISHED'}

def MGS_menu_func(self, context):
    self.layout.operator(MinimiseGroupSocket.bl_idname, text=MinimiseGroupSocket.bl_label)


def register():
    bpy.utils.register_class(MinimiseGroupSocket)
    bpy.types.NODE_MT_node.append(MGS_menu_func)


def unregister():
    bpy.utils.unregister_class(MinimiseGroupSocket)
    bpy.types.NODE_MT_node.remove(MGS_menu_func)


if __name__ == "__main__":
    register()
