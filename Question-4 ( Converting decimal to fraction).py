'''Write a program that will take a number as input. The program will convert the inputted number to a format, 
which will contain an integer part and a fraction part. The fraction part needs to be reduced to its lowest representation.'''
from fractions import Fraction
input_val = float(input('Enter value: '))
integer = int(input_val)
decimal = input_val - integer

frac = Fraction(decimal).limit_denominator()
print(f'{integer} {frac.numerator}/{frac.denominator}')
