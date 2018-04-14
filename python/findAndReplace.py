

searchPath ='/job/comms/att_dtv_distored_everything_3001368/sc060/sc060_0310/publish/'



def search(searchPath):

    results = [] # create list
    z = findSeqs(searchPath)
    if z:
        results.append(z) # append list to list
    
    for i in os.listdir(searchPath):
        newSearch = os.path.join(searchPath, i)
        if os.path.isdir(newSearch):
            results += search(newSearch)
    return results


### find squences

def findSeqs(searchPath):
    found = {}
    fileTypes = ['exr','jpg','dpx','mov']
    for i in os.listdir(searchPath):

        split = i.split('.')
        clipName = split[0]
        ext = split[-1]
        try:
            frame = split[-2]
            
        except:
            #print 'failed to find frame numbers'
            frame = None
            pass
        
        if ext in fileTypes:
            if not clipName in found.keys():
                found[clipName] = [ext, frame, frame, searchPath]
        
            if clipName in found.keys():
                try:
                    int(frame)
                    if frame < found[clipName][1]:
                        found[clipName][1] = frame
                    elif frame > found[clipName][2]:
                        found[clipName][2] = frame
                except:
                    #print "frame numbers weren't numbers at all"
                    pass

    if len(found) > 0:
        return found



for i in search(searchPath):
    print '\n',i
