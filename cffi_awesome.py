from cffi import FFI

import os
os.system("go build -buildmode=c-shared -o awesome.dll awesome.go")

ffi = FFI()

ffi.cdef("""
typedef long long GoInt;

typedef struct {
    void* data;
    GoInt len;
    GoInt cap;
} GoSlice;

typedef struct {
    const char *data;
    GoInt len;
} GoString;

GoInt Add(GoInt a, GoInt b);
double Cosine(double v);
void Sort(GoSlice values);
GoInt Log(GoString str);
""")

lib = ffi.dlopen("awesome.dll")

print("awesome.Add(12,99) = %d" % lib.Add(12,99))
print("awesome.Cosine(1) = %f" % lib.Cosine(1))

data = ffi.new("GoInt[]", [74,4,122,9,12])
nums = ffi.new("GoSlice*", {'data':data, 'len':5, 'cap':5})
lib.Sort(nums[0])
print("awesome.Sort(74,4,122,9,12) = %s" % \
      [ffi.cast("GoInt*", nums.data)[i] for i in range(nums.len)])

data = ffi.new("char[]", b"Hello Python!")
msg = ffi.new("GoString*", {'data':data, 'len':13})
print("log id %d" % lib.Log(msg[0]))
