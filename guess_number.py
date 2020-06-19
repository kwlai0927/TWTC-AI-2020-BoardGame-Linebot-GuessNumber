#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:00:00 2020

@author: lavend
"""

import random
import math

class Guesser:

    ## --- 文句 ----

    sentence_guess = [
        "阿，我知道了，__guess__",
        "不會是__guess__吧",
        "隨便啦～就__guess__",
        "__guess__",
        "應該是__guess__吧 哈哈",
        "好吧! 那就__guess__囉....",
        "不然就來個__guess__囉....",
        "擲杯問問，__guess__應該是個大吉吧！",
        "就來個幸運數字__guess__囉..",
        "決定就是你了！去吧~__guess__",
        "我阿公剛剛托夢說是__guess__",
        "媽祖叫我選__guess__"
    ]

    sentence_guick_correct = [
        "顆顆顆~ 小菜一疊！∠( ᐛ 」∠)＿",
        "再來十題，也是咻咻咻",
        "我就説我有讀心術，現在相信了吧！",
        "今天的我，沒有極限！",
        "哈哈哈~  ㄟ 拜託~我誰！(傲嬌口氣)",
        "什麼鬼ㄚ...太沒挑戰性了啦……（欠扁）",
        "就說吧~",
        "eazy~",
        "Seeeeeeee", 
        "Skr",
        "666666666"
    ]

    sentence_correct = [
        "好，就醬，掰",
        "那走了，掰",
        "唉~ 還有進步空間..",
        "好棒～拍手！！！",
        "不要這麼專業～",
        "賽啦～",
        "出運了！",
        "哦……結束咯？",
        "靠! 差一點....",
        "不行，再來一次！"
        "終於"
    ]

    sentence_wrong = [
        "阿，會不會是...不行，講太多了",
        "emm……",
        "水逆日！(╯°□°）╯︵ ┻━┻", 
        "保持微笑",
        "......",
        "...",
        "尬電"
    ]

    sentence_wrong_exceed_exp = [
        "這也太難了吧~_(:з」∠)_",
        "寶寶心理苦但寶寶不說...(´ཀ`」 ∠)",
        "水逆日！(╯°□°）╯︵ ┻━┻", 
        "保持微笑",
        "我就爛！",
        "生無可戀...",
        "繼續旋轉我沒關係",
        "媽的了....&%**&￥#@*#&（消音）到底是多少啦！（抓頭）",
        "用盡大半青春和你對猜，我得到了什麼啊！！"
    ]

    sentence_exit = [
        "不玩我走了",
        "我要去尿尿了"
        "吃飯皇帝大"
        "算了~ 吃飯去.."
        "有事嗎?"
        "哩喜來亂欸逆！"
        "洗滴攻山小"
        "史密斯"
        "到底想怎樣？"
        "……我去喂貓了，拜~"
        "你是不是發錯人了？"
        "認真一點好不好？"
        "當我塑膠做的？"
        "用盡大半青春和你對猜，我得到了什麼啊！！"
        "過完年再跟你算帳"
        "是在哈囉？"
    ]

    ## ------


    all_guessers = {}


    def __init__(self):
        self.state = "init"
        self._from = None
        self._to = None
        self._exp = None
        self._quick = 3
        self._count = 0

    def setRange(self, f = None, t = None):
        if int(f):
            self._from = f
            self._f = f
            self.state = "from"
            
        if int(t):
            self._to = t
            self._t = t
            self.state = "to"
            
        if self._f and self._t and self._t >= self._f:
            interval = self._t - self._f
            self._exp = int(math.log2(interval))
            # 區間太小 沒有快速
            if self._quick >= self._exp:
                self._quick = 0 
                

    # random

    def randint(self, f, t):
        return random.randint(f, t)

    def _get_sentence_guess(self, guess):
        return self._get_sentence(self.__class__.sentence_guess).replace('__guess__', str(guess))

    def _get_sentence(self, ary):
        idx = random.randint(0, len(ary) - 1)
        a = ary[idx]
        return a

    def _get_correct_sentence(self):
        if self._count <= self._quick:
            return self._get_sentence(self.__class__.sentence_guick_correct)
        else:
            return self._get_sentence(self.__class__.sentence_correct)
    
    def _get_wrong_sentence(self):
        if self._count <= self._exp:
            return self._get_sentence(self.__class__.sentence_wrong)
        else:
            return self._get_sentence(self.__class__.sentence_wrong_exceed_exp)


    # guess

    def guess(self):
        self._guess = self.randint(self._f, self._t)
        self._count += 1
        return self._get_sentence_guess(self._guess)

    def feedback(self, result):
        if result == 'b':
            self._f = self._guess + 1
            return self._get_wrong_sentence()
        elif result == 's':
            self._t = self._guess - 1
            return self._get_wrong_sentence()
        elif result == 'y':
            return  self._get_correct_sentence()
        else:
            self.state = 'end'
            return self._get_sentence(self.__class__.sentence_exit)
    



def main():
    f, t = map(int, input('請輸入範圍(以空格分開)：').split())
    
    _guesser = Guesser()
    _guesser.setRange(f, t)
    while True:
        
        print(_guesser.guess())
        
        ans = input('大請按「b」；小請按「s」；正確請按「y」；放棄請按其他鍵：')
        a = _guesser.feedback(ans)
        print(a)
        if ans not in ['b', 's']:
            break

if __name__ == "__main__":
    main()
