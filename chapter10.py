#%%
def getTraiangleArea_m2 (base, height = 1) :
    area = base * height / 2.0
    print('base = ' + str(base))
    print('height = ' + str(height))
    return area

print(getTraiangleArea_m2(10, 5))
print(getTraiangleArea_m2(height = 10, base = 5))#キーワード指定
print(getTraiangleArea_m2(base = 5))#初期値指定利用

# %%
#何個でもタプルで受け取る
def getSumValue(*args) :
    sum = 0
    for num in args:
        sum += num
    return sum

print(getSumValue(1,2,3,4,5))
print(getSumValue(1,2,3,4,5,6,7,8,9))

# %%
#何個でも辞書で受け取る
def echoAsDict(**kwargs) :
    print(kwargs)

echoAsDict(apple = 10, banana = 20)
echoAsDict(apple = 10, banana = 20, orange = 30)
