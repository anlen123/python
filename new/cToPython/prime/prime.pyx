cdef extern from "_prime.h":
    cdef int _is_prime(int i)

def is_prime(int i):
    return bool(_is_prime(i))