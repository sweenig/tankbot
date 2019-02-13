import demo
import unicornhat as unicorn
from time import sleep
from pprint import pprint

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.5)
u_width,u_height = unicorn.get_shape()

# available colors
colors = {
  " ": (0,0,0),
  "g": (0,255,0),
  "r": (255,0,0),
  "b": (0,0,255),
  "y": (255,255,0),
  "m": (255,0,255),
  "c": (0,255,255),
  "o": (255,165,0),
  "w": (255,255,255)
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
            '     ggg'],
 'ok':     ['www     ',
            'w w     ',
            'w w     ',
            'w w w  w',
            'www w w ',
            '    ww  ',
            '    w w ',
            '    w  w']
  }
for key, value in faces.iteritems():
  newface = []
  for row in faces[key]:
    str = ""
    for i in row: str = i + str
    newface.append(str)
  faces[key] = newface

def showface(face):
  for h in range(u_height):
    for w in range(u_width):
      color = face[w][h]
      unicorn.set_pixel(w,h,colors[face[w][h]][0],colors[face[w][h]][1],colors[face[w][h]][2])
  unicorn.show()
def dosmile(): showface(faces["smile"])
def dowink(): showface(faces["wink"])
def dofight(): showface(faces["frown"])
def doblank(): showface(faces["blank"])
def dowhoa(): showface(faces["whoa"])
def dohi(): showface(faces["hi"])
def dowhat(): showface(faces["what"])
def gocrazy():
  i=0
  while i < 200:
    for key,value in faces.iteritems():
      showface(value)
      i += 1
  showface(faces["frown"])
def rainbow():
  execfile("rainbow.py")
  showface(faces["smile"])
def doswirl():
  demo.demo(demo.effects[0],50)
  showface(faces["smile"])
def dochecker():
  demo.demo(demo.effects[1],50)
  showface(faces["smile"])
def doblues_and_twos():
  demo.demo(demo.effects[2],50)
  showface(faces["smile"])
def dorainbow_search():
  demo.demo(demo.effects[3],50)
  showface(faces["smile"])
def dotunnel():
  demo.demo(demo.effects[4],50)
  showface(faces["smile"])
def dook():
  showface(faces["ok"])
def dono():
  rainbow()
  showface(faces["no"])
def doyes():
  rainbow()
  showface(faces["yes"])

actions = {
    49: dosmile, #1
    50: dowink,  #2
    51: dofight, #3
    52: gocrazy, #4
    53: rainbow, #5
    54: doswirl, #6
    55: dochecker, #7
    56: doblues_and_twos, #8
    57: dorainbow_search, #9
    48: dotunnel, #0
    121: doyes, #y
    110: dono, #n
    32: doblank, #[space bar]
    111: dowhoa, #o
    47: dowhat, #/
    104: dohi, #h
    107: dook #k
}

#showface(faces["hi"])
#sleep(3)
#showface(faces["smile"])
