import math

def entropy(dataset):
    "Calculate the entropy of a dataset"
    "Assuming the values are 0-4"
    n = len(dataset)
    s0 = dataset.count(0)
    s1 = dataset.count(1)
    s2 = dataset.count(2)
    s3 = dataset.count(3)
    s4 = dataset.count(4)

    p0 = float(s0)/float(n)
    p1 = float(s1)/float(n)
    p2 = float(s2)/float(n)
    p3 = float(s3)/float(n)
    p4 = float(s4)/float(n)

    return (-p0*math.log(p0,2)) + (-p1*math.log(p1,2)) + (-p2*math.log(p2,2)) + \
        (-p3*math.log(p3,2)) + (-p4*math.log(p4,2))

uniform_dist = [i for i in range(5)]
non_uniform_dist = [1,1,2,2,2,3,3,4,4,4,2,2,2,0]

un_e = entropy(uniform_dist)
nun_e = entropy(non_uniform_dist)

print("Entropy Uniform Distribution: {}".format(un_e))
print("Entropy Non-Uniform Distribution: {}".format(nun_e))