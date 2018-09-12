import dtree
import monkdata

t = dtree.buildTree(monkdata.monk1, monkdata.attributes)
print("Monk-1 Train Error: {}".format(dtree.check(t, monkdata.monk1)))
print("Monk-1 Test Error: {}".format(dtree.check(t, monkdata.monk1test)))

t = dtree.buildTree(monkdata.monk2, monkdata.attributes)
print("Monk-2 Train Error: {}".format(dtree.check(t, monkdata.monk2)))
print("Monk-2 Test Error: {}".format(dtree.check(t, monkdata.monk2test)))

t = dtree.buildTree(monkdata.monk3, monkdata.attributes)
print("Monk-3 Train Error: {}".format(dtree.check(t, monkdata.monk3)))
print("Monk-3 Test Error: {}".format(dtree.check(t, monkdata.monk3test)))