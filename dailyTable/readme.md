매일 일기를 쓸 때 사용할 일간기록표 이미지를 자동 생성하는 프로그램.   
input.txt의 내용을 읽어 텍스트를 작성하고 진행도를 체크.  

### 목표 이미지
![일간기록표](./result/240328.png)

### 사용 방법

1. 리소스 폴더의 리소스 확인 (`bgimg`, `check`, `font`, `icon`, `temp.png`)
2. input.txt에 내용 입력
3. `run.bat`(혹은 `main.py`)를 실행
4. `./result/[날짜].png` 확인

### 프로그램 구조

`ImageEditor`를 상속받는 `ImageMaker` 클래스는 생성자에서 모든 동작을 완료한다.  

``` python
class ImageMaker(ImageEditor):
    def __init__(self):
        ImageEditor.__init__(self)
        self.input = getConfig(C.INPUT_LIST,configFilePath=C.INPUT_PATH)

        self.write_date()
        self.write_morning()
        self.write_maintext()
        self.mark_check()
        self.mark_happy()
```

`ImageMaker`의 각 함수는 input.txt의 값을 처리해서 `ImageEditor`의 함수를 호출한다.  

예시) `write_date` 함수  
``` python
    def write_date(self):
        for d in C.DATE_INPUTS:
            idx = C.INPUT_LIST.index(d)
            dateText = self.input[idx].strip() \
                        if self.input[idx] != '' else getNowStr("%Y.%m.%d")
            self.write_text(dateText,d)
```

`ImageEditor` 클래스는 생성시에 이미지 리소스를 가져오고, 배경과 아이콘을 붙여 베이스 이미지를 생성한다. 

``` python
class ImageEditor:

    def __init__(self):
        self.ticketimg = Image.open(C.TICKET_PATH)
        self.get_random_bgimg()
        self.get_random_icon()
        self.get_check_icon()
        self.draw = ImageDraw.Draw(self.image)

        self.image.paste(self.ticketimg, (0,0), self.ticketimg.split()[-1])
        self.image.paste(self.icon, \ 
	        self.get_start_pos(self.icon.getbbox(),*(155,410)), self.icon.split()[-1])
```

이후 `ImageMaker`클래스의 메소드에서 `ImageEditor`클래스의 `write_text`, `put_stars`, `do_check`, `draw_happy` 등의 함수를 호출하여 베이스 이미지를 가공한다. 

### 추가 기능 

- 이모티콘 그룹화 + 달성 일정 수에 따라 이모티콘 그룹 선택하기