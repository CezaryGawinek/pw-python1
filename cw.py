#====================================================
#           suma cyfr liczby calkowitej
#====================================================
def counting(x:str):
    summa=0
    if x.isdigit():
        for num in x:
            summa+=int(num)
        return summa
    else:
        print("Please enter numbers only")

print(counting("555"))

#====================================================
#             licznik BMI na 1 funkcje
#====================================================
def BMI_counter(weight:float,height:float):
    BMI = weight/(height**2)
    if BMI < 18.5:
        result="Underweight"
    elif 18.5 < BMI < 24.9:
        result="Healthy weight"
    elif BMI > 24.9:
        result="Overweight"
    return result

print(BMI_counter(86,1.9))

#====================================================
#             licznik BMI na 2 funkcje
#====================================================
def BMI_counter2(weight:float,height:float): # -> bool:
    BMI = weight/(height**2)
    return BMI

def BMI_result(BMI:float):
    if BMI < 18.5:
        result="Underweight"
    elif 18.5 < BMI < 24.9:
        result="Healthy weight"
    elif BMI > 24.9:
        result="Overweight"
    return result
# try:
#     weight = input("Enter your weight: ")
#     height = input("Enter yor height: ")


print(BMI_counter2(86,1.9))
print(BMI_result(23.8))