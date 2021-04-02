name = "Osama"
age = "38"
country = "Egypt"

print("Hello "+"'"+name+"' "+ 'How you doing \\ """ '+ 'Your age is "' + age +'"" + and your country is: ' + country )

print("Hello "+"'"+name+"' " + 'How you doing \\\n """ ' +
      'Your age is "' + age + '"" + \n and your country is: ' + country)

name_zero = "Elzero"
print('Second letter is "%s"' %name_zero[1])
print('Third letter is "%s"' %name_zero[2])
print('Last letter is "%s"' %name_zero[-1])


print(name_zero[1:4])
print(name_zero[0::2])
print(name_zero[-2::-2])

name = "#@#@Elzero#@#@"
print(name_zero.strip('#@'))

num = "9"
print(num.zfill(4))


name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20,'@'))
print(name_two.rjust(20,'@'))

name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())

msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))

name = "Elzero"
print(name.find('z'))


msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace('<3',"Love",1))
print(msg.replace('<3',"Love"))

name = "Osama"
age = 38
country = "Egypt"

print("My Name Is {}, And My Age Is {}, And My Country Is {}" .format(
    name, age, country))


