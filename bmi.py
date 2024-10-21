def calculate_bmi(height,weight):
    print("Height = " + height)
    print("Weight = " + weight)

calculate_bmi(weight="57", height="1.73")
#calculate_bmi(1.73,57)

def calculate_bmi_2(height,weight):
    bmi = weight/(height*height)
    return bmi

bmi_value = calculate_bmi_2(1.73,57)
if bmi_value < 18.5:
    print("Under weight")
elif bmi_value<=25.0:
    print("Normal Weight")
else:
    print("Over Weight")
