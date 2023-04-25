# build a pyramid-shpaed tower as an array/list of strings, given a positive integer
# "number of floors"

#complexity this solution has to loop through the number of floors. The rest of
# my answer runs in constant time, so the loop determines the time complexity,
# which is O(n). Looks like space complexity would be the list we're building,
# which I think is also O(n).

# looks to me like each floor will have its (floor number *2)-1 stars in it, with an equal
# number of spaces to either side, with each floor having the "length" of the tower's 
# widest floor.
def tower_builder(n_floors):
    # build here
    solution = []
    max = (n_floors*2)-1
    for ele in range(1,n_floors+1):
        stars = (2*ele)-1
        padding = int((max-stars)/2)
        solution.append((" "*padding) + ("*"*stars) + (" "*padding))
        
    return(solution)