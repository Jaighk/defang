import sys

from defang import *

def main():
    args = sys.argv

    if len(args)<2:
        print("Syntax: defang {input_file} (optional) {output_file}")
        sys.exit()

    input_file = args[1]
    output_file = None

    if len(args) > 2:
        output_file = args[2]

    input = []
    with open(input_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line != "\n":
                input.append(line.strip())

    generate_output(input, output_file)

if __name__== "__main__":
    main()
