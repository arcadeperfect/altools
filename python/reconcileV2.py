l = nuke.selectedNodes()

def deSelExcept(n):
    for i in nuke.allNodes():
        try: 
            i['selected'].setValue(0)
        except:
            pass
    n['selected'].setValue(1)
 
def bakeCurve( curve, first, last, inc ):
    for f in xrange( first, last, inc ):
        curve.setKey( f, curve.evaluate( f ) )
    curve.setExpression( 'curve' )
  
const = nuke.nodes.Constant()
rList = []


for i in l[1:]:
    deSelExcept(i)
    r = nuke.createNode("Reconcile3D", inpanel = False)
    r.setInput(0,const)
    r.setInput(1,l[0])
    rList.append(r)
    r['calc_output'].setValue(1)

t = nuke.nodes.Tracker3()

for x,i in enumerate(rList):
    x+=1
    t['enable%s' %x].setValue(1)
    k = 'track%s' %x
    t[k].setExpression('%s.output.x' %i.name(),0)
    t[k].setExpression('%s.output.y' %i.name(),1)
    t[k].animations()
    curves = t[k].animations()
    for z in curves:
        bakeCurve(z,1001,1144,1)