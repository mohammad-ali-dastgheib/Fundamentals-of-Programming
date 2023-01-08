

def sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    i = 0
    while True:
        i += 1
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.001:
            return better, i
        approx = better

# Test cases
print(sqrt(25.0))
print(sqrt(49.0))
print(sqrt(81.0))
