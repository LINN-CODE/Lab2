import bmi
import exercise

print("Test Lab2")

def find_min_max():
    result = []
    input_arr = [ 1, 2, 3, 4, 5]
    test_arr = [1,5]

    result = exercise.large_small(input_arr)

    assert(result == test_arr)