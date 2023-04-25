# given class scores in a list and an integer of your score, see if your score is greater than the class avg.
# you should be considered part of the class when calculating the class average.

# the limiting factor here is sum(), which has O(n) time complexity. Space complexity is
# likewise O(n), again mostly from the input.

def better_than_average(class_points, your_points):
    # Your code here
    avg = (sum(class_points)+your_points) / (len(class_points)+1)
    return True if your_points > avg else False