import sys
import re
from datetime import datetime
import ctypes
import bs4
import quopri
import base64
import email
import poplib
poplib._MAXLINE = 20480
from pytz import timezone
from pprint import pprint


def getMailClient(id,pw,server:str ='pop.naver.com'):

    mailClient = poplib.POP3_SSL(server, port=995)
    mailClient.user(id)
    mailClient.pass_(pw)

    return mailClient


def getInfoFromMsg(msg):
    itemDict = {}
    for item in msg.items():
        if item[0].lower() not in ['subject','from','to','cc','date']:continue
        else:
            try:
                decodedResult = decodeAndMerge(item[1])
            except UnicodeDecodeError:
                decodedResult = mergeAndDecode(item[1])
            except:
                decodedResult = item[1]
            itemDict[item[0].lower()] = decodedResult
            print(str(itemDict))
    return itemDict


def getContentTextAndAttachmentFromMsg():...


# [문자 디코딩] ===============================================================================
def decodeBytes(bytesToDecode):
    bytesToDecode = bytesToDecode[2:-2]   # =?, ?= 제거
    temp = bytesToDecode.split('?')       # 인코딩목록과 내용 분리
    bytesToDecode = temp[-1]
    encodings = temp[:-1]

    for e in encodings[::-1]:   # 인코딩목록의 뒤에서부터 디코딩
        if e.lower() == 'b':
            bytesToDecode = base64.b64decode(bytesToDecode)
        elif e.lower()  == 'q':
            bytesToDecode = quopri.decodestring(bytesToDecode,header=True)
        else:
            bytesToDecode = bytesToDecode.decode(e)
    return bytesToDecode
# -------------------------------------------------------------------------------
def mergeAndDecode(oriBytesToDecode):
    bytesToDecode = ''.join(re.findall(r"=\?\S+\?\S\?(\S+)\?=",oriBytesToDecode))
    prefix = re.findall(r"(=\?\S+\?\S\?)",oriBytesToDecode)[0]
    bytesToDecode = prefix + bytesToDecode + "?="
    decodedResult = decodeBytes (bytesToDecode)
    return decodedResult

def decodeAndMerge(oriBytesToDecode):
    bytesToDecodeList = re.findall(r"(=\?\S+\?\S\?\S+\?=)",oriBytesToDecode)
    if bytesToDecodeList == []: raise
    decodedResult = ''
    for bytesToDecode in bytesToDecodeList:
        decodedResult += decodeBytes (bytesToDecode)
    return decodedResult


# ===========================================================================================
ID = 'id'
PW = 'pw'

if __name__ == '__main__':

    mailClient = getMailClient(ID, PW)    # 메일서버 연결하기
    latestMailNo = mailClient.stat()[0]  # 전체 메시지 수
    ... # latestMailTime = DB에 저장된 메일 중 최신메일의 시간

    for idx in range(latestMailNo,-1,-1): #마지막 메시지부터 역순으로 조회
        # 메시지 번호로 메시지 가져오기
        msg = email.message_from_bytes(b'\n'.join(mailClient.retr(idx)[1]))

        # 메일정보 읽기
        (subject,mailFrom,mailTo,mailCc,mailDate), timeObj = getInfoFromMsg(msg)
        
        # ... # mailDate를 latestMailTime과 비교해서 저장여부 확인

        # # 메일본문/첨부파일 읽기
        # (contentText, attachment) = getContentTextAndAttachmentFromMsg(msg)         
        
        ... # 읽은 정보를 DB에 저장하기