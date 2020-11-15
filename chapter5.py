#%%
import random
# 条件分岐
val1 = random.random() * 20
print(f"start with val1 = {val1: .1f}")
if val1 > 10:
    print('OK')
elif val1 <= 10:
    print('OK2')    
else:
    print('NG')

print('end')

if not val1 > 10:
    print('OK ?')#not で反転

if val1 > 10 <= 15:
    print('15 >= val1 > 10 ')#省略して条件式を書く

print(val1 if val1 <= 15 else -1)# 三項演算子ぽい書き方

#%%
# while
idx = 0
while idx < 3:
    print(idx)
    idx+= 1
else: 
    # break 以外で抜けるときに通る
    print('else')

print('while end.')
print(idx)


#%%
# for
for i in range(3):
    print(f"loop {i}th")#0-2
for i in range(3, 5):
    print(f"loop {i}th")#3-4
for i in range(5, 10, 2):
    print(f"loop {i}th")#5,7,9
else: 
    # break 以外で抜けるときに通る
    print('else')


#%%
# try
try:
    pass
except ValueError :
    pass
else:
    pass
finally:
    pass
# except は複数記載してエラー種類によって処理を変更可能
# else は例外が発生しなかった場合に実行
