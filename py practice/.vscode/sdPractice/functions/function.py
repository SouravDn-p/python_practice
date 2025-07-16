x = "awesome"

def myfunc() :
    global var1
    var1 = "sourav Debnath"
    x = "sourav"
    print("first function is ", x)

myfunc()

print("outside function: " , x)
print("outside global function: " , var1)
