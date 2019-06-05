import bpy


def get_users(obj, types=(bpy.types.Object, bpy.types.Armature)):
    """ get users of the given types """
    users = list()
    object_users = list(list(bpy.data.user_map(subset=[obj]).values())[0])
    for user in object_users:
        for user_type in types:
            if isinstance(user, user_type):
                users.append(user)
    return users


def get_constraint_bones(armature):
    """ get all bones with a constraint in the given armature """
    bones = list()
    for bone in armature.pose.bones:
        if bone.constraints:
            bones.append(bone)
    return bones


def get_constraints_on_object(object):
    """ get external constraints pointing to object """
    constraints = dict()
    type_list = ['OBJECT', 'MESH', 'EMPTY']

    slaves = get_users(object)
    for slave in slaves:
        if slave.type == 'ARMATURE':
            bones = get_constraint_bones(slave)
            for bone in bones:
                for cst in bone.constraints:
                    cst_data = dict_visual_props(cst)
                    try:
                        if getattr(cst, 'target') != slave:
                            constraints[cst] = (slave, bone, cst_data)
                    except AttributeError:
                        pass
        if slave.type in type_list:
            for cst in slave.constraints:
                cst_data = dict_visual_props(cst)
                try:
                    if getattr(cst, 'target') != slave:
                        constraints[cst] = (slave, '', cst_data)
                except AttributeError:
                    pass
    return constraints


def dict_visual_props(obj, hidden_props=None, readonly_props=None):
    """
    store constraint data in a dict
    hidden_props= list of props you still need, even if hidden or readonly
    :param obj: from which you want properties
    :param hidden_props: list of props you still need, even if hidden
    :param readonly_props: list of props you still need, even if readonly
    :return: dict of properties and values
    """
    tgtinfos = dict()
    if not hidden_props:
        # we always need type
        hidden_props = ['type']
    if not readonly_props:
        readonly_props = []
    for prop in dir(obj):
        try:
            if not obj.is_property_hidden(prop) and not obj.is_property_readonly(prop):
                tgtinfos[prop] = getattr(obj, prop, None)
            elif prop in hidden_props or prop in readonly_props:
                tgtinfos[prop] = getattr(obj, prop, None)
            else:
                continue
        except TypeError:
            continue
    return tgtinfos
