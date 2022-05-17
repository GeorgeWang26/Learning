# **Compile Python**

add this to top of .py so cython uses python3 `#cython: language_level=3`

## **Executable** ##
 
to compile into executable
```
cython3 --embed -o hello.c hello.py
gcc -Os -I /usr/include/python3.x -o hello hello.c -lpython3.xm -lpthread -lm -lutil -ldl
./hello
```
`gcc <C_file_from_cython> -I<include_directory> -L<directory_containing_libpython> -l<name_of_libpython_without_lib_on_the_front> -o <output_file_name>`

## **Shared library (.so)**
In compile.py (will generate .so file)
```
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
 

ext_modules = [
    Extension("say_hello", ["hello.py"]) # the generated file will be say_hello.so
]
 

for e in ext_modules:
    e.cython_directives = {​​​​'language_level': "3"}​​​​​​​​​​​ # all are Python-3
 

setup(
    name = 'My_Program_Name',
    cmdclass = {​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​'build_ext': build_ext}​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​,
    ext_modules = ext_modules
)​​
```

run `python compile.py build_ext --inplace` to get .so files \
In main.py (wrapper used to execute .so files)
```
from say_hello import hi

hi() # suppose hi() is a function in say_hello.so, which is originally hello.py
```
