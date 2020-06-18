#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:00:00 2020

@author: lavend
"""


import random

f, t = map(int, input('請輸入範圍(以空格分開)：').split())
count = 1
keep = True
while keep:
    print(f'from: {f}, to: {t}')
    guess = random.randint(f, t)
    print(f'神機：{guess}')
    while True:
        ans = input('大請按「b」；小請按「s」；正確請按「y」；放棄請按「n」：')
        if ans == 'y':
            print(f'Ya~! 猜對了，共猜了{count}次')
            keep = False
            break
        elif ans == 'b':
            f = guess + 1
            break
        elif ans == 's':
            t = guess - 1
            break
        elif ans == 'n':
            print("你忙")
            keep = False
            break
        else:
            print('抱歉，沒聽清楚，請再說一次。')
    count += 1