# tolerance calculator considers the material and level of precicion of the parts
# variables definition quality leve
coarsev = 0.0075
mediumv = 0.005
highv = 0.003
POR = 0.003
uservalue = float(input("enter the dimension value  "))
uservalue_quality = input("Enter the quality level : coarse ,medium , high ")
if uservalue_quality == "coarse":
    x = uservalue*coarsev
    print("toleance range is:", x)
elif uservalue_quality == 'medium':
    x = uservalue*mediumv
    print("toleance range is:", x)
elif uservalue_quality == 'high':
    x = uservalue*highv
    print("toleance range is:", x)
print("not entered value")
