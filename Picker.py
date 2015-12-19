import maya.cmds as cmds

def WIDTH():
    return 500
    
def HEIGHT():
    return 600

# Create the window    
cmds.window(widthHeight=(WIDTH(), HEIGHT()), title="Model Picker", sizeable=False)
            
# Set the layout then set the parent back to the window
form_layout = maya.cmds.formLayout()

# Load the image from Documents/maya/2015-x64/prefs/icons
background_image = cmds.image(image="HellknightBG.png", width=WIDTH(), height=HEIGHT())
    
# Create the controls,
r_wrist_button = cmds.button(label="", w= 20, h=20, bgc=(0.2, 0.2, 1.0), command="pass")
l_wrist_button = cmds.button(label="", w= 20, h=20, bgc=(1.0, 0.2, 0.2), command="pass")
r_leg_button   = cmds.button(label="", w= 20, h=20, bgc=(0.2, 0.2, 1.0), command="pass")
l_leg_button   = cmds.button(label="", w= 20, h=20, bgc=(1.0, 0.2, 0.2), command="pass")
pelvis_button  = cmds.button(label="", w= 70, h=10, bgc=(1.0, 1.0, 1.0), command="pass")
master_button  = cmds.button(label="", w=200, h=10, bgc=(1.0, 1.0, 1.0), command="pass")

# set the parent back to the window so we can possiton our objects on the form
#cmds.setParent("..")

# Position the image in the layout
cmds.formLayout(form_layout, edit=True, attachForm=[[background_image, "left", 0],[background_image, "top", 0]])
    
# Position the controls
cmds.formLayout(form_layout, e=True, af=[[r_wrist_button,"left",100          ],[r_wrist_button,"top",220]])
cmds.formLayout(form_layout, e=True, af=[[l_wrist_button,"left",380          ],[l_wrist_button,"top",220]])
cmds.formLayout(form_layout, e=True, af=[[r_leg_button,  "left",200          ],[r_leg_button,  "top",400]])
cmds.formLayout(form_layout, e=True, af=[[l_leg_button,  "left",280          ],[l_leg_button,  "top",400]])
cmds.formLayout(form_layout, e=True, af=[[pelvis_button, "left",WIDTH()/2-35 ],[pelvis_button, "top",250]])
cmds.formLayout(form_layout, e=True, af=[[master_button, "left",WIDTH()/2-100],[master_button, "top",480]])

# display the window
cmds.showWindow()