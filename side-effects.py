def side_effectless_aka_pure_func(x, y):
   return x + y

def side_effect_that_modifies_enclosing_context(x, y):
    print("I'm modifying the environment because I'm printing to the console")
    return x + y

def side_effect_that_modifies_a_parameter_ref_in_place(x, y, d):
    d["key"] = 0
    return x + y

VALUE = 0
def side_effect_that_modifies_a_value_in_enclosing_scope(x, y):
    VALUE += 1
    return x + y

# relation to idempotency
""" A trivial example is storing a value in cache (like in an in-memory map) once so you don't have to repeat an expensive computation (memoization)
Updating that cache is a side effect. """ 


# memoization and caching

""" A cache in this instance is an implementation detail of how I achieve memoization """ 


# importance of memoization 
""" So if you inspect a lot of commonly used Python data libs
They usually implement memoization via Python decorators and dicts
""" 


""" (For future reference: memoization isn't used as commonly in Go because you can fanout/copy the same values and direct them down different channels to achieve the same effect) """ 


""" But when you're building a data pipeline what you should try to do is yield (and its variants from functions) whenever possible and chain those steps """ 


""" Yield is a mechanism to achieve a form of lazy evaluation """

