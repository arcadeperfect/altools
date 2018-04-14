l = nuke.selectedNodes()

def deSelExcept(n):
    for i in nuke.allNodes():
        try: 
            i['selected'].setValue(0)
        except:
            pass
    n['selected'].setValue(1)
   
const = nuke.nodes.Constant()

for i in l[1:]:
    deSelExcept(i)
    r = nuke.createNode("Reconcile3D", inpanel = False)
    r.setInput(0,const)
    r.setInput(1,l[0])
    

        
