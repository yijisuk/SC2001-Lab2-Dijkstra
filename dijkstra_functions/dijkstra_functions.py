import os
import platform
import ctypes


class Dijkstra_Functions:

    def __init__(self):

        base_path = os.path.join("dijkstra_functions", "c")
        self.os_system = platform.system()

        # Establish connections to the C libraries
        if self.os_system == "Darwin" or self.os_system == "Linux":

            self.array_queue = ctypes.CDLL(
                os.path.join(base_path, "array_queue.so"))
            
            self.min_heap_queue = ctypes.CDLL(
                os.path.join(base_path, "min_heap_queue.so"))

        elif self.os_system == "Windows":

            self.array_queue = ctypes.CDLL(
                os.path.join(base_path, "array_queue.dll"))

            self.min_heap_queue = ctypes.CDLL(
                os.path.join(base_path, "min_heap_queue.dll"))
            

        # Configure the input argument types
        self.array_queue.dijkstra.argtypes = [
            ctypes.POINTER(ctypes.POINTER(ctypes.c_int)),  # int **graph
            ctypes.c_int,  # int V
            ctypes.c_int   # int src
        ]

        self.min_heap_queue.dijkstra.argtypes = [
            ctypes.POINTER(ctypes.POINTER(ctypes.c_int)),  # int **graph
            ctypes.c_int,  # int V
            ctypes.c_int   # int src
        ]

        # Configure the return type
        self.array_queue.dijkstra.restype = ctypes.c_double
        
        self.min_heap_queue.dijkstra.restype = ctypes.c_double
