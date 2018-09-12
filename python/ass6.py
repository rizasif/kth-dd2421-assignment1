import dtree
import monkdata

t1 = dtree.buildTree(monkdata.monk1,monkdata.attributes)
pt1 = dtree.allPruned(t1)

pt1_checks = []
for i in range(len(pt1)):
    pt1_checks.append(round(dtree.check(pt1[i],monkdata.monk1test), 8))

print("Best tree is: {}".format( pt1_checks.index(max(pt1_checks)) ) )