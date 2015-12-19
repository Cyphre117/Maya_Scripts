import maya.cmds as cmds

def WIDTH():
    return 400
    
def HEIGHT():
    return 500
    
# A list of attributes that should be reset on control shapes ...
# ... one of the reset buttons is pressed
attributes_to_reset = ['translateX', 'translateY', 'translateZ',
                       'rotateX', 'rotateY', 'rotateZ',
                       'Pinky_Curl', 'Mid_Curl', 'Index_Curl',
                       'Thumb_Curl', 'Thumb_Side', 'Spread', 'All_Curl']
    
# Resets the attributes of the currently selected control shape
def reset_selected_ctrl(*args):
    selection = cmds.ls(selection=True)
    ctrl = [c for c in selection if 'ctrl_' in c]
    # Check there was a contol shape selected
    if len(ctrl) == 0:
        cmds.confirmDialog(title='Reset Control Shapes', message='Select a control to reset', button='Ok')
        return
    # Create a list of attributes to reset
    name = ctrl[0]
    # if the attribute exists, and is settable, reset it
    for attr in attributes_to_reset:
        if cmds.attributeQuery(attr, node=name, exists=True) == True:
            if cmds.getAttr(name+'.'+attr, settable=True) == True:
                cmds.setAttr(name+'.'+attr, 0.0)
                print(attr+" reset")
            else:
                print(attr+" not settable")
        else:
            print(attr+" not found")        

# Resets the attributes of all control shapes
def reset_all_ctrls(*args):
    transforms = cmds.ls(exactType="transform")
    ctrls = [c for c in transforms if 'ctrl_'  in c]
    if len(ctrls) == 0:
        cmds.confirmDialog(title='Reset Control Shapes', message='No control shapes found, check the debug tab', button='OK')
        return
    # loop through all the found control shapes
    for ctrl in ctrls:
        # if the attribute exists, and is settable, reset it
        for attr in attributes_to_reset:
            if cmds.attributeQuery(attr, node=ctrl, exists=True) == True:
                if cmds.getAttr(ctrl+'.'+attr, settable=True) == True:
                    cmds.setAttr(ctrl+'.'+attr, 0.0)
    print("------------------------------------")
    print("Finished reseting all control shapes")
    
# Setup the window
window_name = cmds.window(widthHeight=(WIDTH(), HEIGHT()), title="Hellknight Picker", sizeable=False)
tab_layout = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)

## Setup the model picker tab ##
model_tab = cmds.formLayout(width=WIDTH()-20, height=HEIGHT()-80)
    
# Create the right controls
r_shoulder_btn  = cmds.iconTextButton(w= 20, h=20, bgc=(1.0, 0.2, 0.2), command="cmds.select('ctrl_R_arm_shoulder')", ann='ctrl_R_arm_shoulder')
r_elbow_btn     = cmds.iconTextButton(w= 15, h=15, bgc=(1.0, 0.2, 0.2), command="cmds.select('ctrl_R_arm_elbow')", ann='ctrl_R_arm_elbow')
r_wrist_btn     = cmds.iconTextButton(w= 20, h=20, bgc=(1.0, 0.2, 0.2), command="cmds.select('ctrl_R_arm_wrist')", ann='ctrl_R_arm_wrist')
r_knee_btn      = cmds.iconTextButton(w= 15, h=15, bgc=(1.0, 0.2, 0.2), command="cmds.select('ctrl_R_leg_knee')", ann='ctrl_R_leg_knee')
r_ankle_btn     = cmds.iconTextButton(w= 20, h=20, bgc=(1.0, 0.2, 0.2), command="cmds.select('ctrl_R_leg_ankle')", ann='ctrl_R_leg_ankle')
# Create the left controls
l_shoulder_btn  = cmds.iconTextButton(w= 20, h=20, bgc=(0.0, 0.2, 1.0), command="cmds.select('ctrl_L_arm_shoulder')", ann='ctrl_L_arm_shoulder')
l_elbow_btn     = cmds.iconTextButton(w= 15, h=15, bgc=(0.0, 0.2, 1.0), command="cmds.select('ctrl_L_arm_elbow')", ann='ctrl_L_arm_elbow')
l_wrist_btn     = cmds.iconTextButton(w= 20, h=20, bgc=(0.0, 0.2, 1.0), command="cmds.select('ctrl_L_arm_wrist')", ann='ctrl_L_arm_wrist')
l_knee_btn      = cmds.iconTextButton(w= 15, h=15, bgc=(0.0, 0.2, 1.0), command="cmds.select('ctrl_L_leg_knee')", ann='ctrl_L_leg_knee')
l_leg_btn       = cmds.iconTextButton(w= 20, h=20, bgc=(0.0, 0.2, 1.0), command="cmds.select('ctrl_L_leg_ankle')", ann='ctrl_L_leg_ankle')
# Create the mid controls
spine_top_btn   = cmds.iconTextButton(w= 60, h=10, bgc=(1.0, 1.0, 1.0), command="cmds.select('ctrl_spine_top')", ann='ctrl_spine_top')
spine_mid_btn   = cmds.iconTextButton(w= 50, h=10, bgc=(1.0, 1.0, 1.0), command="cmds.select('ctrl_spine_mid')", ann='ctrl_spine_mid')
spine_bot_btn   = cmds.iconTextButton(w= 70, h=12, bgc=(1.0, 1.0, 1.0), command="cmds.select('ctrl_spine_bot')", ann='ctrl_spine_bot')
root_btn        = cmds.iconTextButton(w= 90, h=12, bgc=(1.0, 1.0, 1.0), command="cmds.select('ctrl_body_root')", ann='ctrl_body_root')
master_btn      = cmds.iconTextButton(w=200, h=12, bgc=(1.0, 1.0, 1.0), command="cmds.select('ctrl_master')", ann='ctrl_master')

# Position the right controls
cmds.formLayout(model_tab, e=True, af=[[r_shoulder_btn, "right",WIDTH()/2+20],
                                       [r_shoulder_btn, "top",      60]])
cmds.formLayout(model_tab, e=True, af=[[r_elbow_btn,    "right",WIDTH()/2+50],
                                       [r_elbow_btn,    "top",      80]])
cmds.formLayout(model_tab, e=True, af=[[r_wrist_btn,    "right",WIDTH()/2+90],
                                       [r_wrist_btn,    "top",      120]])
cmds.formLayout(model_tab, e=True, af=[[r_knee_btn,     "right",WIDTH()/2+40],
                                       [r_knee_btn,     "bottom",   130]])
cmds.formLayout(model_tab, e=True, af=[[r_ankle_btn,    "right",WIDTH()/2+40],
                                       [r_ankle_btn,    "bottom",   80]])
# Position the left controls
cmds.formLayout(model_tab, e=True, af=[[l_shoulder_btn, "left", WIDTH()/2+20],
                                       [l_shoulder_btn, "top",      60]])
cmds.formLayout(model_tab, e=True, af=[[l_elbow_btn,    "left", WIDTH()/2+50],
                                       [l_elbow_btn,    "top",      80]])
cmds.formLayout(model_tab, e=True, af=[[l_wrist_btn,    "left", WIDTH()/2+90],
                                       [l_wrist_btn,    "top",      120]])
cmds.formLayout(model_tab, e=True, af=[[l_knee_btn,     "left", WIDTH()/2+40],
                                       [l_knee_btn,     "bottom",   130]])
cmds.formLayout(model_tab, e=True, af=[[l_leg_btn,      "left", WIDTH()/2+40],
                                       [l_leg_btn,      "bottom",   80]])

cmds.formLayout(model_tab, e=True, af=[[spine_top_btn,  "left", WIDTH()/2-30 ],[spine_top_btn, "top",100]])
cmds.formLayout(model_tab, e=True, af=[[spine_mid_btn,  "left", WIDTH()/2-25 ],[spine_mid_btn, "bottom",HEIGHT()/2+60]])
cmds.formLayout(model_tab, e=True, af=[[spine_bot_btn,  "left", WIDTH()/2-35 ],[spine_bot_btn, "bottom",HEIGHT()/2]])
cmds.formLayout(model_tab, e=True, af=[[root_btn, "left", WIDTH()/2-45 ],[root_btn, "top",HEIGHT()/2]])
cmds.formLayout(model_tab, e=True, af=[[master_btn, "left", WIDTH()/2-100],[master_btn, "bottom",60]])

# Setup the reset buttons
resetall_btn = cmds.button(label="Reset All",      w=WIDTH()/2-20, command=reset_all_ctrls)
resetsel_btn = cmds.button(label="Reset Selected", w=WIDTH()/2-20, command=reset_selected_ctrl)
cmds.formLayout(model_tab, e=True, af=[[resetsel_btn,"left",  10],[resetsel_btn,"bottom",10]])
cmds.formLayout(model_tab, e=True, af=[[resetall_btn,"right", 10],[resetall_btn,"bottom",10]])

## Setup the foot tab ##
cmds.setParent( tab_layout )
feet_tab = cmds.columnLayout( width=WIDTH() )

hl_grp = cmds.floatSliderGrp( l='Heel Lift', field=True, min=-20, max=20, value=0, cw=[(1,80),(2,60),(3,WIDTH()-160)] )
#cmds.connectControl( hl_grp, '%s.Custom' % 'pSphere1' )

## Setup the hands tab ##
cmds.setParent( tab_layout )
hands_tab = cmds.columnLayout( width=WIDTH(), adjustableColumn=True )

cmds.separator(style="in", height=10)
cmds.text(label="Left Hand", align="center", height=20)
cmds.separator(style="out", height=10)

# Setup sliders for left hand attributes
acl_grp = cmds.floatSliderGrp( l='All Curl', field=True, min=-20, max=20, value=0, cw=[(1,80),(2,60),(3,WIDTH()-160)] )
cmds.connectControl( acl_grp, '%s.All_Curl' % 'ctrl_L_arm_wrist' )
pcl_grp = cmds.floatSliderGrp( l='Pinky Curl', field=True, min=-20, max=20, value=0, cw=[(1,80),(2,60),(3,WIDTH()-160)] )
cmds.connectControl( pcl_grp, '%s.Pinky_Curl' % 'ctrl_L_arm_wrist' )
mcl_grp = cmds.floatSliderGrp( l='Middle Curl', field=True, min=-20, max=20, value=0, cw=[(1,80),(2,60),(3,WIDTH()-160)] )
cmds.connectControl( mcl_grp, '%s.Mid_Curl' % 'ctrl_L_arm_wrist' )
icl_grp = cmds.floatSliderGrp( l='Index Curl', field=True, min=-20, max=20, value=0, cw=[(1,80),(2,60),(3,WIDTH()-160)] )
cmds.connectControl( icl_grp, '%s.Index_Curl' % 'ctrl_L_arm_wrist' )
tcl_grp = cmds.floatSliderGrp( l='Thumb Curl', field=True, min=-20, max=20, value=0, cw=[(1,80),(2,60),(3,WIDTH()-160)] )
cmds.connectControl( tcl_grp, '%s.Thumb_Curl' % 'ctrl_L_arm_wrist' )
tsi_grp = cmds.floatSliderGrp( l='Thumb Side', field=True, min=-20, max=20, value=0, cw=[(1,80),(2,60),(3,WIDTH()-160)] )
cmds.connectControl( tsi_grp, '%s.Thumb_Side' % 'ctrl_L_arm_wrist' )
spr_grp = cmds.floatSliderGrp( l='Spread', field=True, min=-20, max=20, value=0, cw=[(1,80),(2,60),(3,WIDTH()-160)] )
cmds.connectControl( spr_grp, '%s.Spread' % 'ctrl_L_arm_wrist' )

cmds.separator(style="in", height=10)
cmds.text(label="Right Hand", align="center", height=20)
cmds.separator(style="out", height=10)

# Setup sliders for right hand attributes
acl_grp = cmds.floatSliderGrp( l='All Curl', field=True, min=-20, max=20, value=0, cw=[(1,80),(2,60),(3,WIDTH()-160)] )
cmds.connectControl( acl_grp, '%s.All_Curl' % 'ctrl_R_arm_wrist' )
pcl_grp = cmds.floatSliderGrp( l='Pinky Curl', field=True, min=-20, max=20, value=0, cw=[(1,80),(2,60),(3,WIDTH()-160)] )
cmds.connectControl( pcl_grp, '%s.Pinky_Curl' % 'ctrl_R_arm_wrist' )
mcl_grp = cmds.floatSliderGrp( l='Middle Curl', field=True, min=-20, max=20, value=0, cw=[(1,80),(2,60),(3,WIDTH()-160)] )
cmds.connectControl( mcl_grp, '%s.Mid_Curl' % 'ctrl_R_arm_wrist' )
icl_grp = cmds.floatSliderGrp( l='Index Curl', field=True, min=-20, max=20, value=0, cw=[(1,80),(2,60),(3,WIDTH()-160)] )
cmds.connectControl( icl_grp, '%s.Index_Curl' % 'ctrl_R_arm_wrist' )
tcl_grp = cmds.floatSliderGrp( l='Thumb Curl', field=True, min=-20, max=20, value=0, cw=[(1,80),(2,60),(3,WIDTH()-160)] )
cmds.connectControl( tcl_grp, '%s.Thumb_Curl' % 'ctrl_R_arm_wrist' )
tsi_grp = cmds.floatSliderGrp( l='Thumb Side', field=True, min=-20, max=20, value=0, cw=[(1,80),(2,60),(3,WIDTH()-160)] )
cmds.connectControl( tsi_grp, '%s.Thumb_Side' % 'ctrl_R_arm_wrist' )
spr_grp = cmds.floatSliderGrp( l='Spread', field=True, min=-20, max=20, value=0, cw=[(1,80),(2,60),(3,WIDTH()-160)] )
cmds.connectControl( spr_grp, '%s.Spread' % 'ctrl_R_arm_wrist' )

## Setup debug tab
cmds.setParent( tab_layout )
debug_tab = cmds.columnLayout( width=WIDTH(), adjustableColumn=True )

transforms_list = cmds.ls(exactType="transform", visible=True)

cmds.textScrollList( numberOfRows=24, allowMultiSelection=False, append=transforms_list )

# Name the tabs
cmds.setParent( tab_layout )
cmds.tabLayout( tab_layout, edit=True, tabLabel=((model_tab, 'Model'), (feet_tab, 'Feet'), (hands_tab, 'Hands'), (debug_tab, 'Debug')) )

# Display the window
cmds.showWindow()