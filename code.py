print("Starting keyboard")
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.layers import Layers
from kmk.modules.combos import Combos, Chord, Sequence
	combos = Combos()
from kmk.modules.modtap import ModTap
	modtap = ModTap()
from kmk.modules.oneshot import OneShot
	oneshot = OneShot()
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.international import International
	

keyboard = KMKKeyboard()


keyboard.modules.append(Layers())
keyboard.modules.append(combos)
keyboard.modules.append(modtap)
keyboard.modules.append(oneshot)
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(International())

print(dir(board))
print(dir(keyboard))
print(dir(keyboard.matrix))

keyboard.row_pins = (board.D1,)
keyboard.col_pins = (board.A0, board.A1, board.A2, board.A3, board.D10, board.MOSI, board.MISO, board.CLK)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


# Hold to change layer keys:
LAYER_3_KEY = KC.LT(3, KC.T) #
LAYER_1_KEY = KC.LT(1, KC.D) #
LAYER_2_KEY = KC.LT(2, KC.E) #
LAYER_4_KEY = KC.LT(4, KC.S) #

# Default layer change keys.
DF_NAV  = KC.DF(5)   # Nav Layer
DF_BASE = KC.DF(0)   # Base Layer


### Keymap definition ###
keyboard.keymap = [
    # 0 - BASE Layer
    [LAYER_1_KEY, KC.A,  KC.R,  LAYER_3_KEY, 	# D:A:R:T
     LAYER_4_KEY, KC.I,  KC.N,  LAYER_2_KEY,], 	# S:I:N:E

    # 1 - NUM Layer
    [KC.TRNS, KC.N3, KC.N2, KC.N1,		# :3:2:1
     KC.NO,   KC.N6, KC.N5, KC.N4],		# :6:5:4

    # 2 - SYMBOL Layer
    [KC.NUHS,  RALT(KC.E), KC.NUBS, KC.EXLM,	# #:€:\:!
     KC.NO, RALT(KC.A) , KC.QUES, KC.NO],		# :@:?:

    # 3 - PARENS Layer - currently unused
    [KC.NO, KC.NO, KC.NO, KC.NO,	# }:(:):
     KC.NO, KC.NO, KC.NO, KC.NO],	# {:[:]:

    # 4 - CUSTOM Layer - currently unused
    [KC.NO,   KC.NO, KC.NO,  KC.NO,	# :::
     KC.TRNS, KC.NO, KC.NO, KC.NO],	# :::

    # 5 - NAV Layer
    [KC.SCUP, KC.HOME, KC.UP,   KC.END,		# SCROLLup:HOME:UP:END
     KC.SCDN, KC.LEFT, KC.DOWN, KC.RGHT],	# SCROLLdown:LEFT:DOWN:RIGHT
]

### One Shot Keys ###
	OS_LSFT = KC.OS(KC.LSFT) #, tap_time=1000)	# OneShot left Shift
	OS_LCTL = KC.OS(KC.LCTL) #, tap_time=1000)	# OneShot left Control
	OS_LALT = KC.OS(KC.LALT) #, tap_time=1000)	# OneShot left Alt
	OS_LGUI = KC.OS(KC.LGUI) #, tap_time=1000)	# OneShot GUI
	OS_RALT = KC.OS(KC.RALT) #, tap_time=1000)	# OneShot AltGr

combos.combos = [
    #### Alpha Chords ####
                                 			#  A
	Chord((LAYER_3_KEY, LAYER_2_KEY),		KC.B),
	Chord((KC.N, LAYER_2_KEY),			KC.C),
	Chord((KC.A, KC.R, LAYER_3_KEY),		KC.D),	# legacy
                                 			#  E
	Chord((KC.R, LAYER_3_KEY),			KC.F),
	Chord((KC.A, KC.R),				KC.G),
	Chord((KC.I, LAYER_2_KEY),			KC.H),
                                 			#  I
	Chord((LAYER_1_KEY, KC.A),			KC.J),
	Chord((LAYER_4_KEY, KC.N),			KC.K),
	Chord((KC.I, KC.N, LAYER_2_KEY),		KC.L),
	Chord((LAYER_4_KEY, KC.I, KC.N),		KC.M),
	Chord((Layer_4_KEY, KC.I),			KC.N),	# legacy
	Chord((KC.A, KC.R, LAYER_2_KEY),		KC.O),
	Chord((LAYER_4_KEY, KC.I, LAYER_2_KEY),		KC.P),
	Chord((LAYER_1_KEY, KC.A, LAYER_3_KEY),		KC.Q),
                                 			#  R
                                 			#  S
                                 			#  T
	Chord((KC.I, KC.N),				KC.U),
	Chord((LAYER_1_KEY, KC.R),			KC.V),
	Chord((LAYER_1_KEY, LAYER_3_KEY),		KC.W),
	Chord((LAYER_1_KEY, KC.A, KC.R),		KC.X),
	Chord((LAYER_1_KEY, KC.I, KC.N, LAYER_3_KEY),	KC.Y),
	Chord((LAYER_1_KEY, KC.A, KC.R, LAYER_3_KEY),	KC.Z),

    #### Umlaute ###
	Chord((KC.A, LAYER_3_KEY),			KC.QUOT),	# Ä
	Chord((KC.A, LAYER_2_KEY),			KC.SCLN),	# Ö
	Chord((KC.A, KC.N),				KC.LBRC),	# Ü
	Chord((LAYER_4_KEY, KC.A),			KC.MINS),	# ß
	

    #### Symbols ####
    	Chord((KC.I, KC.N, LAYER_3_KEY),	KC.DQT),	# Anführungszeichen
    	Chord((KC.N, LAYER_3_KEY),         	KC.DOT),	# Punkt
    	Chord((KC.I, LAYER_3_KEY),         	KC.COMM),	# Komma
    	Chord((LAYER_4_KEY, LAYER_3_KEY),       LSFT(KC.N7)),	# Slash
    
    #### Numeric Chords ####
    	Chord((KC.N1, KC.N2), 	KC.N7),		# 7
    	Chord((KC.N2, KC.N3), 	KC.N8),		# 8
    	Chord((KC.N4, KC.N5), 	KC.N9),		# 9
    	Chord((KC.N5, KC.N6), 	KC.N0),		# 0
    	Chord((KC.N2, KC.N4), 	KC.BSPC),	# Backspace

    #### Other Chords ####
## Base layer Chords ##  
    	Chord((LAYER_4_KEY, KC.I, KC.N, LAYER_2_KEY), 	KC.SPACE),    	# Base Layer: Space
    	Chord((LAYER_4_KEY, KC.R, LAYER_3_KEY),       	KC.ESC), 	      # Base Layer: Esc
    	Chord((LAYER_3_KEY, LAYER_2_KEY),             	KC.ENT),	      # Base Layer: Enter
    	Chord((LAYER_4_KEY, KC.A, KC.R, LAYER_3_KEY), 	KC.TAB),	      # Base Layer: Tab
    	Chord((LAYER_2_KEY, KC.R),              	KC.BSPC),      	      # Base Layer: Backspace
    	Chord((KC.I, KC.R),               		KC.DEL),     	            # Base Layer: Delete
	    Chord((LAYER_4_KEY, KC.I, KC.N, LAYER_3_KEY),	KC.LCAP), 	      # Base Layer: Caps Lock
  
  ## Nav layer Chords ##
    	Chord((KC.PGDN, KC.LEFT, KC.DOWN, KC.RGHT), KC.SPACE), 		# Nav layer
    	Chord((KC.UP, KC.RGHT),           KC.BSPC),            		# Nav Layer: Backspace
    	Chord((KC.LEFT, KC.UP),           KC.DEL),             		# Nav layer: Delete

    #### One-Shot Chords ####
    	Chord((LAYER_2_KEY, KC.R, KC.A, LAYER_1_KEY), 	OS_LSFT),	# OneShot left Shift
    	Chord((LAYER_1_KEY, LAYER_2_KEY),             	OS_LCTL),	# OneShot left Control
    	Chord((LAYER_1_KEY, KC.I),              	OS_LALT),	# OneShot left Alt
    	Chord((LAYER_1_KEY, KC.N),              	OS_LGUI),	# OneShot left GUI
	Chord((LAYER_1_KEY, LAYER_4_KEY),		OS_RALT),	# OneShot AltGr

    #### LAYER Trigger Chords ####
    Chord((KC.R, LAYER_2_KEY, KC.I),	DF_NAV),	# Change to Navigation Layer
    Chord((KC.UP, KC.LEFT, KC.RGHT),  	DF_BASE),	# Change back from Navigation Layer
]

if __name__ == '__main__':
    keyboard.go()

