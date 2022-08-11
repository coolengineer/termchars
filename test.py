
import __init__ as termchars

import random

s = "[고지] 하나멤버스 광고성 정보 수신동의 내역 안내"
s = "[그렙] 프로그래머스 기업 이용약관 개정 공지"

beg = 0
for size in range(0, 50):
    print(beg, size, termchars.substr(s, beg, size, True) + "####")
