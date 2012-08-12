def user_input(type):
    """
    uses parameter type to choose what to be used for input
    1 = number input
    2 = string input
    """
    if type == 1:
        while True:
            i = raw_input("> ") # = in for this func
            if i.isdigit():
                return int(i)
            else:
                print "Incorrect input."
    
    elif type == 2:
        return raw_input("> ")


def common(func,args):
    funcs = ["look", "help", "go"]
    if func in funcs: # if the given func is in funcs list
        if func == funcs[0]: # look
            ####
        elif func == funcs[1]: # help
            #### print HELP
        elif func == funcs[2]: # go
            

