a = [1,2]
b = [1,2]

print(f"type of variable 'a' is: {type(a)}, the value of variable 'a' is: {a}")
print()
print(f"type of variable 'b' is: {type(b)}, the value of variable 'b' is: {b}")
print()
if(a == b):
	print("Condition: a == b")
	print(f"a: {a} is equal to the value of b: {b}")
else:
	print("Condition: a == b")
	print(f"a: {a} is not equal to the value of b: {b}")
print()
if(a is b):
	print("Condition: a is b")
	print(f"a: {hex(id(a))} contains the same reference in memory as b: {hex(id(b))}")
else:
	print("Condition: a is b")
	print(f"a: {hex(id(a))} does not contain the same reference in memory as b: {hex(id(b))}")
