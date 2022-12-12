import sys
if len(sys.argv) > 2:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print("sum = %d" % (a + b))
    except ValueError:
        print("failed to parse all arguments as integers.")
        exit(1)
else:
    print("Not enough numbers to add")
