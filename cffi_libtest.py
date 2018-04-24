import os
os.system("go build -buildmode=c-shared -o libtest.dll test.go")

from cffi import FFI

ffi = FFI()
ffi.cdef("""
typedef long long GoInt;
void printBye();
GoInt sum(GoInt p0, GoInt p1);
""")

lib = ffi.dlopen("libtest.dll")

lib.printBye()
lib.sum(1, 2)


