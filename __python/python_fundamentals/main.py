# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi( name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    x = "hello world"
    print(x)
    y = 42
    print(y)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("hello world")
x = "mohammad raddad"
print(x)
print("hello"       ,x )  # this with space
print("hello"+x  )# and this without space
w= 4815162342


# 1. TASK: print "Hello World"
print(  "hello world")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print ( "hello ",name )	# with a comma
print("hello"+name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print(" ",name)	# with a comma
#print(" "+name )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "hello".format(fave_food2,fave_food1))  # with .format()
#format(fave_food1,fave_food2)
print (  fave_food2 )  # with an f string