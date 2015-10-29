import maya.cmds as cmds

# get a list of the selected joints
selected_joints = cmds.ls(selection=True, type="joint")

if len(selected_joints) > 0 :
    # create strings with ctrl and grp prefixs instead of jnt
    joint_name       = selected_joints[0]
    ctrl_shape_namne = "ctrl" + joint_name[3:]
    grp_name         = "grp" + joint_name[3:]
    constraint_name  = joint_name + "_pin_constraint"

    print( "\nJoints Selected: " + str(len(selected_joints)) )
    print( joint_name )
    print( ctrl_shape_namne )
    print( grp_name )

    # create the control shape
    cmds.circle( nr=(0,1,0), c=(0,0,0), name=ctrl_shape_namne )
    
    # create the group and parent it to the seleced joint
    cmds.group( empty=True, name=grp_name, parent=joint_name )    

    # parent the shape to the group
    # the translation and rotation of the shape should be implicitly zero when relative=True
    cmds.parent( ctrl_shape_namne, grp_name, relative=True )
    
    # unparent the shape
    cmds.parent( grp_name, world=True )
    
    # constain the shape to the parent, currently using a parent constraint
    # could change this to a orient or aim constraint based on user input
    cmds.parentConstraint( ctrl_shape_namne, joint_name, name=constraint_name )
    
else:
    print( "No Joint Selected!" )