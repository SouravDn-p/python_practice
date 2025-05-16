def my_recursion(k):
    if(k > 0):
        result = k + my_recursion(k - 1)
        print(result)
        return result
    else:
        result = 0
        return result

print("\n\nRecursion Example Results")
my_recursion(6)