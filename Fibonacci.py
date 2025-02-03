#Write a program in a Object Orientated Programming language of your choice to calculate the sum of the first 100 even-valued Fibonacci numbers. 
#Consider efficiency and demonstrate good coding practices.


class Fibonacci:
    def even_fib_sum(self, count):
        a, b, sum_even, n=0,2,0,0
        while n<count:
            sum_even=sum_even+b
            a, b=b, 4*b+a 
            n=n+1
        return sum_even

fib= Fibonacci()
print(fib.even_fib_sum(100))       