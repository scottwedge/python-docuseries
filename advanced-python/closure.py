## --------------- Closures ---------------
# A closure is an inner function that remembers and has access to variables in the local scope in which it was created even after the outer function has finished executing

def outer_func():
      message = 'hi';

      def inner_func():
            print(message); # free variable inside inner function
      
      # return inner_func(); # return and execute
      return inner_func; # only return

# outer_func();
my_func = outer_func(); # this variable is assigned to inner_func, we are doen with the execution of outer_func but we still can have access to inenr_func
my_func();