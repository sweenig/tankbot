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
           ,"   bb   "
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
           ,"   bb   "
           ,"b      b"
           ," bbbbbb "],
  "yes":   ["     b b"
           ,"   oob b"
           ,"    obbb"
           ,"gggoo b "
           ,"  g o b "
           ,"gggoo   "
           ,"g       "
           ,"ggg     "],
  "no":    ["        "
           ,"        "
           ,"rrr r  r"
           ,"r r r rr"
           ,"r r rr r"
           ,"rrr r  r"
           ,"        "
           ,"        "]
}

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
def doyes(): showface(faces["yes"])
def dono(): showface(faces["no"])
def doblank(): showface(faces["blank"])

showface(faces["smile"])
