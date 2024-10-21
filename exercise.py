def main():
    print("ET0735 (DevOps for AIot) - Lab2 - Introductin to python")
    display_main_menu()
    num_list = get_user_input()

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
    print(list_array)


if __name__ == "__main__":
    main()