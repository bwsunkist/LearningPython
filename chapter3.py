#%%
a = 10
b = 5
print(a + b)

# %%
# 区切り文字の変更と, 末尾文字列の追加
print(a, b, 100, sep="、", end=" 以上")

# %%
# round は四捨五入と異なるので注意
# 1.5 では 偶数の２に丸める
# 2.5 では 偶数の２に丸める
# 3.5 では 偶数の４に丸める
print(round(1.4))
print(round(1.5))
print(round(1.6))
print(round(2.4))
print(round(2.5))
print(round(2.6))
print(round(3.4))
print(round(3.5))
print(round(3.6))
# %%
# 複素数を扱う
n = 1j * 1j
print(n) # -1
print(n.real)
print(n.imag)


# %%
# 商を小数点切り捨てで求める
print(5/2)# 通常の商
print(5//2)#切り捨て
# ** でべき乗できる
print(2 ** 3)

# %%
print("aaa")
print("""
      a
      a
      a
      """)
#文字列の掛け算が可能
print("abc"*3)
#数字の文字列変換
print(str(3000) + "円!")


# %%
h = ["a", "b", "c", "d"]
print(h[2])
#後ろから数えての指定が可能。
print(h[-2])


# %%
g = "abcdefgh"
print(g[0])
print(g[:])#全部
print(g[2:])#3文字目以降
print(g[2:2+4])#3文字目から4文字

#ステップ数を指定可能
print(g[0:9:2])#ステップ2なので 1, 3, 5文字目が表示
print(g[::-2])#後ろからステップ2


# %%
# and or の指定が楽
print(True and True)
print(True and False)
print(False or True)

