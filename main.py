#!/usr/bin/env python3

import sys
import csv

from argparse import Namespace

from src.arg_processor import process_args
from src.defang import (
        process_iocs,
        generate_output
)


def main():
    args: Namespace = process_args(sys.argv)
    defanged: dict[str, str] = process_iocs(input_file=args.input_file)
    generate_output(defanged_iocs=defanged, output_file=args.output_file)


if __name__== "__main__":
    main()
