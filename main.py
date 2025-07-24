def total_sum(array):
    total = 0
    for i in array:
        total += i
    return total

def total_avg(array):
    total = 0
    count = 0
    for i in array:
        total += i
        count += 1
    avg = total / count
    return avg

def positive_negative(array):
    positive = 0
    negative = 0
    for i in array:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
    return positive, negative

def area_triangle(base, height):
    area = (base * height) / 2
    return area

def even(num):
    return num % 2 == 0

def max_min(array):
    maximum = max(array)
    minimum = min(array)
    return maximum, minimum







