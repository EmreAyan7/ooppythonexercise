input_num = int(input("Enter a number: "))
is_prime = True
if input_num <0:

    print("Please enter a positive integer.")
elif input_num>0 and input_num<2:
    print(f"{input_num} is not a prime number.")

else:
    for i in range(2, int(input_num**0.5)+1):
        if input_num % i ==0:
            print(f"{input_num} is not a prime number.")
            is_prime = False
            break
     
    if (is_prime):
        print(f"{input_num} is a prime number.")
       
    else :
        print(f"{input_num} is not a prime number.")
