
firstPerson = ("Michael", "Gappa");
secondPerson = ("Tommy", "Gappa");
thirdPerson = ("Robert", "Gappa");

def greetUser(fullName):
    print("Hello {}!\nIt is so nice to meet you {}!\nHopefully, you have a good day, {}!".format(fullName, fullName, fullName))
    
def greetPerson(fullName):
    print("Hello, {} {}!".format(fullName[0], fullName[1]));
    
def additionCalculator(a, b):
    print("The addition of {} and {} is {}".format(a,b, a+b));
    
listOfPeople = [firstPerson, secondPerson, thirdPerson];

print("");

[greetUser(i[0]) for i in listOfPeople]

print("");

greetPerson(firstPerson);
greetPerson(secondPerson);
greetPerson(thirdPerson);

print("");
    
additionCalculator(1, 2);
additionCalculator(84, 684);
additionCalculator(10047, 208);

print("");
# Modify Addition Calculator so that your function returns the sum of the two numbers. The printing should happen outside of the function.
def additionCalculator(a, b):
    return a + b;

print("");

print("The addition of {} and {} is {}".format(1,2, additionCalculator(1,2)));

print("");

# 2. Consider the following expression, intended to print the square  root of 16: pow(16,(1/2))
print(16 ** (1/2))

# 3. Define the variables x and y as lists of numbers, and z as a tuple.
x=[1, 2, 3, 4, 5]
y=[11, 12, 13, 14, 15]
z=(21, 22, 23, 24, 25)

# (a) What is the value of 3*x?
print(3*x);
# (b) What is the value of x+y?
print(x+y);
# (c) What is the value of x-y?
print(x - y);
# (d) What is the value of x[1]?
print(x[1]);
# (e) What is the value of x[0]?
print(x[0]);
# (f) What is the value of x[-1]?
print(x[-1]);
# (g) What is the value of x[:]?
print(x[:]);
# (h) What is the value of x[2:4]?
print(x[2:4]);
# (i) What is the value of x[1:4:2]?
print(x[1:4:2]);
# (j) What is the value of x[:2]?
print(x[:2]);
# (k) What is the value of x[::2]?
print(x[::2]);
# (l) What is the result of the following two expressions?
print();
print("");
x[3] = 8
print (x)
# (m) What is the result of the above pair of expressions if the list x were
# replaced with the tuple z?

# (a) What is the value of 3*x?
print(3*z);
# (b) What is the value of x+y?
print(z+y);
# (c) What is the value of x-y?
print(z-y);
# (d) What is the value of x[1]?
print(z[1]);
# (e) What is the value of x[0]?
print(z[0]);
# (f) What is the value of x[-1]?
print(z[-1]);
# (g) What is the value of x[:]?
print(z[:]);
# (h) What is the value of x[2:4]?
print(z[2:4]);
# (i) What is the value of x[1:4:2]?
print(z[1:4:2]);
# (j) What is the value of x[:2]?
print(z[:2]);
# (k) What is the value of x[::2]?
print(z[::2]);
# (l) What is the result of the following two expressions?