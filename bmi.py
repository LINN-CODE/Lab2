def calculate_bmi(height,weight):
    print("Height = " + height)
    print("Weight = " + weight)

calculate_bmi(weight="57", height="1.73")
#calculate_bmi(1.73,57)

def calculate_bmi_2(height,weight):
    bmi = weight/(height*height)
    if bmi < 18.5:
        print("Under weight")
        return -1
    elif bmi<=25.0:
        print("Normal Weight")
        return 0
    else:
        print("Over Weight")
        return 1
    
bmi_value = calculate_bmi_2(1.73,57)


