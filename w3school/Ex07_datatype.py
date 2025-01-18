'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''
x = "Hello World"
x = 20
x = 20.5
x = 3+4j # j -> 1j
print(x)
x = ["apple", "banana", "cherry"] #array
print(x)
x = ("apple", "banana", "cherry") #tuple
x = range(6)
print(x)
x = {"John" : "John", "age" : "36"} #dict
print(x)
x = {"apple", "banana", "cherry"} # set
x = frozenset({"apple", "banana", "cherry"}) #frozenset
print(x)
x = True
print(x)
x = b"Hello" #bytes
print(x)
x = bytearray(5) #bytearray
print(x)
x = memoryview(bytes(5))
print(x)
x = None
print(x)


x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j) #complex_number = complex(real, imag)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))