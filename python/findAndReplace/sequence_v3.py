def isNumber(string):
    try:
        int(string)
        return True
    except:
        return False

class sequence:
    def __init__ (self, name, type, first, last, location):
        self.name = name
        self.type = type
        self.first = first
        self.last = last
        self.location = location

        if isNumber(self.first) & isNumber(self.last):
            self.duration = int(self.last) - int(self.first)
        else:
            self.duration = 0

        if isNumber(self.last) & self.duration != 0:
            self.padding = '%%0%sd' %len(str(self.last))
        else:
            self.padding = last

    def nukeString(self):
        if isNumber(self.first) & isNumber(self.last):
            #return "%s.%s.%s %s-%s" %(self.name,self.padding,self.type,self.first,self.last)
            return "%s.%s.%s" %(self.name,self.padding,self.type)
        else:
            return "%s.%s" %(self.name, self.type)

    def fullPath(self):
        if isNumber(self.first) & isNumber(self.last):
            return "%s.%s.%s" %(os.path.join(self.location,self.name),self.padding,self.type)

        else:
            return "%s.%s" %(os.path.join(self.location,self.name),self.type)

    def fullNukeString(self):
        if isNumber(self.first) & isNumber(self.last):
            #return "%s.%s.%s %s-%s" %(os.path.join(self.location,self.name),self.padding,self.type, self.first, self.last)
            return "%s.%s.%s" %(os.path.join(self.location,self.name),self.padding,self.type)
        else:
            return "%s.%s" %(os.path.join(self.location,self.name),self.type)

def findSeqs(searchPath, fileTypes = ['exr','jpg', 'jpeg', 'dpx', 'tif', 'tiff', 'tga', 'cin', 'mov', 'hdr', 'png', 'targa', 'xpm']):

    #print '\n FINDSEQS BEGIN ____________________________'

    #print fileTypes
    found = {}
    result = []
    
    for i in sorted(os.listdir(searchPath)):
        
        ext = i.split('.')[-1]
        if ext in fileTypes:
    
            frame = None
            splitted = i.split('.')
            clipName = splitted[0]

            try:
                int(splitted[-2])  # found frame numbers
                frame = splitted[-2]
            except:
                frame = None

                
            if not clipName in found.keys():
                found[clipName] = [ext,frame,frame]

            else:
                if not frame == None:

                    if int(frame) > str(found[clipName][1]):
                        found[clipName][1] = frame

                    if int(frame) < str(found[clipName][2]):
                        found[clipName][2] = frame
     
    for i in found.keys():
        name = i
        ext = found[i][0]
        first = found[i][1]
        last = found[i][2]
        location = searchPath
        result.append(sequence(name,ext,first,last,searchPath))

    return result

def search(searchPath, fileTypes = ['exr','jpg', 'jpeg', 'dpx', 'tif', 'tiff', 'tga', 'cin', 'mov', 'hdr', 'png', 'targa', 'xpm']):
    #print fileTypes
    resultz = [] # create list
    z = findSeqs(searchPath, fileTypes)
    if z:
        resultz.extend(z) # append list to list
    
    for i in os.listdir(searchPath):
        newSearch = os.path.join(searchPath, i)
        if os.path.isdir(newSearch):
            resultz += search(newSearch)
    return resultz
