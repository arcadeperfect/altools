searchPath = '/net/homes/aharding/test'


name = 'butt'
ext = 'exr'


def isNumber(string):
    try:
        int(string)
        return True
    except:
        return False
isNumber(None)

class sequence:
    def __init__ (self, name, type, first, last, location):
        self.name = name
        self.type = type
        self.first = first
        self.last = last
        self.location = location
        if isNumber(last):
            self.padding = '%%0%sd' %len(str(int(last)))
        else:
            self.padding = None

    def nukeString(self):
        if isNumber(self.first) & isNumber(self.last):
            return "%s.%s.%s %s-%s" %(self.name,self.padding,self.type,self.first,self.last)
        else:
            return "%s.%s" %(self.name, self.type)

    def fullPath(self):
        if isNumber(self.first) & isNumber(self.last):
            return "%s.%s.%s" %(os.path.join(location,name),self.padding,ext)
        else:
            return "%s.%s" %(os.path.join(location,name),ext)

    def fullNukeString(self):
        if isNumber(self.first) & isNumber(self.last):
            return "%s.%s.%s %s-%s" %(os.path.join(location,name),self.padding,ext, self.first, self.last)
        else:
            return "%s.%s" %(os.path.join(searchPath,name),ext)

    def duration(self):
        if isNumber(self.first) & isNumber(self.last):
            return int(self.last)-int(self.first)
        else:
            return 'could not find duration'

found = {}
result = []


def findSeqs(searchPath):

    fileTypes = ['exr','jpg','dpx','mov', 'tif']
    
    #found = {}
    #result = []

    for i in sorted(os.listdir(searchPath)):
    #for i in ['test4.mov']:
        
        ext = i.split('.')[-1]
        if ext in fileTypes:
    
            frame = None
            splitted = i.split('.')
            clipName = splitted[0]
            try:
                frame = int(splitted[-2])  # found fame numbers
                  
                  
            except:
                print i, ': failed to find frame numbers'
                frame = None
    
            if not clipName in found.keys():
                found[clipName] = [ext,frame,frame]
        
            else:
                if not frame == None:
                    if frame < found[clipName][1]:
                        found[clipName][1] = frame
                    if frame > found[clipName][2]:
                        found[clipName][2] = frame
     
    for i in found.keys():
        name = i
        ext = found[i][0]
        first = found[i][1]
        last = found[i][2]
        location = searchPath

        result.append(sequence(name,ext,first,last,searchPath))

        return result

def search(searchPath):

    results = [] # create list
    z = findSeqs(searchPath)
    if z:
        results.extend(z) # append list to list
    
    for i in os.listdir(searchPath):
        newSearch = os.path.join(searchPath, i)
        if os.path.isdir(newSearch):
            results += search(newSearch)
    return results

for i in search(searchPath):
    print i.name, i.location
