from igzg.utils import getConfig, getNowStr
from PIL import Image, ImageDraw
from os import listdir, path
from random import choice
from config import Constants as C, Styles as S

class ImageEditor:
    def __init__(self):
        self.ticketimg = Image.open(C.TICKET_PATH)
        self.get_random_bgimg()
        self.get_random_icon()
        self.get_check_icon()
        self.draw = ImageDraw.Draw(self.image)

        self.image.paste(self.ticketimg, (0,0), self.ticketimg.split()[-1])
        self.image.paste(self.icon, self.get_start_pos(self.icon.getbbox(),*(155,410)), self.icon.split()[-1])
    # -------------------------------------------------------------------------------------------

    def write_text(self, text, text_type):
        pos = S.POS_DICT[text_type]
        text_type = "routine" if "routine" in text_type else "work" if "work" in text_type else text_type
        font, color, anchor = S.FONT_DICT[text_type]
        pos = self.get_start_pos(font.getbbox(text),*pos) if "center" in anchor else pos
        self.draw.text(pos, text, color, font)

    # -------------------------------------------------------------------------------------------

    def put_stars(self,count):
        temp = Image.open(C.STAR_PATH.format(count))
        self.star = temp.resize(self.get_resize_size(temp,C.STAR_SIZE))
        self.image.paste(temp, self.get_start_pos(self.star.getbbox(),*(150,520)), temp.split()[-1])
    
    def do_check(self,checks,poss,text_type=None):
        for idx, p in enumerate(poss):
            if checks[idx]:
                if text_type:
                    text = text_type[-1]
                    font, color, anchor = S.FONT_DICT[text_type]
                    self.draw.text(self.get_start_pos(font.getbbox(text),*p), text, color, font)
                else:
                    self.image.paste(self.check, self.get_start_pos(self.check.getbbox(),*p), self.check.split()[-1])

    def call_check(self,checks):
        if len(checks) == 4:
            poss = [S.POS_DICT[x+'check'] for x in C.ROUNTINE_INPUTS]
            self.do_check(checks,poss,text_type="checkX")
            if checks.count(True) == 4:
                self.image.paste(self.check, self.get_start_pos(self.check.getbbox(),*(767,235)), self.check.split()[-1])

        elif len(checks) == 3:
            poss = [S.POS_DICT[x+'check'] for x in C.WORK_INPUTS]
            self.do_check(checks,poss)
            self.put_stars(checks.count(True))

        elif len(checks) == 6:
            poss = [S.POS_DICT["hobby{}check".format(str(x+1))] for x in range(6)]
            self.do_check(checks,poss,text_type="checkO")            
        else:print("check err")

    # -------------------------------------------------------------------------------------------

    def draw_happy(self,happy):
        happy_bar = Image.new("RGB", (int(happy/100*550), 12), color=S.PURPLE)
        self.image.paste(happy_bar,(250,535))

    # -------------------------------------------------------------------------------------------
    def get_random_bgimg(self):
        bgimg_paths = self.get_filepaths(C.BGIMG_PATH)
        temp = Image.open(choice(bgimg_paths)).convert('RGB')
        self.image = temp.resize(self.get_resize_size(temp,self.ticketimg.height)).crop(self.ticketimg.getbbox())

    def get_random_icon(self):
        icon_paths = self.get_filepaths(C.ICON_PATH)
        temp = Image.open(choice(icon_paths))
        self.icon = temp.resize(self.get_resize_size(temp,C.ICON_SIZE))

    def get_check_icon(self):
        temp = Image.open(C.CHECK_PATH)
        self.check = temp.resize(self.get_resize_size(temp,C.CHECK_SIZE))        

    # -------------------------------------------------------------------------------------------

    def get_filepaths(self,dir,end=".png"):
        return [path.join(dir, x) for x in listdir(dir) if x.endswith(end)]

    def get_resize_size(self,img,resizeH):
        return (img.width * resizeH // img.height, resizeH)

    def get_start_pos(self, bbox, centerX, centerY):
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        return (centerX - w // 2, centerY - h //2)
    
    def show(self): self.image.show()
    def save(self): self.image.save(C.RESULT_PATH.format(getNowStr("%y%m%d")))
# ===========================================================================================


class ImageMaker(ImageEditor):
    def __init__(self):
        ImageEditor.__init__(self)
        self.input = getConfig(C.INPUT_LIST,configFilePath=C.INPUT_PATH)
        self.write_date()
        self.write_morning()
        self.write_maintext()
        self.mark_check()
        self.mark_happy()

    def write_date(self):
        for d in C.DATE_INPUTS:
            idx = C.INPUT_LIST.index(d)
            dateText = self.input[idx].strip() \
                        if self.input[idx] != '' else getNowStr("%Y.%m.%d")
            self.write_text(dateText,d)

    def write_morning(self):
        for m in C.MORNING_INPUTS:
            idx = C.INPUT_LIST.index(m)
            morningText = self.input[idx].replace('1',' 1').replace(':','').strip() \
                            if self.input[idx] else C.DEFAULT_BLANK
            self.write_text(morningText,m)

    def write_maintext(self):
        for w in C.MAINTEXT_INPUTS:
            idx = C.INPUT_LIST.index(w)
            wText = '\n'.join([x.strip() for x in self.input[idx].split('\\')]) \
                            if self.input[idx] else C.DEFAULT_BLANK
            self.write_text(wText,w)

    def mark_check(self):
        for c in C.CHECK_INPUTS:
            idx = C.INPUT_LIST.index(c)
            checks = [True if x=='o'else False for x in self.input[idx].strip()]
            self.call_check(checks)

    def mark_happy(self):
        for h in C.HAPPY_INPUTS:
            idx = C.INPUT_LIST.index(h)
            self.draw_happy(int(self.input[idx]))


if __name__ == "__main__":
    tm = ImageMaker()
    tm.save()
