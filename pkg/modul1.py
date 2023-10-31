from pkg.modul1 import *
from pkg.modul2 import *

def fungsi1():
    print('memanggil fungsi 1 yang ada di modul1')

def fungsi2():
    print('memanggil fungsi 2 yang ada di modul1')

def main():
    #memanggil fungsi 1 yang ada di dalam modul 1
    #memanggil fungsi yang ada di dalam modul 2
    fungsi1()
    fungsi2()
    fungsi3()
    fungsi4()
if __name__ == '__main__':
    main()