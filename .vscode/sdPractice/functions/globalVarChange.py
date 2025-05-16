x = "global variable"

def changeGlobal() : 
    global x
    x = "new global variable"

changeGlobal()

print("global variable x :" , x)
