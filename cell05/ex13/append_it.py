import sys

def main():
    args = sys.argv[1:]
    found = False

    for arg in args:
        if not arg.endswith("ism"):
            print(f"{arg}ism$")
            found = True
    
    if not found:
        print("none$")

if __name__ == "__main__":
    main()