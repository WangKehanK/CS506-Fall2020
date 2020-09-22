import math

def euclidean_dist(x, y):
    # base case
    if (len(x) != len(y)):
        return "There is an error in input."
    result = 0
    for i in range(len(x)):
        result += (x[i]-y[i])**2
    result = math.sqrt(result)
    return result

def manhattan_dist(x, y):
    if (len(x) != len(y)):
        return "There is an error in input."
    result = 0
    for i in range(len(x)):
        result += abs(x[i]-y[i])
    return result

def jaccard_dist(x, y):
    if (len(x) != len(y)):
        return "There is an error in input."
    x1 = set(x)
    x2 = set(y)
    result = 1 - len(x1.intersection(x2)) / len(x1.union(x2))
    return result

def cosine_sim(x, y):
    if (len(x) != len(y)):
        return "There is an error in input."
    r = 0
    m1 = 0
    m2 = 0
    result = 0
    for i in range(len(x)):
        r += x[i]*y[i]
        m1 += x[i]**2
        m2 += y[i]**2
    m1 = m1**(1/2)
    m2 = m2**(1/2)
    result = r / (m1*m2)
    return result