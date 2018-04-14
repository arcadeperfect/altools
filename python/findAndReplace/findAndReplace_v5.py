testPath = '/net/homes/aharding/test/'
#testPath = '/job/comms/att_dtv_distored_everything_3001368/sc060/sc060_0310/publish/'


def recursiveLoad(searchPath, fileTypes = ['exr','jpg', 'jpeg', 'dpx', 'tif', 'tiff', 'tga', 'cin', 'mov', 'hdr', 'png', 'targa', 'xpm']):

    reads = search(testPath, fileTypes)
    print 'recload', fileTypes    
    for i in reads:
        n = nuke.nodes.Read(file = i.fullNukeString())
        first = i.first
        last = i.last
        if first != None and i.type not in ['mov']:
            n['first'].setValue(int(first))
            n['last'].setValue(int(last))



recursiveLoad(testPath, ['dpx'])