#normal distribution(정규분포) library
import math
from functools import reduce

def average(scores):
    return reduce(
        lambda a, b:
        a + b,
        scores)/len(scores)

def variance(scores, avrg):
    return round(
        reduce(
        lambda a, b:
        a + b,
        map(
            lambda s:
            (s-avrg)**2,
            scores))/len(scores),
                 1)

def std_dev(variance):
    return round(
        math.sqrt(variance),
        1)
