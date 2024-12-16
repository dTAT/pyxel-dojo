import pyxel
import json

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Hello Pyxel")
        pyxel.images[0].load(0, 0, "assets/img_sumika.png")
        with open(f"assets/hatsu.json", "rt") as fin:
            self.music = json.loads(fin.read())
        for ch, sound in enumerate(self.music):
            pyxel.sound(ch).set(*sound)
            pyxel.play(ch, ch, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(20, 1, "Tame-Line One Step!!", pyxel.frame_count % 16)
        pyxel.blt(20, 8, 0, 8, 8, 120, 112)



App()
