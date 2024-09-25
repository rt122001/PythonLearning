a = "Hello, World!"
print(a[1])

for x in "banana":
	print(x)

txt = "The best things in life are free!"
print(txt)
if "free" in txt:
	print("Yes, 'free' is present.")

if "expensive" not in txt:
	print("Yes, 'expensive' is not present.")

b = " Hello, World!     "
print(b[2:5])
print(b[2:])
print(b[:5])
print(b[-5:-2])

print(b.upper())
print(b.lower())
print(b.strip())
print(b.replace('H','J'))
print(b.split(','))

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)
