from sympy import isprime


class int(int):
    def isPrime(self):
        return isprime(self)


print(int(10).isPrime())
