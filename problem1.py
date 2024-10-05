"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def problem1(num1, num2, limit):
    # find all multiples of num1 and num2 below limit
    multiplesOfNumOne = [i * num1 for i in range(limit) if i * num1 < limit]
    multiplesOfNumTwo = [j * num2 for j in range(limit) if j * num2 < limit]

    combinedMultiplesWithoutDuplicates = set(multiplesOfNumOne + multiplesOfNumTwo)

    total = sum(combinedMultiples)
    return total


x = problem1(3, 5, 1000)
print(x) # # 233168
