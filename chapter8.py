#%%
sampleSet = {1,2,3,4,5}
print(3 in sampleSet)
print(10 in sampleSet)
sampleSet2 = set(range(0, 10, 2))
print(sampleSet2)


# %%
# リストから重複を削除
listA = [1,1,2,2,3,3]
setA  = set(listA)
print(setA)
print(list(setA))#リストに戻す

setA.add(100)
print(setA)
setA.discard(3)
print(setA)
setA.pop()
print(setA)

#%%
setf = frozenset(range(0,2))
print(setf)
type(setf)#型


# %%
listB = [2,3,4]
setB = {num*2 for num in listB}
print(setB)


# %%
setC = set(['a','b','c','d'])
setD = set(['c','d','e','f'])
#和
print(setC | setD)
print(setC.union(setD))
#積
print(setC & setD)
print(setC.intersection(setD))
#差
print(setC - setD)
print(setC.difference(setD))
#対象差
print(setC ^ setD)
print(setC.symmetric_difference(setD))

setE = setD.copy()
print(setC == setD)
print(setD == setE)
print(setC != setD)
print(setC.isdisjoint(setD))#共通要素がないかどうか

# update
setC |= setD
print(setC)
print(setD.issubset(setC))#setD がsetCの一部かどうか
