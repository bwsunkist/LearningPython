#%%
nums = [1,2,3]
print(nums)
print(nums * 3)
print(len(nums))

rangeList = list(range(0,10,2))
print(rangeList)

listFromStr = list("Hello World")
print(listFromStr)


# %%
listFromStr.append(10)
listFromStr.insert(11, '!')
print(listFromStr)

listFromStr.pop()
listFromStr.pop(0)
print(listFromStr)

listFromStr.remove('W')#最初に見つけたWを削除
print(listFromStr)


# %%
listFromStr2 = "Hello World"
print(listFromStr2)
print(listFromStr2.split('o'))
print(listFromStr2.split('l', 2))#２回分割

# %%
listFromStr3 = listFromStr.copy()
print(listFromStr is listFromStr3)
numbers = [5,2,6,9,3]
numbers.sort()
print(numbers)
numbers.sort(reverse = True)
print(numbers)
print(sorted(numbers))

import random
random.shuffle(numbers)
print(numbers)

numbers_db = [num * 2 for num in numbers]
print(numbers_db)
print([num for num in numbers_db if num >= 10])

print(10 in numbers_db)
print(numbers_db.index(10))

print(sum(numbers_db))
print(max(numbers_db))
print(min(numbers_db))

# %%
# Chapter7
# Tuple はListとだいたい同じ操作？
# ただし中身を変更できないconstぽい感じ？
nums = (5,6,7)
print(nums)
(a,b,c) = tuple(range(2, 5))#変数に格納
print(a, b, c)

x = [ 1, 2 ]
y = [ 7, 8 ]
xy = zip(x, y)
print(list(xy))#[(1, 7), (2, 8)]
