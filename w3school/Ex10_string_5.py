"""age = 36
txt = "My name is John, I am " + age
print(txt)
ERROR"""

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)


price = 59
txt = f"The price is {price:.2f} dollars" #a modifier is included by adding a colon : followed by a legal formatting type
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)


price = 400
txt = "The price is {} dollars".format(price)
print(txt)


price = 400
txt = "The price is {} dollars".format(price)
print(txt)

name = "Alice"
greeting = "Hello, my name is {0} and I am {1} years old. {0} is my name.".format(name, age)
print(greeting)  

pi = 3.14159
formatted = "Pi is approximately {:.2f}".format(pi)
print(formatted)  # Выведет: Pi is approximately 3.14

