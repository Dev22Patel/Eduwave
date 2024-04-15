from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from .forms import CustomRegistrationForm
from .models import UserProfile

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)

            try:
                user_profile = UserProfile.objects.get(user=user)
                user_role = user_profile.role  
            except UserProfile.DoesNotExist:
                user_role = 'default_role'  

            
            request.session['user_role'] = user_role

            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')  


def register(request):
    if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "New user account created") 
            return redirect('index')  
        else:
            print(register_form.errors)  
    else:
        register_form = CustomRegistrationForm()
    
    return render(request, 'register.html', {'register_form': register_form})




import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random Number:", random_number)

import math

# Define a function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Define a function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Define a function to calculate the square root of a number
def square_root(n):
    return math.sqrt(n)

# Define a function to generate Fibonacci sequence up to a given limit
def fibonacci(limit):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Define a function to calculate the area of a circle
def circle_area(radius):
    return math.pi * radius ** 2

# Define a function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

# Define a function to calculate the area of a triangle
def triangle_area(base, height):
    return 0.5 * base * height

# Define a function to calculate the volume of a sphere
def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

# Define a function to calculate the volume of a cylinder
def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

# Define a function to calculate the volume of a cone
def cone_volume(radius, height):
    return (1/3) * math.pi * radius ** 2 * height

# Define a function to calculate the area of a trapezoid
def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

# Define a function to calculate the circumference of a circle
def circle_circumference(radius):
    return 2 * math.pi * radius

# Define a function to calculate the perimeter of a rectangle
def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Define a function to calculate the perimeter of a triangle
def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

# Define a function to calculate the hypotenuse of a right triangle
def hypotenuse(side1, side2):
    return math.sqrt(side1 ** 2 + side2 ** 2)

# Define a function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Define a function to convert temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Define a function to check if a year is a leap year
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Define a function to calculate the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Define a function to calculate the least common multiple (LCM) of two numbers
def lcm(a, b):
    return (a * b) // gcd(a, b)

# Define a function to generate a list of prime numbers up to a given limit
def generate_prime_numbers(limit):
    prime_numbers = []
    for num in range(2, limit+1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Define a function to reverse a string
def reverse_string(string):
    return string[::-1]

# Define a function to check if a string is a palindrome
def is_palindrome(string):
    return string == reverse_string(string)

# Define a function to count the number of vowels in a string
def count_vowels(string):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in string if char in vowels)

# Define a function to count the number of words in a string
def count_words(string):
    return len(string.split())

# Define a function to calculate the sum of digits in a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Define a function to check if a number is an Armstrong number
def is_armstrong_number(n):
    num_digits = len(str(n))
    return n == sum_of_digits(n) ** num_digits

# Define a function to generate a list of Armstrong numbers up to a given limit
def generate_armstrong_numbers(limit):
    armstrong_numbers = []
    for num in range(1, limit+1):
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
    return armstrong_numbers


