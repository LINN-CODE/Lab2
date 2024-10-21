def main():
    print("ET0735 (DevOps for AIot) - Lab2 - Introductin to python")
    display_main_menu()
    num_list = get_user_input()
    average = calculate_average(num_list)
    max_min = large_small(num_list)

def display_main_menu():
    print("display_main_menu")

def get_user_input():
    print("Enter the number: ")
    string_array =  input().split(',')
    list_array = []
    for x in string_array:
        print(x)
        list_array.append(float(x))
    #float_array = [float(string) for string in string_array]
    return list_array

def calculate_average(numlist):
    print("The average value is " , sum(numlist)/len(numlist))

def large_small(numlist):
    print("The maximum value is ", max(numlist))
    print("The minimum value is ", min(numlist))

if __name__ == "__main__":
    main()