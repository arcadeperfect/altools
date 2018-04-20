


#timewarp cam
target = nuke.selectedNode().name()
n = nuke.nodes.Camera()
n.addKnob(nuke.Array_Knob('timewarp'))

for i in ['translate','rotate','focal','haperture','vaperture','near','far']:

    n[i].setExpression("parent.{}.{}(timewarp)".format(target,i))
    n['label'].setValue("\ntimewarp\n[value timewarp]"


#offset cam


target = nuke.selectedNode().name()
n = nuke.nodes.Camera()

n.addKnob(nuke.Array_Knob('offset'))
for i in ['translate','rotate','focal','haperture','vaperture','near','far']:

    n[i].setExpression("parent.{}.{}(frame - offset)".format(target,i))
    n['label'].setValue("\noffset\n[value offset]"

