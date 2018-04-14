defaultFiles = ['exr','jpg', 'jpeg', 'dpx', 'tif', 'tiff', 'tga', 'cin', 'mov', 'hdr', 'png', 'targa', 'xpm']

def isNumber(string):
    try:
        int(string)
        return True
    except:
        return False



class sequence(object):

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

    def info(self):
        return "%s    %s    %s    %s" %(self.name, self.type, self.first, self.last)


def findSeqs(searchPath, fileTypes = defaultFiles):

    #print '\n FINDSEQS BEGIN ____________________________'

    #print fileTypes
    found = {}
    result = []
    
    for i in os.listdir(searchPath):
        
        ext = i.split('.')[-1]
        if ext in fileTypes:
    
            frame = None
            splitted = i.split('.')
            clipName = splitted[0]
            ID = clipName + ext



            try:
                int(splitted[-2])  # found frame numbers
                frame = splitted[-2]
            except:
                frame = None

                
            if not ID in found.keys():
                found[ID] = [ext,frame,frame, clipName]

            else:
                if not frame == None:

                    if int(frame) < int(found[ID][1]):
                        found[ID][1] = frame

                    if int(frame) > int(found[ID][2]):
                        found[ID][2] = frame
     
    for i in found.keys():
        name = found[i][3]
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


def recursiveLoad(searchPath, fileTypes = defaultFiles):
    
    reads = search(searchPath, fileTypes)

    if len(nuke.allNodes()) > 0:
        x = max([node['xpos'].getValue() for node in nuke.allNodes()]) + 200 
        y = max([node['ypos'].getValue() for node in nuke.allNodes()]) + 200

    else:
        x = 0
        y = 0
 
    origX = x
    lastRead = None
    offset = 150        

    for read in reads:

        print read.name, read.type
        print x, y
        print read.fullNukeString()
        print '\n'

        n = nuke.nodes.Read()


        if read.type in ['mov']:
            n['file'].fromUserText(read.fullNukeString())
        else:
            n['file'].setValue(read.fullNukeString())            


        first = read.first
        last = read.last
        if first != None and read.type not in ['mov']:
            n['first'].setValue(int(first))
            n['last'].setValue(int(last))

        n.setXYpos(int(x),int(y))
        if lastRead != None:
            if read.location == lastRead.location:
                x += offset
            else:
                x = origX
                y += offset
        else:
            x += offset

        lastRead = read
