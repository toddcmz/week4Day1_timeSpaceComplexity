# return formatted text strings based on how many names are in the "liked the thing" string. There are 5 
# possible cases, each accounted for manually.

# my solution should run in O(1) constant time, and should take up O(n) space. 
# len() is constant time complexity, and I don't do any looping through the input.
# the string's input takes up n space with only constant auxillary space.

def likes(names):
    # your code here
    if len(names) > 3:
        return(names[0]+", "+names[1] + " and "+str(len(names)-2)+" others like this")
    elif len(names) == 3:
        return(names[0]+", "+names[1] + " and "+names[2]+" like this")
    elif len(names) == 2:
        return(names[0]+" and "+names[1] +" like this")
    elif len(names) == 1:
        return(names[0]+ " likes this")
    else:
        return("no one likes this")