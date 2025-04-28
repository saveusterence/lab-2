def main():
    h = float(input("Enter your Height: "))
    w= float(input("Enter your Weight: "))
    bmirange(bmi(h,w))
def bmi(height,weight):
    print("The height is " + str(height))
    print("The weight is " + str(weight))
    bmi = weight/(height**2)
    print("The bmi is " +str(round(bmi,2)))
    return bmi
def bmirange(bmi):
    if (bmi <18.5):
        print("Under Weight")
    elif (bmi <= 25):
        print("Normal Weight")
    else:
        print("Over Weight")
if __name__ == "__main__":
    main()