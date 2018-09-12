import monkdata
import dtree

e1 = dtree.entropy(monkdata.monk1)
e2 = dtree.entropy(monkdata.monk2)
e3 = dtree.entropy(monkdata.monk3)

print("Entropy Monk-1: {}".format(e1))
print("Entropy Monk-2: {}".format(e2))
print("Entropy Monk-3: {}".format(e3))