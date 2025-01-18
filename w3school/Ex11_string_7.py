# Исходная строка
a = "hello, World!"

# capitalize
print("capitalize:", a.capitalize())

# casefold
print("casefold:", a.casefold())

# center
print("center:", a.center(20, "-"))

# count
print("count:", a.count("l"))

# encode
print("encode:", a.encode())

# endswith
print("endswith:", a.endswith("!"))

# expandtabs
b = "H\te\tl\tl\to"
print("expandtabs:", b.expandtabs(4))

# find
print("find:", a.find("World"))

# format
print("format:", "Hello, {}!".format("Python"))

# format_map
mapping = {"name": "John", "age": 25}
template = "My name is {name} and I am {age} years old."
print("format_map:", template.format_map(mapping))

# index
print("index:", a.index("World"))

# isalnum
print("isalnum:", "hello123".isalnum())

# isalpha
print("isalpha:", "hello".isalpha())

# isascii
print("isascii:", a.isascii())

# isdecimal
print("isdecimal:", "123".isdecimal())

# isdigit
print("isdigit:", "123".isdigit())

# isidentifier
print("isidentifier:", "variable_name".isidentifier())

# islower
print("islower:", a.islower())

# isnumeric
print("isnumeric:", "12345".isnumeric())

# isprintable
print("isprintable:", a.isprintable())

# isspace
print("isspace:", "   ".isspace())

# istitle
print("istitle:", "Hello World".istitle())

# isupper
print("isupper:", "HELLO".isupper())

# join
iterable = ["Python", "is", "fun"]
print("join:", " ".join(iterable))

# ljust
print("ljust:", a.ljust(20, "-"))

# lower
print("lower:", a.lower())

# lstrip
print("lstrip:", "   hello   ".lstrip())

# maketrans and translate
table = str.maketrans("aeiou", "12345")
print("translate:", a.translate(table))

# partition
print("partition:", a.partition(","))

# replace
print("replace:", a.replace("World", "Python"))

# rfind
print("rfind:", a.rfind("l"))

# rindex
print("rindex:", a.rindex("l"))

# rjust
print("rjust:", a.rjust(20, "-"))

# rpartition
print("rpartition:", a.rpartition(","))

# rsplit
print("rsplit:", a.rsplit(",", 1))

# rstrip
print("rstrip:", "   hello   ".rstrip())

# split
print("split:", a.split(","))

# splitlines
multiline = "Hello\nWorld\nPython"
print("splitlines:", multiline.splitlines())

# startswith
print("startswith:", a.startswith("hello"))

# strip
print("strip:", "   hello   ".strip())

# swapcase
print("swapcase:", a.swapcase())

# title
print("title:", a.title())

# upper
print("upper:", a.upper())

# zfill
print("zfill:", "42".zfill(5))
