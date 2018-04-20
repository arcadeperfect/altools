def disableMBF():

    for i in nuke.allNodes():
        if 'MBF' in i.name():
            i['disable'].setValue(1)