def aVeryBigSum(n, ar):
    #
    # Write your code here.
    #
    if not(1<=n<=10):
        return "input invalid for n"
    for i in ar:
        if not(0<=i<=10**10):
            return "invalid input for ar"
    if not(n==len(ar)):
        return "invalid input for length"
    total =0
    for n in ar:
        total+=n
    return total
