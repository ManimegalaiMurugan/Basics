principle =float(input("Enter the total amount"))
time = float(input("Enter the total number of years"))
rate = float(input("Enter the interest"))
CI = principle * (pow((1 + rate / 100), time))
print(CI)
