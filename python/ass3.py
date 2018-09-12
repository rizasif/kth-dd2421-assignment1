import monkdata
import dtree

m1av1 = round(dtree.averageGain(monkdata.monk1, monkdata.attributes[0]),8)
m1av2 = round(dtree.averageGain(monkdata.monk1, monkdata.attributes[1]),8)
m1av3 = round(dtree.averageGain(monkdata.monk1, monkdata.attributes[2]),8)
m1av4 = round(dtree.averageGain(monkdata.monk1, monkdata.attributes[3]),8)
m1av5 = round(dtree.averageGain(monkdata.monk1, monkdata.attributes[4]),8)
m1av6 = round(dtree.averageGain(monkdata.monk1, monkdata.attributes[5]),8)

m1AttrList = [m1av1, m1av2, m1av3, m1av4, m1av5, m1av6]
print("Monk-1 Avrage Gain: {}".format(m1AttrList))

m2av1 = round(dtree.averageGain(monkdata.monk2, monkdata.attributes[0]),8)
m2av2 = round(dtree.averageGain(monkdata.monk2, monkdata.attributes[1]),8)
m2av3 = round(dtree.averageGain(monkdata.monk2, monkdata.attributes[2]),8)
m2av4 = round(dtree.averageGain(monkdata.monk2, monkdata.attributes[3]),8)
m2av5 = round(dtree.averageGain(monkdata.monk2, monkdata.attributes[4]),8)
m2av6 = round(dtree.averageGain(monkdata.monk2, monkdata.attributes[5]),8)

m2AttrList = [m2av1, m2av2, m2av3, m2av4, m2av5, m2av6]
print("Monk-2 Avrage Gain: {}".format(m2AttrList))

m3av1 = round(dtree.averageGain(monkdata.monk3, monkdata.attributes[0]),8)
m3av2 = round(dtree.averageGain(monkdata.monk3, monkdata.attributes[1]),8)
m3av3 = round(dtree.averageGain(monkdata.monk3, monkdata.attributes[2]),8)
m3av4 = round(dtree.averageGain(monkdata.monk3, monkdata.attributes[3]),8)
m3av5 = round(dtree.averageGain(monkdata.monk3, monkdata.attributes[4]),8)
m3av6 = round(dtree.averageGain(monkdata.monk3, monkdata.attributes[5]),8)

m3AttrList = [m3av1, m3av2, m3av3, m3av4, m3av5, m3av6]
print("Monk-3 Avrage Gain: {}".format(m3AttrList))

print("Recommended Attribute Monk-1: {}".format(m1AttrList.index(max(m1AttrList))+1))
print("Recommended Attribute Monk-2: {}".format(m2AttrList.index(max(m2AttrList))+1))
print("Recommended Attribute Monk-3: {}".format(m3AttrList.index(max(m3AttrList))+1))