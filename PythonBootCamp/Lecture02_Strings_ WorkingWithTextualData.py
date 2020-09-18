#print a message directly

print('Hello World!!')

#print a message using variable

message='Hello World!!'
print(message)

#print a message with single comma

message = 'It\'s my life' #using escape character
msg = "It's my life" #using double quotes to differentiate with single inverted comma
msgdq = 'Let us say "Hurray!!!"' #using single quotes to differentiate with double inverted comma

print(message)
print(msg)
print(msgdq)

#print a message in multiple lines

message = """Hi,
How are you doing?"""
msg = '''Hi,
Wassup Mannnnn ?'''
print(message)
print(msg)

#print the number of characters in string
message = 'Hello World!!!'
print(len(message))
print(len('Wassup'))

#print the character present at specific index in string
print(message[0])
print(message[6])

#print the characters between the range
print(message[0:5]) # : is symbol of range, 0 is starting index i.e. from which index you wanna print the characters, 5 is the stop index
# i.e. till how many characters you wanna print the characters, keep in mind that 5 will not print character that includes index 5
print(message[:5])# behaves as above, it will start with 0 index with starting index is left blank
print(message[6:9])
print(message[5:]) # if stop index is not provided then it will print the characters till the last index of string

#Refer SLICING VIDEO in details

print(message.lower()) #print message in lower case
print(message.upper()) #print message in upper case

print(message.count('l')) #print occurrences of letter in string
print(message.count('Hello')) #print occurrences of word in string

print(message.find('l')) #print the first index of letter in string
print(message.find('World')) #print the first index of word in string
print(message.find('test')) #word does not exist in string

message.replace("Hello","Wassup") #replace a word in string with another word
print(message) #still prints the old string because a new string is created and returned, so need to store it in another variable
new_message=message.replace("Hello","Wassup")
print(new_message)
message=message.replace("Hello","Wassup") #work around to print with same variable name as message
print(message)

greeting='Hello'
name='ShinChan'
message=greeting+name
print(message)
message= greeting+', '+name+'. Welcome!'
print(message)

message= '{}, {}. Welcome!'.format(greeting, name) #{} are called place holders, it is difficult to keep the track of + signs for large
#concatenations, hence place holders are used with string formatter methods to avoid confusion

print(message)
#Refer string formatter video in detail

message= f'{greeting}, {name}. Welcome!' #f_strings: introduced in version 3.6 and above, work same as format method
print(message)

message="Hello World!"
print(dir(message)) #shows the attributes and methods that can be used with string

print(help(str)) #shows the help for str class
print(help(str.lower)) #shows the help for specific method of str class








