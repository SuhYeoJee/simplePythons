import os
import random
from PIL import Image

class TitleMaker:
    def __init__(self):
        self.width, self.height = 966, 200
        self.image = Image.new("RGBA", (self.width, self.height), "#232226")

    def putSticker(self, filename):
        resizeH=80

        sticker = Image.open(filename)
        sticker.thumbnail((sticker.width * resizeH // sticker.height, resizeH))
        
        x = random.randint(0, self.width  - sticker.width)
        y = random.randint(0, self.height - sticker.height)
        
        r, g, b, a = sticker.split()
        self.image.paste(sticker, (x, y), mask=a)
    
    def save(self):
        self.image.save('res.png')

if __name__ == "__main__":
    stickerPath = "sticker"
    stickers = [os.path.join(stickerPath, x) for x in os.listdir(stickerPath) if x.endswith(".png")]

    tm = TitleMaker()
    [tm.putSticker(y) for y in [os.path.join(stickerPath, x) for x in os.listdir(stickerPath) if x.endswith(".png")]]
    tm.save()