### DELETE NODES WITH NO DEPENDENCIES

if len(nuke.selectedNodes())==0:
    nuke.message("IT IS IMPERATIVE THAT YOU SELECT SOME NODES")
else:
    if nuke.ask("WOULD YOU LIKE TO DELETE ALL NODES WITHOUT DEPENDENCIES?"):
        
        exclude = ['BackdropNode','Viewer']
        if not nuke.ask("INCLUDE READ NODES?"):
            exclude.append('Read')
        for n in nuke.selectedNodes():
            if not n.Class() in exclude:
                if len(n.dependent())==0 and len(n.dependencies())==0:
                    nuke.delete(n)


### DELETE DISABLED NODES

if len(nuke.selectedNodes())==0:
    nuke.message("IT IS IMPERATIVE THAT YOU SELECT SOME NODES")
else:
    if nuke.ask("WOULD YOU LIKE TO DELETE ALL NODES THAT ARE DISABLED?"):

        exclude = ['BackdropNode','Viewer']
        
        for n in nuke.selectedNodes():
            if not n.Class() in exclude:
                for i in n.knobs():
                    if i == 'disable':
                    
                        if not n['disable'].isAnimated():
                            if n['disable'].getValue() == 1:
                                nuke.delete(n)
      
