#fibonacci serisi
fib_element=int(input("Enter the number of fibonacci elements:"))
if(fib_element<=0):
    print("Please enter a positive integer")
else:
    fibonacci_series=[]
    first=0
    second=1
    for _ in range(fib_element):
        fibonacci_series.append(first)
        temp=first+second
        first=second
        second=temp
    print(f"The first {fib_element} elements of the fibonacci series:{fibonacci_series}")
