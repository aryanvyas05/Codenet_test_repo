import ctypes

# Load the compiled C library
lib = ctypes.CDLL("./utils.so")

# Define argument and return types
lib.factorial.argtypes = [ctypes.c_int]
lib.factorial.restype = ctypes.c_int

def main():
    n = 5
    print(f"Factorial of {n} (from C) is {lib.factorial(n)}")

if __name__ == "__main__":
    main()
