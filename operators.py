import re
import bpy
from . import utilities


class CVShowConstraints(bpy.types.Operator):
    """ Fill up the list of the constraints. """

    bl_idname = "scene_constraints.show_constraints"
    bl_label = "show_constraints"

    def execute(self, context):
        scene_csts = dict()
        readable_csts = list()
        # check collection
        if hasattr(context.scene, 'scene_constraints'):
            context.scene.scene_constraints.clear()
        # parse scene
        for ob in bpy.context.scene.objects:
            csts = utilities.get_constraints_on_object(ob)
            for k, v in csts.items():
                scene_csts[k] = v
        # process infos - populate list
        for cst, data in scene_csts.items():
            regex = '\W\d{3}'
            cst_name = cst.name
            # SLAVE
            slave_name = data[0].name.split('_')[0]
            instance = re.search(regex, data[0].name)
            if instance:
                keep_dgt = instance.group(0)
            else:
                keep_dgt = ''
            # if object
            if data[1] == '':
                slave = '{}{}'.format(slave_name, keep_dgt)
            else:
                bone_slave = data[1].name
                slave = '{}{}-{}'.format(slave_name, keep_dgt, bone_slave)
            # TARGET
            tgtinfos = data[-1]
            if tgtinfos['target']:
                instance_tgt = re.search(regex, tgtinfos['target'].name)
                if instance_tgt:
                    target_dgt = instance_tgt.group(0)
                else:
                    target_dgt = ''
                if tgtinfos['target']:
                    target_name = tgtinfos['target'].name.split('_')[0]
                if tgtinfos['subtarget']:
                    bone_target = tgtinfos['subtarget']
                    target = '{}{}-{}'.format(target_name, target_dgt, bone_target)
                else:
                    target = '{}{}'.format(target_name, target_dgt)
            else:
                target = 'EMPTY'

            read_cst = '{} has a {} constraint: target is {}'.format(slave, cst_name, target)
            readable_csts.append(read_cst)

        # if empty list
        if len(readable_csts) == 0:
            empty_read = "no constraints found in the scene"
            readable_csts.append(empty_read)
        # populate UI list
        for i, phrase in enumerate(readable_csts):
            item = context.scene.scene_constraints.add()
            item.id = i
            item.name = phrase
        return {'FINISHED'}