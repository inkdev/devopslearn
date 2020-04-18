import sys
from math import sqrt

if len(sys.argv) < 4:
    print('Please, enter three integer digits')
    sys.exit()
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    p = (a + b + c) / 2
    try:
        S = sqrt((p * (p - a) * (p - b) * (p - c)))
        print(S)
    except ValueError:
        print("Wrong size of sides")

