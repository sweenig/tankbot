# available colors
colors = {
  " ": (0,0,0),
  "g": (0,255,0),
  "r": (255,0,0),
  "b": (0,0,255),
  "y": (255,255,0),
  "m": (255,0,255),
  "c": (0,255,255),
  "o": (255,165,0)
}

# available faces
faces = {
  "blank": ["        "
           ,"        "
           ,"        "
           ,"        "
           ,"        "
           ,"        "
           ,"        "
           ,"        "],
  "smile": [" yy  yy "
           ,"y      y"
           ," bb  bb "
           ," bb  bb "
           ,"        "
           ,"   oo   "
           ,"b      b"
           ," bbbbbb "],
  "frown": ["yy    yy"
           ,"  y  y  "
           ," r    r "
           ,"        "
           ,"   rr   "
           ,"        "
           ," rrrrrr "
           ,"r      r"],
   "wink": [" yy     "
           ,"y    yyy"
           ," bb     "
           ," bb  bb "
           ,"        "
           ,"   oo   "
           ,"b      b"
           ," bbbbbb "],
  "whoa":  ["yy    yy"
           ," bb  bb "
           ," bb  bb "
           ,"   oo   "
           ,"        "
           ,"  bbbb  "
           ,"  b  b  "
           ,"  bbbb  "],
  "hi":    ["        ",
            ' g g    ',
            ' g g  g ',
            ' ggg    ',
            ' g g  g ',
            ' g g  g ',
            '        ',
            '        '],
  'no':    ['        ',
            '        ',
            'r  r rrr',
            'rr r r r',
            'r rr r r',
            'r  r rrr',
            '        ',
            '        '],
 'what':   ['   bbb  ',
            '  b   b ',
            '      b ',
            '     b  ',
            '    b   ',
            '        ',
            '   bb   ',
            '   bb   '],
 'yes':    ['b b     ',
            'b boo   ',
            'bbbo    ',
            ' b ooggg',
            ' b o g  ',
            '   ooggg',
            '       g',
            '     ggg']
  }
for key, value in faces.iteritems():
  if debug: print("Processing: %s" % key)
  newface = []
  for row in faces[key]:
    str = ""
    for i in row: str = i + str
    newface.append(str)
  faces[key] = newface
if debug: pprint(faces)

def showface(face):
  if debug:
    print("Face:\n")
    pprint(face)
  for h in range(height):
    for w in range(width):
      color = face[w][h]
      if debug:
        print("(h,w) = (%s,%s)" % (h,w))
        print("Pixel color: %s" % color)
        print("Pixel RGB: (%s,%s,%s)" % colors[color])
      unicorn.set_pixel(w,h,colors[face[w][h]][0],colors[face[w][h]][1],colors[face[w][h]][2])
  unicorn.show()

def dosmile(): showface(faces["smile"])
def dowink(): showface(faces["wink"])
def dofight(): showface(faces["frown"])
def doyes():
  execfile("demo.py")
  showface(faces["yes"])
def dono():
  execfile("demo.py")
  showface(faces["no"])
def doblank(): showface(faces["blank"])
def dowhoa(): showface(faces["whoa"])
def dohi(): showface(faces["hi"])
def dowhat(): showface(faces["what"])
def gocrazy():
  i=0
  while i < 20:
    showface(faces["smile"])
    showface(faces["wink"])
    showface(faces["frown"])
    showface(faces["yes"])
    showface(faces["no"])
    showface(faces["whoa"])
    showface(faces["hi"])
    showface(faces["what"])
    showface(faces["blank"])
    i += 1

def rainbow():
  execfile("rainbow.py")
  showface(faces["blank"])

def thinking():
  execfile("demo.py")
  showface(faces["blank"])


showface(faces["hi"])
sleep(3)
showface(faces["smile"])
