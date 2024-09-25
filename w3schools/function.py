def my_function():
	print("Hello from a function")
def my_function2(fname, lname):
	print(fname + " " + lname)
def my_function3(*kids):
	print("The youngest child is " + kids[2])
def my_function4(**kid):
	print("His last name is " + kid["lname"])

my_function4(fname = "Tobias", lname = "Refsnes")

my_function3("Emil", "Tobias", "Linus")

my_function2("Emil", "Refsnes")
my_function()
x = lambda a : a + 10
print(x(5))
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
