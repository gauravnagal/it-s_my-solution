'''
Write a program that prints the numbers from 1 to 50. But for
multiples of three print "Fizz" instead of the number and for
the multiples of five print "Buzz". For numbers which are
multiples of both three and five print "FizzBuzz"
'''

for fizzbuzz in range(1, 51):
    fizz = (fizzbuzz % 3 == 0)
    buzz = (fizzbuzz % 5 == 0)
    if fizz and buzz:
        print('FizzBuzz')
    elif fizz:
        print('Fizz')
    elif buzz:
        print('Buzz')
    else:
        print(fizzbuzz)