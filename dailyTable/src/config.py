
class Constants:
    
    DATE_INPUTS = ["date"]
    MORNING_INPUTS = ["morning"]
    WORK_INPUTS = ["work1","work2","work3"]
    ROUNTINE_INPUTS = ["routine1","routine2","routine3","routine4"]
    MAINTEXT_INPUTS = ["memo",'title'] + WORK_INPUTS + ROUNTINE_INPUTS
    CHECK_INPUTS =  ["checkRoutine", "checkWork", "checkHobby"]
    HAPPY_INPUTS = ["happy"]
    # --------------------------
    INPUT_LIST = DATE_INPUTS + MORNING_INPUTS + MAINTEXT_INPUTS +CHECK_INPUTS + HAPPY_INPUTS
    # -------------------------------------------------------------------------------------------
    INPUT_PATH = './input.txt'
    TICKET_PATH = "./temp.png"
    BGIMG_PATH = "./bgimg"
    ICON_PATH = "./icon"
    RESULT_PATH = "./result/{}.png"
    CHECK_PATH = "./check/check.png"
    STAR_PATH = "./check/star{}.png"
    # --------------------------
    DEFAULT_BLANK = ""
    # --------------------------
    ICON_SIZE = 170
    CHECK_SIZE = 35
    STAR_SIZE = 30
# ===========================================================================================
    
class Styles:

    from PIL import ImageFont
    # --------------------------
    FONT_DATE_PATH = "./font/consola.ttf"
    FONT_MORNING_PATH = "./font/Seven Segment.ttf"
    FONT_MAINTEXT_PATH = "./font/SuseongDotum.ttf"
    FONT_MEMO_PATH = "./font/나눔손글씨 옥비체.ttf"
    FONT_CHECK_PATH = "./font/HYQingZhouXingW-2.ttf"
    # --------------------------
    GRAY = (78, 77, 72)
    BROWN = (124, 94, 70)
    GREEN = (112,178,164)
    LIGHTGRAY = (186,178,167)
    PURPLE = (192,161,255)
    # -------------------------------------------------------------------------------------------
    FONT_DICT = {"date":[ImageFont.truetype(FONT_DATE_PATH, 22), BROWN, "center"],
                 "morning":[ImageFont.truetype(FONT_MORNING_PATH, 60), BROWN, "center"],
                 "work":[ImageFont.truetype(FONT_MAINTEXT_PATH, 25), GRAY, "start"],
                 "routine":[ImageFont.truetype(FONT_MAINTEXT_PATH, 25), GRAY, "center"],
                 "title":[ImageFont.truetype(FONT_MAINTEXT_PATH, 25), BROWN, "start"],
                 "memo":[ImageFont.truetype(FONT_MEMO_PATH, 40), GRAY, "start"],
                 "checkO":[ImageFont.truetype(FONT_CHECK_PATH, 70), GREEN, "center"],
                 "checkX":[ImageFont.truetype(FONT_MAINTEXT_PATH,60), LIGHTGRAY, "center"]}
    # -------------------------------------------------------------------------------------------
    POS_DICT = {"date": (730,575),
                "morning": (730,603),
                "title":(255,306),
                "work1":(293,356), "work2":(293,417), "work3":(293,478),
                "work1check":(280,360), "work2check":(280,422), "work3check":(280,483),
                "hobby1check":(198,580),"hobby2check":(285,580),"hobby3check":(370,580),
                "hobby4check":(457,580),"hobby5check":(537,580),"hobby6check":(609,580),
                "routine1":(220,233), "routine2":(365,233), "routine3":(505,233), "routine4":(650,233),
                "routine1check":(220,222), "routine2check":(365,222), "routine3check":(505,222), "routine4check":(650,222),
                "memo":(900,180)}
# ===========================================================================================