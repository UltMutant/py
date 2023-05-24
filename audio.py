from pyo import *
s = Server().boot()
osc = Sine(freq=440, mul=0.5)
env = Adsr(attack=0.1, decay=0.1, sustain=0.5, release=0.1, dur=1.0)
osc = osc * env
env.play()
s.start()
s.gui(locals())
s.stop()