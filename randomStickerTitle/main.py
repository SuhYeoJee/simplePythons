import os
import random
from PIL import Image

class TitleMaker:
    def __init__(self):
        self.width, self.height, self.resizeH = 966, 200, 80
        self.image = Image.new("RGB", (self.width, self.height), "#232226")

        self.posXs = [x for x in range(0,self.width,self.resizeH >> 1)][1:-2]
        self.posYs = [x for x in range(0,self.height,self.resizeH >> 1)][1:-1]
        self.posHistory = [(0,0)]

    def getSticker(self,filename):
        h = self.resizeH + random.choice([-20,0,0,0,20])
        sticker = Image.open(filename)
        sticker.thumbnail((sticker.width * h // sticker.height, h))
        return sticker

    def getRandPos(self):
        x,y = 0,0
        while (x,y) in self.posHistory:
            x = random.choice(self.posXs)
            y = random.choice(self.posYs)
        else:
            self.posHistory.append((x,y))

        x += random.randint(0,10)
        y += random.randint(0,10)
        return (x,y)

    def putSticker(self, filename):
        sticker = self.getSticker(filename)
        r, g, b, a = sticker.split()
        self.image.paste(sticker, self.getRandPos(), mask=a)
    
    def save(self):
        self.image.save('res.png')

if __name__ == "__main__":
    stickerPath = "sticker"

    tm = TitleMaker()
    [tm.putSticker(y) for y in [os.path.join(stickerPath, x) for x in os.listdir(stickerPath) if x.endswith(".png")]]
    tm.save()