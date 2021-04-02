# --- Numbers ---

# Integer

print(type(10))
print(type(100))
print(type(-10))
print(type(-110))

# Float
print(type(1.500))
print(type(-1.500))
print(type(0.990))
print(type(1000.590))

# Complex

print(type(5+6j))
myComplexNumber = 5+6j

print("Real Part is: {}".format(myComplexNumber.real))
print("Imaginary Part is: {}".format(myComplexNumber.imag))

# [1] You can convert from Int to Float or Complex
# [2] You can convert from Float to Int or Complex
# [3] You can not convert from Complex to any type

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(5+6j)
# print(int(5+6j)) # This is an error convertion


