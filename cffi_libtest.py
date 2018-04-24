import os
os.system("go build -buildmode=c-shared -o libtest.dll test.go")

import sys
from cffi import FFI
is_64b = sys.maxsize > 2**32

ffi = FFI()
if is_64b:
    ffi.cdef("typedef long GoInt;\n")
else:
    ffi.cdef("typedef int GoInt;\n")

ffi.cdef("""
void printBye();
GoInt sum(GoInt p0, GoInt p1);
""")

lib = ffi.dlopen("libtest.dll")

lib.printBye()
lib.sum(1, 2)


