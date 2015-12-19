import maya.cmds as cmds

def WIDTH():
    return 400
    
def HEIGHT():
    return 500
    
# Setup the window
window_name = cmds.window(widthHeight=(WIDTH(), HEIGHT()), title="Hellknight Picker", sizeable=False)
tab_layout = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)

## Setup the model picker tab ##
model_tab = cmds.formLayout(width=WIDTH()-20, height=HEIGHT()-80)
    
# Create the right controls
r_shoulder_btn  = cmds.iconTextButton(w= 20, h=20, bgc=(0.2, 0.2, 1.0), command="pass")
r_elbow_btn     = cmds.iconTextButton(w= 20, h=20, bgc=(0.2, 0.2, 1.0), command="pass")
r_wrist_btn     = cmds.iconTextButton(w= 20, h=20, bgc=(0.2, 0.2, 1.0), command="pass")
r_knee_btn      = cmds.iconTextButton(w= 20, h=20, bgc=(0.2, 0.2, 1.0), command="pass")
r_leg_btn       = cmds.iconTextButton(w= 20, h=20, bgc=(0.2, 0.2, 1.0), command="pass")
# Create the left controls
l_shoulder_btn  = cmds.iconTextButton(w= 20, h=20, bgc=(1.0, 0.2, 0.2), command="left")
l_elbow_btn     = cmds.iconTextButton(w= 20, h=20, bgc=(1.0, 0.2, 0.2), command="left")
l_wrist_btn     = cmds.iconTextButton(w= 20, h=20, bgc=(1.0, 0.2, 0.2), command="left")
l_knee_btn      = cmds.iconTextButton(w= 20, h=20, bgc=(1.0, 0.2, 0.2), command="left")
l_leg_btn       = cmds.iconTextButton(w= 20, h=20, bgc=(1.0, 0.2, 0.2), command="left")
# Create the mid controls
spine_btn       = cmds.iconTextButton(w= 60, h=10, bgc=(1.0, 1.0, 1.0), command="pass")
waist_btn       = cmds.iconTextButton(w= 70, h=12, bgc=(1.0, 1.0, 1.0), command="pass")
pelvis_btn      = cmds.iconTextButton(w= 90, h=12, bgc=(1.0, 1.0, 1.0), command="pass")
master_btn      = cmds.iconTextButton(w=200, h=12, bgc=(1.0, 1.0, 1.0), command="pass")

# Position the right controls
cmds.formLayout(model_tab, e=True, af=[[r_shoulder_btn, "right",WIDTH()/2+20],
                                       [r_shoulder_btn, "top",      60]])
cmds.formLayout(model_tab, e=True, af=[[r_elbow_btn,    "right",WIDTH()/2+50],
                                       [r_elbow_btn,    "top",      80]])
cmds.formLayout(model_tab, e=True, af=[[r_wrist_btn,    "right",WIDTH()/2+90],
                                       [r_wrist_btn,    "top",      120]])
cmds.formLayout(model_tab, e=True, af=[[r_knee_btn,     "right",WIDTH()/2+40],
                                       [r_knee_btn,     "bottom",   130]])
cmds.formLayout(model_tab, e=True, af=[[r_leg_btn,      "right",WIDTH()/2+40],
                                       [r_leg_btn,      "bottom",   80]])
# Position the left controls
cmds.formLayout(model_tab, e=True, af=[[l_shoulder_btn, "left", WIDTH()/2+20],
                                       [l_shoulder_btn, "top",      20]])
cmds.formLayout(model_tab, e=True, af=[[l_elbow_btn,    "left", WIDTH()/2+50],
                                       [l_elbow_btn,    "top",      60]])
cmds.formLayout(model_tab, e=True, af=[[l_wrist_btn,    "left", WIDTH()/2+90],
                                       [l_wrist_btn,    "top",      100]])
cmds.formLayout(model_tab, e=True, af=[[l_knee_btn,     "left", WIDTH()/2+40],
                                       [l_knee_btn,     "bottom",   130]])
cmds.formLayout(model_tab, e=True, af=[[l_leg_btn,      "left", WIDTH()/2+40],
                                       [l_leg_btn,      "bottom",   80]])

cmds.formLayout(model_tab, e=True, af=[[spine_btn,  "left", WIDTH()/2-30 ],[spine_btn, "bottom",HEIGHT()/2+60]])
cmds.formLayout(model_tab, e=True, af=[[waist_btn,  "left", WIDTH()/2-35 ],[waist_btn, "bottom",HEIGHT()/2]])
cmds.formLayout(model_tab, e=True, af=[[pelvis_btn, "left", WIDTH()/2-45 ],[pelvis_btn, "top",HEIGHT()/2]])
cmds.formLayout(model_tab, e=True, af=[[master_btn, "left", WIDTH()/2-100],[master_btn, "bottom",60]])

# Setup the reset buttons
resetall_btn = cmds.button(label="Reset All",      w=WIDTH()/2-20, command="pass")
resetsel_btn = cmds.button(label="Reset Selected", w=WIDTH()/2-20, command="pass")
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

# Name the tabs
cmds.setParent( tab_layout )
cmds.tabLayout( tab_layout, edit=True, tabLabel=((model_tab, 'Model'), (feet_tab, 'Feet'), (hands_tab, 'Hands')) )

# Display the window
cmds.showWindow()