#%%
#module を利用する
# math
import math
val = 0.5
print(math.ceil(val))#切り上げ
print(math.floor(val))#切り捨て
print(math.pi)#切り捨て

# %%
# 距離20m 先にある、角度32度でみえる木の高さを求める
dist = 20
degree = 32
rad = math.radians(degree)
height = dist * math.tan(rad)
print('木の高さは' + str(height) + 'm です。')

# 小数点第１位で切り捨てる
heightFloor = math.floor(height * 10) / 10
print('木の高さは' + str(heightFloor) + 'm です。')

# %%
# random
import random
# (x, y)間の整数乱数
print(random.randint(0, 9))

# (0.0, 1.0)間の浮動少数乱数
print(random.random())

# %%
#文字列のメソッドで遊んでみる
sampleStr = 'korehaTESUTOdayo'
print(sampleStr.upper())
print(sampleStr.lower())
print(sampleStr.swapcase())#逆転

sampleStr2 = '  ,.this is a pen...  '
print(sampleStr2.title())#単語の先頭文字だけ大文字にする
print(sampleStr2.capitalize())#先頭だけ大文字にする

print(sampleStr.count('o'))#o の数を数える
print(sampleStr.count('o', 0, 5))#o の数を数える(範囲指定)
print(sampleStr.find('o', 0, 5))#o の位置を探す(範囲指定). 結果はインデックス
print(sampleStr.find('z'))#見つからない場合は-1
print(sampleStr.rfind('o'))#o の位置を後ろから探す

stripedSample = sampleStr2.strip()
print(stripedSample)#前後の空白、改行コードを削除する
print(stripedSample.strip('.,\n'))#前後の指定した文字を削除
print(stripedSample.rstrip('.,\n'))#後の指定した文字を削除

#文字列に値を埋め込むやつ
acsidentNum = 10
settingStr = '{}の交通事故は{}件, 死傷者は{}人でした。'
settingStr.format('今日', acsidentNum, 5)

# ' ではなく " を使わないとエラー
directFormatStr = f"{'今日'}の交通事故は{acsidentNum}件, 死傷者は{5}人でした。"
print(directFormatStr)

acsidentNum = 100000
directFormatStr2 = f"{'今日'}の交通事故は{acsidentNum:,}件, 死傷者は{5}人でした。"
print(directFormatStr2)#3桁で,区切りして出力

pi = math.pi
directFormatStr3 = f"円周率は{pi:.5f}...です。"
print(directFormatStr3)#小数点以下五位まで出力
