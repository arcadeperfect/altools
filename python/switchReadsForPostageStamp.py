masterNode = nuke.selectedNode()

ignoreList = ['xpos', 'ypos', 'name', 'selected', 'SG_NOTES', 'icon']


def compareNodes(ignoreList, masterNode, targetNode):
    for i in masterNode.knobs():
        if not i in ignoreList:
            if masterNode[i].getValue() != targetNode.knobs()[i].getValue():
                #print i, 'did not match'
                return False
        
        #else: 
            #print i, 'in ingnore list'
    return True
        

def switchRead(node, master):
    
    p = nuke.nodes.PostageStamp()
    
    for i in ['xpos', 'ypos']:
        p[i].setValue(node[i].getValue())
        p.setInput(0,master)
        p['hide_input'].setValue(1)
        p['postage_stamp'].setValue(1)
    
    for dep in node.dependent():
        for x, input in enumerate(dep.dependencies()):
            print '    input', x, input.name()
            if input == node:     
                print dep.name()     
                dep.setInput(x,p)
    


for i in nuke.allNodes("Read"):

    if not i == masterNode:
        if compareNodes(ignoreList, masterNode, i):
            switchRead(i, masterNode)
            nuke.delete(i)


