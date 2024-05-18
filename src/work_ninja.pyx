cdef class MyTask:
    cdef int data

    def __init__(self, int data):
        self.data = data

    cpdef int run(self):
        return self.data * 2