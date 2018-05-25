def fib(n):
        previous, result = 0 , 1;
        x = 0
        while(x < n -1):
                temp = result
                result = previous + result
                previous = temp
                x = x +1;
        return result;
fib(8)
