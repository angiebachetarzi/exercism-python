def equilateral(sides):
    occurences = occurences_array(sides)
    return is_valid_triangle(sides) and 3 in occurences


def isosceles(sides):
    occurences = occurences_array(sides) 
    return is_valid_triangle(sides) and 2 in occurences or 3 in occurences


def scalene(sides):
    occurences = occurences_array(sides) 
    return is_valid_triangle(sides) and not 2 in occurences and not 3 in occurences


def occurences_array(sides):
    occurences = [0] * len(sides)
    for i in range(len(sides)):
        occurences[i] = sides.count(sides[i])
    return occurences

def is_valid_triangle(sides):
    #a + b ≥ c
    condition_1 = sides[0] + sides[1] >= sides[2]
    #b + c ≥ a
    condition_2 = sides[1] + sides[2] >= sides[0]
    #a + c ≥ b
    condition_3 = sides[0] + sides[2] >= sides[1]
    return sides.count(0) == 0 and condition_1 and condition_2 and condition_3
