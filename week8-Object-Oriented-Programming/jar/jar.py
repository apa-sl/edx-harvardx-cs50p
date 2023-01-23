# CS50p Problem Set 8: Cookie Jar
# https://cs50.harvard.edu/python/2022/psets/8/jar/
#
# Goal: create a program with cookie jar management using classes
# Author: Adam Labedzki 2023-01-22

class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size


    def __str__(self):
        """ returns string with number of cookies in the jar """
        return "🍪" * self.size


    def deposit(self, n):
        """ add n cookies to the jar """
        if (self.size + n) > self.capacity:
            raise ValueError("Jar will not hold so much cookies!")
        self.size += n


    def withdraw(self, n):
        """ remove n cookies from the jar """
        if self.size - n < 0:
            raise ValueError("There are to little cookies in the jar")
        self.size -= n


    @property
    def capacity(self):
        """ getter returns total capacity of the jar """
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        """ setter setting jar's capacity """
        if not int(n) > 0:
            raise ValueError("Not a non-netagive intiger")
        self._capacity = n


    @property
    def size(self):
        """ getter returns curent number of cookies in the jar """
        return self._size

    @size.setter
    def size(self, n=0):
        """ setter sets number of cookies in the jar """
        if int(n) < 0:
            raise ValueError
        self._size = n


def main():
    # some jar class testing
    jar = Jar(13)
    print(f"Jar capacity: {jar.capacity}")
    print(f"Jar has {jar.size} cookies inside")
    jar.deposit(13)
    print(f"Jar has {jar.size} cookies inside")
    jar.withdraw(10)
    print(f"Jar has {jar.size} cookies inside")
    print(jar)


if __name__ == "__main__":
    main()