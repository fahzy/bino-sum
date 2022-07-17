import argparse

def function_F(N: int, K: int):
    pass

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--textfile", help="The name of the textfile to be read.")

args = parser.parse_args()

if args.textfile:

    name: str = str(args.textfile)
    f = open(name,"r")
    line: str = f.readline()
    
    if not line:
        print("Number of test cases needed")
        exit()

    test_cases: int = int(line)

    sum: int = 0
    DENOMINATOR: int = 1000000007
    T, N, P = (0, 0, 0)
    line: str = ""

    for x in range(test_cases):
        line = str(f.readline()).strip()

        broken: str = line.split(" ")
        T = int(broken[0])
        P = int(broken[1])

        if T < 1 or T > 1000:
            print("T cannot be less than 1 nor can it be greater than 1000")
            continue
        if N < 1 or N > 1000:
            print("T cannot be less than 1 nor can it be greater than 1000")
            continue

        



    f.close()

    
else:
    print("Textfile name not given, cannot perform operation.")

# if __name__ == "__main__":
