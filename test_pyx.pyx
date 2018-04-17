import os
import csv
import datetime
import time
import math
from math import sqrt, pow, floor
import numpy as np
cimport numpy as np
from cpython cimport bool

cdef class CythonTestClass(object):     
    cdef public bool is_initialized
    cdef double std
    cdef var_array1
    cdef var_array2
    def __init__(self, arg):
        pass
