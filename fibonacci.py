def fibonacci():
    """Calculates the fibonacci numbers, then returns them via generator."""
    a, b = 1, 1
    while 1:  # Always true. Not problematic due to how generators work.
        yield a
        # By simultaneously assigning multiple variables, I can skip the temporary variable "z" from the initial solution:
        a, b = b, a+b
