#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 17:50:20 2018

@author: itoumichihiro
"""
list = [1,2,3,4,5,6]

total = 0
for i in list:             # listの値をそれぞれ一つずつ取り出して変数iに代入していく
    total = total + i
print("合計"+str(total))   
ave = total / len(list)
print("平均"+str(ave))
    


a = [11,22,33,44,55]
del(a[3])         #指定した配列番号の値を削除
b = [44]
a = a + b
print(str(a))



points = []   #空の配列を用意しておく
while True:
    s = input("体重は")    #input("")は文字を入力するものであるから数字を入れても文字として判断される
    if (s == "") or (s == "q"):break
    v = int(s)       #文字から数字に変換
    
    points.append(v)  #変数vを空の配列pointsに代入していく
    
print(str(points))
    
        
    