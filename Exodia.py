import csv
import random
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

# CSVファイルの読み込み
with open("Exodia.csv", encoding = "utf-8-sig") as fp:
    deck = fp.read().splitlines()
deck = [int(i) for i in deck]

# 確率計算で使用するカウンターの宣言
hand_5 = 0
hand_4 = 0
hand_3 = 0
hand_2 = 0
hand_1 = 0
hand_0 = 0

# CUIで試行回数を入力させる
print("エクゾディアパーツを初手でそろえることはできるのか？\n確率を求めて見よう！")
print("========================================================")
num = int(input("ゲームを開始する回数（試行回数）を数字で入力してください．\n例：10000\n"))
print("========================================================")
print(str(num) + "回実行します．")

for i in range(num):
    hand = random.sample(deck, 5)
    if sum(hand) == 5:
        hand_5 += 1
    elif sum(hand) == 4:
        hand_4 += 1
    elif sum(hand) == 3:
        hand_3 += 1
    elif sum(hand) == 2:
        hand_2 += 1
    elif sum(hand) == 1:
        hand_1 += 1
    else :
        hand_0 += 1
    
    # 何回実行したかの確認
    if i % 10000 == 0 and num >= 10001:
        print('現在' + str(i) + '回目の計算まで完了') 

# 出現回数まとめ
hand_num = [hand_5, hand_4, hand_3, hand_2, hand_1, hand_0]

# エクゾディアの出現確率を求める．
prob_hand = [] # 確率を格納する配列
for i in range(len(hand_num)):
    prob = hand_num[i]/num * 100
    prob_hand.append(round(prob, 5))

print("すべての計算が完了しました．")

print("========================================================")


# GUIで結果のまとめを表示させる
GUI = tk.Tk()
GUI.geometry('800x500')
GUI.minsize(width=800, height=500)
GUI.maxsize(width=800, height=500)
GUI.title('エクゾディアが初手で揃う確率計算結果')
Title = tk.Label(text = "エクゾディアが初手で揃う確率の計算結果まとめ", font=("MSゴシック", "20", "bold"))
Title.pack(pady = 10)
PlayNum = tk.Label(text = "試行回数：" + str(num) + "回", font=("MSゴシック", "15", "bold"))
PlayNum.pack()
# "初手にエクゾディア5枚は" + str() + "回揃った．その確率は" + str() + "%だった．"
H_5 = tk.Label(text = "初手にエクゾディア5枚は" + str(hand_num[0]) + "回揃った．\n確率は" + str(prob_hand[0]) + "%だった．", font=("MSゴシック", "20", "bold"), foreground='red', background='black')
H_5.pack()
H_4 = tk.Label(text = "初手にエクゾディア4枚は" + str(hand_num[1]) + "回揃った．\n確率は" + str(prob_hand[1]) + "%だった．", font=("MSゴシック", "15", "bold"))
H_4.pack()
H_3 = tk.Label(text = "初手にエクゾディア3枚は" + str(hand_num[2]) + "回揃った．\n確率は" + str(prob_hand[2]) + "%だった．", font=("MSゴシック", "15", "bold"))
H_3.pack()
H_2 = tk.Label(text = "初手にエクゾディア2枚は" + str(hand_num[3]) + "回揃った．\n確率は" + str(prob_hand[3]) + "%だった．", font=("MSゴシック", "15", "bold"))
H_2.pack()
H_1 = tk.Label(text = "初手にエクゾディア1枚は" + str(hand_num[4]) + "回揃った．\n確率は" + str(prob_hand[4]) + "%だった．", font=("MSゴシック", "15", "bold"))
H_1.pack()
H_0 = tk.Label(text = "初手にエクゾディアは0枚も来なかった．その回数は" + str(hand_num[5]) + "回だった．\n確率は" + str(prob_hand[5]) + "%だった．", font=("MSゴシック", "15", "bold"))
H_0.pack()
if hand_5 >= 1:
    Clear = tk.Label(text = "エクゾディアがそろったぞ！", font=("MSゴシック", "20", "bold"))
    Clear.pack()
else :
    GameOver = tk.Label(text = 'エクゾディアはそろいませんでした……\n' + str(num) + "回程度で揃うことはないんだなあ……", font=("MSゴシック", "20", "bold"))
    GameOver.pack()
GUI.mainloop()
input("何かキーを押すと終了します．")