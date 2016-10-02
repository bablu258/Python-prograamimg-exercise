def get_text(name):
   return "My name is, {0} and i don't like decorators".format(name)

def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def main():
    name = (raw_input("Enter your name to demonstrate decorator"))

    print ("*******calling name without decorator*******")
    print (get_text(name))

    print ("********calling name with decorator*********")
    my_get_text = p_decorate(get_text)
    print my_get_text(name)


if __name__== "__main__" :main()