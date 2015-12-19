import maya.cmds as cmds

def WIDTH():
    return 400
    
def HEIGHT():
    return 600
    
# Setup the window
window_name = cmds.window(widthHeight=(WIDTH(), HEIGHT()), title="Hellknight Picker", sizeable=False)

form_layout = cmds.formLayout()

tab_layout = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
cmds.formLayout(form_layout, edit=True, attachForm=((tab_layout, 'top', 0),
                                                    (tab_layout, 'left', 0),
                                                    (tab_layout, 'bottom', 0),
                                                    (tab_layout, 'right', 0)) )

## Setup the model picker tab
model_tab = cmds.formLayout(width=WIDTH()-20, height=HEIGHT()-80)

# Load the image from Documents/maya/2015-x64/prefs/icons on Windows
# or from ~/Library/Preferences/Autodesk/maya/2015-x64/prefs/icons on OSX
background_image = cmds.image(image="HellknightBG.png")

pelvis_button = cmds.button(label="", w= 70, h=10, bgc=(1.0, 1.0, 1.0), command="pass")
master_button = cmds.button(label="", w=200, h=10, bgc=(1.0, 1.0, 1.0), command="pass")

cmds.formLayout(model_tab, e=True, af=[[background_image, "left", 0],[background_image, "top", 0]])
cmds.formLayout(model_tab, e=True, af=[[pelvis_button,"left",WIDTH()/2- 35],[pelvis_button,"top",250]])
cmds.formLayout(model_tab, e=True, af=[[master_button,"left",WIDTH()/2-100],[master_button,"top",480]])

# Setup the reset buttons
resetall_button = cmds.button(label="Reset All",      w=WIDTH()/2-20, command="pass")
resetsel_button = cmds.button(label="Reset Selected", w=WIDTH()/2-20, command="pass")
cmds.formLayout(model_tab, e=True, af=[[resetsel_button,"left",          10],[resetsel_button,"top",HEIGHT()-60]])
cmds.formLayout(model_tab, e=True, af=[[resetall_button,"left",WIDTH()/2+10],[resetall_button,"top",HEIGHT()-60]])

## Setup the foot tab
cmds.setParent( tab_layout )
feet_tab = cmds.columnLayout( width=WIDTH() )

hl_grp = cmds.floatSliderGrp( l='Heel Lift', field=True, min=-20, max=20, value=0, cw=[(1,80),(2,60),(3,WIDTH()-160)] )
#cmds.connectControl( hl_grp, '%s.Custom' % 'pSphere1' )


## Setup the hands tab
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