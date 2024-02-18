# calling my hello.py module
import hello

def loop_func():
   x = 1
   while x< 4:
      print("Hello World!!")
      x+=1

def first_func(name):
   print(f"Hello {name.title()}")


first_func('dave')
first_func('bob')
first_func('cindy')

hello.greet()