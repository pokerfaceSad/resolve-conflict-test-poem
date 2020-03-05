class Fibonacci(object):
    
    @staticmethod
    def of(index):
        val0 = 1
        val1 = 1
        if index > 2:
            for _ in range(index-2):
                val2 = val0 + val1
                val0 = val1
                val1 = val2
            return val2
        else:
            return 1

if __name__ == "__main__":
    for i in range(200):
        print("Fibonacci " + str(i+1) + ": " + str(Fibonacci.of(i+1)))


