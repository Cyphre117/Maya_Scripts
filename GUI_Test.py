import maya.cmds as cmds

# define the functions before passing them as function objects to the buttons
# functions should take *args because UI elements pass some number of arguments depending on
# what type of element they are and their current state, or something like that...
# see -> http://download.autodesk.com/us/maya/2011help/PyMel/ui.html#function-name-as-string
def say_hello(*args):
    number = 123
    # numbers have to be converted to strings explicitly with the str() function
    print("Testing testing, "+str(number)+"..."+"\nHello!")
    
def count_joints(*args):
    # the ls command return a list of all objects in the scene
    # filtered by the passed parameters
    joints = cmds.ls(type="joint")
    # len gets the length of the list
    joint_count = str(len(joints))
    print(joint_count + " joints found")
    
def reset_joints(*args):
    print("TODO: zero out the transform on all the joints")

# width and height of the window
def WIDTH():
    return 200
    
def HEIGHT():
    return 500

# TODO: Remove windows with the same title


# create the window, specify the width and height in pixels
cmds.window(widthHeight=(WIDTH(), HEIGHT()),
            title="it's a window",
            sizeable=True)

# set the layout of the window that was just created
clayout = cmds.columnLayout(adjustableColumn=True, rowSpacing=8)

# a simple text label
cmds.text(label="These may not work", align="center")

# add some UI elements to the window
cmds.button(label="hello button", command=say_hello)
cmds.separator(style="single")
cmds.button(label="count the joints", command=count_joints)
cmds.separator(style="double")
cmds.button(label="reset the joints", command=reset_joints)
cmds.separator(style="in")
cmds.checkBox(label="save the world")
cmds.separator(style="out")

# make a new layout which is a child of the previous layout
cmds.rowLayout(numberOfColumns=2,
               columnWidth2=(WIDTH()/2, WIDTH()/2),
               adjustableColumn=2,
               columnAttach=[(1, 'both', 0), (2, 'both', 0)])

cmds.button(label="buy bitcoin")
cmds.intField()

# revert back to the previously specified layout
cmds.setParent("..")

cmds.rowLayout(numberOfColumns=2,
               columnWidth=(1, WIDTH()/2),
               adjustableColumn=2,
               columnAttach=[(1, 'both', 0), (2, 'both', 0)])

cmds.button(label="sell bitcoin", enable=False)
cmds.intField()

cmds.setParent("..")

# pass the layout back to cmds.columnLayout to change properties
cmds.columnLayout( clayout, adjustableColumn=True, rowSpacing=2)

cmds.text(label="left", align="left")
cmds.text(label="center", align="center")
cmds.text(label="right", align="right")
cmds.separator()
cmds.text(label="it's a slider")
cmds.intSlider()

cmds.setParent("..")

# text is right justified, button is static, field stretches to fill window
cmds.rowLayout(numberOfColumns=3,
               columnWidth3=(80, 75, 150),
               adjustableColumn=2,
               columnAlign=(1, 'right'),
               columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )
cmds.text(label="Right Aligned")
cmds.button(label="stretchy")
cmds.intField()

cmds.setParent("..")

# text can be linked
cmds.text(label="Made by Tom")
cmds.text(label="http://www.thomashope.co.uk", hyperlink=True)

# you have to do this to see the window that was created
cmds.showWindow()
