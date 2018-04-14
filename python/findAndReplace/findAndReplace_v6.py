searchPath = '/job/comms/att_dtv_distored_everything_3001368/reference/in/artwork/180327_PM/'


errorReads = []

for r in nuke.allNodes("Read"):
    if r.treeHasError():
        errorReads.append(r)

foundReads = search(searchPath)


for i in errorReads:
    name = os.path.basename(i['file'].getValue()).split('.')[0]
    for f in foundReads:
        if name == f.name:
            i['file'].setValue( f.fullNukeString())
