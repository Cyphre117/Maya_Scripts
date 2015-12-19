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
model_tab = cmds.formLayout(width=200, height=200)

pelvis_button = cmds.button(label="", w= 70, h=10, bgc=(1.0, 1.0, 1.0), command="pass")
master_button = cmds.button(label="", w=200, h=10, bgc=(1.0, 1.0, 1.0), command="pass")

cmds.formLayout(model_tab, e=True, af=[[pelvis_button,"left",WIDTH()/2- 35],[pelvis_button,"top",250]])
cmds.formLayout(model_tab, e=True, af=[[master_button,"left",WIDTH()/2-100],[master_button,"top",480]])

# Setup the reset buttons
resetall_button = cmds.button(label="Reset All",      w=WIDTH()/2-20, command="pass")
resetsel_button = cmds.button(label="Reset Selected", w=WIDTH()/2-20, command="pass")
cmds.formLayout(model_tab, e=True, af=[[resetsel_button,"left",          10],[resetsel_button,"top",HEIGHT()-60]])
cmds.formLayout(model_tab, e=True, af=[[resetall_button,"left",WIDTH()/2+10],[resetall_button,"top",HEIGHT()-60]])

## Setup the foot tab
cmds.setParent( tab_layout )
feet_tab = cmds.rowColumnLayout(numberOfColumns=3,
                                columnWidth=[(1, WIDTH()/5), (2, WIDTH()/5*3), (3, WIDTH()/5)],
                                columnAttach=[(1, 'both', 0), (2, 'both', 10), (3, 'both', 10)])

cmds.text(label="Heel Lift", align="right")
cmds.floatSlider()
cmds.button(label="Reset")
cmds.text(label="Toe Lift", align="right")
cmds.floatSlider()
cmds.button(label="Reset")

## Setup the hands tab
cmds.setParent( tab_layout )
hands_tab = cmds.rowColumnLayout(numberOfColumns=2)

cmds.button()
cmds.button()
cmds.button()
cmds.intSlider()

# Name the tabs
cmds.setParent( tab_layout )
cmds.tabLayout( tab_layout, edit=True, tabLabel=((model_tab, 'Model'), (feet_tab, 'Feet'), (hands_tab, 'Hands')) )

# Display the window
cmds.showWindow()