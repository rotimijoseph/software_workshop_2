from flask import Flask 
import math

app = Flask(__name__)

@app.route("/<int:num>")
    
def find_prime_factors(num):
    factors = []
    divisor = 2

    while divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num = num / divisor
        else:
            divisor += 1

    all_factors = " ".join(str(num) for num in factors)
    return f"The factors are: {all_factors}"
