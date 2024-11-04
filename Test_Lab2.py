import bmi
import exercise

print("Test Lab2")

def test_find_min_max():
    result = []
    input_arr = [ 1, 2, 3, 4, 5]
    test_arr = [1,5]

    result = exercise.large_small(input_arr)

    assert(result == test_arr)

def test_average():
    input_arr = [10,10,10]
    test_arr = 10

    result = exercise.calculate_average(input_arr)

    assert(test_arr == result)

def test_median_temperature():
    input_arr = [1,2,3,4,5]
    test_arr = 3

    result = exercise.func_median(input_arr)

    assert(test_arr == result)