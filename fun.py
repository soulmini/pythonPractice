# print('hello word');

# x = 5;
# print(x);

# If else conditions 

# if x > 6:
#     print('greater')
#     print('heloo');

# else : print('lower')


# functions in py


def findUnique(number):
    n = len(number)
    xor_sum = 0 # Initialize with the first element

    # for i in range(1, n):  # Start from the second element
    #     xor_sum = xor_sum ^ number[i]

    for num in number : 
        xor_sum = xor_sum ^ num
        # print(num)

    return xor_sum

number = [2, 3, 2]
result = findUnique(number)
print(result)  
