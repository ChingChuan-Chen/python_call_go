import os

os.system("go build -buildmode=c-shared -o libtest.dll test.go")

import ctypes
exportgo = ctypes.cdll.LoadLibrary("libtest.dll")

exportgo.printBye()
exportgo.sum(1, 2)
