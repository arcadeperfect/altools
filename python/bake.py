

framerange = nuke.getFramesAndViews('get range', str(nuke.root().frameRange()))

framerange = [int(f) for f in framerange[0].split('-')]
g = nuke.thisNode()
g.begin()
t = nuke.toNode("daTrack")
for f in range(framerange[0],framerange[1]):
    for i in range(1,5):
        attr = t['track%s' %i]
        if attr.isAnimated():
            attr.animations()[0].setKey(f, attr.getValue()[0])
            attr.animations()[1].setKey(f, attr.getValue()[1])
    



