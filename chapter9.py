#%%
jisho = {"some": "thing", "key": "value"}
print(jisho)
print(len(jisho))

jisho2 = dict([("a", 1), ("b", 2), ("c",  3)])
print(jisho2)


# %%
jisho3 = dict.fromkeys(["e", "f", "g"], 1)
jisho4 = dict.fromkeys("hijk")
print(jisho3)
print(jisho4)

jisho3["f"] = 2
print(jisho3)
jisho3["l"] = 3
print(jisho3)
jisho3.update(jisho4)#追加
print(jisho3)

del jisho3["f"]
print(jisho3)
jisho3.clear()
print(jisho3)


# %%
jisho5 = dict.fromkeys(["e", "f", "g"], 1)
jisho6 = { key: 10 for key in jisho5 }
print(jisho6)

print(jisho5["e"]) #値を取り出す
print(jisho5.get("e")) #値を取り出す.こちらが良い
print("f" in jisho5) #keyがあるか？

for key in jisho5:
    print(key + ': ' + str(jisho5[key]))

print(jisho5.keys())
keyList = list(jisho5.keys())
print(keyList)
valList = list(jisho5.values())
print(valList)
itemList = list(jisho5.items())# item = (key, val)
print(itemList)

#削除
print(jisho5)
jisho5.pop("e")
print(jisho5)
jisho5.popitem()
print(jisho5)

# %%
